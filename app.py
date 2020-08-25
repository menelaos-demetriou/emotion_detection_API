import os
from flask import Flask, request, render_template
from flask_dropzone import Dropzone

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
)

dropzone = Dropzone(app)

@app.route('/', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        f = request.files.get('file')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="178.128.40.146", debug=True)