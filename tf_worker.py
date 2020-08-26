import json
import tensorflow as tf

class Worker(object):

    def __init__(self):
        self.img_height = 64
        self.img_width = 64
        self.model_path = "model/"
        self.class_json = "model/class.json"

    def image_to_tensor(self, data):
        image = tf.image.decode_jpeg(data, channels=1)

        # This will convert to float values in [0, 1]
        image = tf.image.convert_image_dtype(image, tf.float32)

        resized_image = tf.image.resize(image, [self.img_height, self.img_width])

        return resized_image

    @staticmethod
    def load_tf_model():
        # Load model
        model = tf.keras.models.load_model('model/final_model.h5')

        # Print summary of model
        print(model.summary())

        return model

    def evaluate(self, model, image):
        with open(self.filename) as f_in:
            classes =  json.load(f_in)
        model.evaluate