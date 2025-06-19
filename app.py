import os
from flask import Flask, request, render_template, jsonify
import whisper
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1024MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load Whisper model
model = whisper.load_model("base")

ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a', 'ogg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Transcribe the audio file
            result = model.transcribe(filepath)
            
            # Clean up the uploaded file
            os.remove(filepath)
            
            return jsonify({
                'success': True,
                'transcription': result['text']
            })
        except Exception as e:
            app.logger.error("An error occurred during file processing: %s", e, exc_info=True)
            return jsonify({'error': 'An internal error has occurred. Please try again later.'}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV', 'production') == 'development'
    app.run(debug=debug_mode)