# server.py
from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import os
import main

app = Flask(__name__)

# Make sure to create 'uploads' directory in the same path where your server.py file is
UPLOAD_FOLDER = 'uploads/'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/process_pdf', methods=['GET', 'POST'])
def process_pdf():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        main.process_pdf(file_path)  # run your script
        return send_file('attributes.xlsx', as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
