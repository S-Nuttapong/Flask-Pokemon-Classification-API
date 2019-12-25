from flask import Flask, request, jsonify
from flask_cors import CORS #for disabling cross-origin policy 
from PIL import Image, ImageOps
from base64 import b64decode #decode base64 received from JS
from tensorflow import keras

import io
import numpy as np
import requests #make request
import os
import cv2


with open('pokenet_model/label.txt') as txtf:
    labels = txtf.read().splitlines()
# print(labels)

def preprocessing(encoded_base64):
    decoded_base64 = b64decode(encoded_base64)
    byte_img = io.BytesIO(decoded_base64)
    pil_img = Image.open(byte_img)
    cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    cv_img = cv2.resize(cv_img, (96, 96))

    # since training and validating data were preprocessed by opencv 
    # input images have BGR scale and significantly different pixels after resizing compare to preprocessing with pillow and numpy
    # therefore producing poorer result
    
    # img = Image.open(byte_img)
    # thumb = ImageOps.fit(img, (96, 96), Image.ANTIALIAS)
    # img_numpy = np.array(thumb).reshape(-1, 96, 96, 3)
    # return thumb

    return cv_img

def make_prediction(image):
    img = image.reshape(-1, 96, 96, 3) / 255.0  #BGR scale
    pokemon_model_path = os.path.join(os.getcwd(), 'pokenet_model/best_model.hdf5')
    model = keras.models.load_model(pokemon_model_path)
    
    raw_preds = model.predict(img)[0].tolist()

    preds = {labels[i]:score for i, score in enumerate(raw_preds)}
    Top_preds = {k:v for k, v in sorted(preds.items(), key=lambda item: item[1], reverse=True)} #sorting dict by value (item[1])
    
    return Top_preds


app = Flask(__name__)
CORS(app) #---> disable CORS policy so we can do cross-origin request, quick fix but bad pratice

@app.route("/predict", methods=["POST"])
def home():
    status = {'success': 'Fail'}
    raw_response = request.form.get('image').split(',')
    encoded_base64 = raw_response[1]  #raw_response[0] for meta_data --> ()
    img = preprocessing(encoded_base64)
    # cv2.imshow('image', img)
    try:
        Top_preds = make_prediction(img)
        response = jsonify(Top_preds)
        response.status_code = 200
        print('Top predictions: ')
        print(Top_preds)
    except:
        response = jsonify(status)
        response.status_code = 500
    return response

app.run(host="0.0.0.0", debug=False)


