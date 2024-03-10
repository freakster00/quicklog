from flask import Flask, jsonify
import threading
import time
from flask_sqlalchemy import SQLAlchemy
import cv2
import uuid
app = Flask(__name__)


def generate_uuid():
    unique_id = uuid.uuid4()
    return unique_id

#Url of the esp32 stream address
stream_url = 'http://192.168.159.210:81/stream'
def capture_frame():
    cap = cv2.VideoCapture(stream_url)
    ret, frame = cap.read()
    cap.release()
    return frame



@app.route('/count')
def index():
    currentFrame = capture_frame()
    uniqueUUID = generate_uuid()
    
    savedPath = f"./savedFrames/{uniqueUUID}.jpg"  # Include file extension
    print(savedPath)
    cv2.imwrite(savedPath, currentFrame)
    count = peopleCounter(savedPath)
    message={
        "Message":"Image Processing Complete",
        "Number of people":count
    }
    return jsonify(message)

from ultralytics import YOLO
from PIL import Image
import numpy as np


model = YOLO('yolov8x.pt')

def peopleCounter(imagePath):
    image = Image.open(imagePath)
    results = model(image)
    cls_values = results[0].boxes.cls.cpu().numpy().flatten()
    counter = np.count_nonzero(cls_values == 0)
    return counter



if __name__ == '__main__':
    app.run(debug=True)
