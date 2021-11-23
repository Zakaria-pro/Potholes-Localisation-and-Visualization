from picamera import PiCamera
from time import sleep


#from keras.models import Sequential
#from keras.layers import Dense
#from keras.models import model_from_json
import numpy as np
import os# load json and create model
#from keras.preprocessing import image
import joblib

filename = "model.sav"
loaded_model = joblib.load(filename)
print(loaded_model)
# Load tflite Model
#json_file = open('~/Desktop/SafeRoad/ExportedModel/model.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#loaded_model = model_from_json(loaded_model_json)
#loaded_model.load_weights("~/Desktop/SafeRoad/ExportedModel/model.h5")
#print("Loaded model from disk")

# Init Camera
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
sleep(5)
camera.capture('foo.jpg')

# Prediction
i=0;
def waitDetectedPothole():
    while(1):
        sleep(10)
        print("reading frame"+i)
        frame = camera.capture('/home/pi/Desktop/SafeRoad/images/image%s.jpg' % i)
        test_image = image.load_img( '/home/pi/Desktop/SafeRoad/images/image%s.jpg' %i , target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image) 
        if result[0][0] == 1: # Pothole
            return 1
        i=i+1

camera.stop_preview()