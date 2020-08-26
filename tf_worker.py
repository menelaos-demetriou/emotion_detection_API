import json
import keras
import tensorflow as tf
from keras.models import model_from_json

class Worker(object):

    def __init__(self):
        self.img_height = 64
        self.img_width = 64
        self.num_classes = 8
        self.metrics = keras.metrics.CategoricalAccuracy(name='accuracy')
        self.checkpoint_path = "model/cp.ckpt.data-00000-of-00001"
        self.class_json = "static/class_mapping.json"
        self.model_path = "model/model.json"
        with open(self.filename) as f_in:
            self.classes =  json.load(f_in)

    def load_model(self):
        json_file = open(self.model_path, "r")
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        return loaded_model

    def image_to_tensor(self, data):
        image = tf.image.decode_jpeg(data, channels=1)

        # This will convert to float values in [0, 1]
        image = tf.image.convert_image_dtype(image, tf.float32)

        resized_image = tf.image.resize(image, [self.img_height, self.img_width])

        return resized_image

    def load_tf_model(self):
        # Create model
        model = self.load_model()

        # Load weights
        model.load_weights(self.checkpoint_path)

        # Print summary of model
        print(model.summary())

        return model

    def get_prediction(self, model, image):
        prediction = model.predict(image)
        return self.classes[str(prediction)]
