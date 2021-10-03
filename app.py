import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import sys
from src.new_enc import enc
from src.new_dec import dec

UPLOAD_FOLDER = 'src/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'txt'])
app.secret_key = "secret key"

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/output/")
def output_page():
    return render_template('output.html')

@app.route("/uploadenc/")
def uploadenc_page():
    return render_template('uploadenc.html')

@app.route("/uploaddec/")
def uploaddec_page():
    return render_template('uploaddec.html')

@app.route('/uploadenc/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], "image.jpg"))
		print('upload_image filename: ' + filename)
		enc()
		return render_template('index.html')
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/uploaddec/', methods = ['POST'])
def upload_file():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], "encrypted.txt"))
		print('upload_image filename: ' + filename)
		dec()
		return render_template('index.html')
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)