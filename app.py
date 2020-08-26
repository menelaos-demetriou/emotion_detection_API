import os
from flask import Flask, request, render_template
from tf_worker import Worker
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
# Initialise worker
tensorflow_worker = Worker()
# Load model
model = tensorflow_worker.load_tf_model()

@app.route('/', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        f = request.files.get('file')

        image = tensorflow_worker.image_to_tensor(f)

        print("Hello")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="178.128.40.146", debug=True)