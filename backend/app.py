import os

import pandas as pd
from flask import Flask, jsonify, request, send_from_directory
from flask.helpers import url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename

CSV_FILES = './csv_files'
ALLOWED = {'csv'}

def allowed_file(filename):
    """Check is file is a CSV."""

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED

def get_files():
    """Return a list of file names and download URLs"""

    files=[]

    for idx,file in enumerate(os.listdir('csv_files/')):
        files.append({'id':idx, 'filename':file,'link':url_for('file_download', name=file)})

    return files

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = CSV_FILES
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/files')
def send_file_list():
    return jsonify(get_files())

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    """Checks if there was a file sent and saves it to the csv_files folder."""

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'ERROR':'NO FILE'})

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
    return jsonify({'OK':'FILE ADDED'})

@app.route('/dl/<name>')
def file_download(name):
    """Receive name of file and sends said file for download."""

    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)

@app.route('/contents/<name>')
def file_contents(name):
    """Receive name of file and create HTML table for data."""
    
    #Could increase if you are willing to wait.
    rows = 300
    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], name))
    df['state'] = df['state'].fillna('BLANK')

    return jsonify(df.to_html(index=False, max_rows=rows))

@app.route('/stats/<name>')
def file_stats(name):
    """Returns the number of rows each year appears in."""

    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], name), parse_dates=['date'], infer_datetime_format=True)
    year_count = df.groupby(df['date'].dt.year).count()

    return jsonify(year_count['date'].rename('Count').to_frame().to_html())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)