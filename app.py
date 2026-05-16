from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from ai_module.analyzer import InteriorAnalyzer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'webp'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize AI Analyzer
analyzer = InteriorAnalyzer()

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    """Upload page"""
    return render_template('upload.html')

@app.route('/process', methods=['POST'])
def process_image():
    """Process uploaded image and analyze"""
    try:
        # Check if file was uploaded
        if 'room_image' not in request.files:
            flash('No file uploaded', 'error')
            return redirect(url_for('upload_page'))
        
        file = request.files['room_image']
        
        # Check if file is selected
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('upload_page'))
        
        # Validate file
        if not allowed_file(file.filename):
            flash('Invalid file type. Please upload PNG, JPG, or JPEG', 'error')
            return redirect(url_for('upload_page'))
        
        # Get user preferences
        selected_style = request.form.get('style', 'modern')
        budget = request.form.get('budget', 'medium')
        
        # Save file with unique name
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        # Analyze image using AI module
        analysis_result = analyzer.analyze_room(
            filepath, 
            preferred_style=selected_style,
            budget=budget
        )
        
        # Add filename to result
        analysis_result['uploaded_image'] = unique_filename
        analysis_result['selected_style'] = selected_style
        analysis_result['budget'] = budget
        
        return render_template('result.html', result=analysis_result)
    
    except Exception as e:
        flash(f'Error processing image: {str(e)}', 'error')
        return redirect(url_for('upload_page'))

@app.route('/api/quick-analyze', methods=['POST'])
def quick_analyze():
    """API endpoint for AJAX analysis"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Save temporarily
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        # Quick analysis
        result = analyzer.quick_detect(filepath)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)