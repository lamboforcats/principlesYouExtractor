# server.py
from flask import Flask, request, send_file
import main

app = Flask(__name__)

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    file = request.files['file']
    main(file)  # run your script
    return send_file('attributes.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
