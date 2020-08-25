from flask import Flask, request
from flask_dropzone import Dropzone

app = Flask(__name__)

dropzone = Dropzone(app)

@app.route('/uploads', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        f = request.files.get('file')

    return "upload template"

if __name__ == '__main__':
    app.run(host="178.128.40.146", debug=True)
