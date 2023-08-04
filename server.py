# server.py
from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import os
import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/process_pdf', methods=['GET', 'POST'])
def process_pdf():
    if request.method == 'POST':
        file = request.files['file']
        upload_directory = 'uploads/'
        if not os.path.exists(upload_directory):
            os.makedirs(upload_directory)
        file_path = os.path.join(upload_directory, secure_filename(file.filename))
        file.save(file_path)
        main.process_pdf(file_path)  # run your script
        return send_file('attributes.xlsx', as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
