# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import tflite_runtime.interpreter as tflite


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
width = 64 #640
height = 64 #480
camera.resolution = (width, height)
camera.framerate = 8
rawCapture = PiRGBArray(camera, size=(width, height))


# Setup the model
# -----Load the TFLite model and allocate tensors.--------
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()


# -----Get input and output tensors.----------------------
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
#print("input details :",input_details, "\n")
#print("output details :",output_details)

# -----Verify the model input and output.-----------------
input_shape = input_details[0]['shape'] #  [ 1 64 64  3]

#image = cv2.imread('normal.jpg')
#print('Original Dimensions :', image.shape)

# dim = (input_shape[1], input_shape[2])
# input_data = cv2.resize(image, dim)
# numpy_data = np.asarray(input_data)
# 
# print('Resized Dimension :', input_data.shape)

#cv2.imshow("Resized Image", image)



# allow the camera to warmup
time.sleep(0.1)






# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    # show the frame
    cv2.imshow("Frame", image)
    #print("type of input: ",type(image))
    #print(image[0])
    image.shape = (1, 64, 64, 3)

    
    interpreter.set_tensor(input_details[0]['index'], image.astype('float32')/255) 
    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    prediction = output_data[0][0]
    print("prediction : ", prediction)

    #IF OUTPUT_DATA
    
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
