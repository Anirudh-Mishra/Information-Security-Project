from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)