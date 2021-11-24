from picamera.array import PiRGBArray
from picamera import PiCamera

import cv2
import numpy as np
import time

#from matplotlib import pyplot as plt



# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
width = 640 #640
height = 480 #480
camera.resolution = (width, height)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(width, height))



# allow the camera to warmup
time.sleep(1)



# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    im = frame.array
#     cv2.resize(im, (width, height))
#     cv2.imshow("Frame", im)
# 
# 
# #     #CONTOUR DETECTION CODE
#     imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#     ret,thresh = cv2.threshold(imgray,127,255,0)
# 
#     contours1, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#     contours2, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 
# #     #img1 = im.copy()
#     img2 = im.copy()
# 
#     #out = cv2.drawContours(img1, contours1, -1, (255,0,0), 2)
#     out = cv2.drawContours(img2, contours2, -1, (250,250,250),1)
#     #out = np.hstack([img1, img2])
#     cv2.imshow('img2',img2)
#     #cv2.waitKey(0)
#     #plt.subplot(331),plt.imshow(im),plt.title('GRAY')
#     #plt.xticks([]), plt.yticks([])
# # #     img = cv2.imread('index2.jpg',0)
# 
#     
# 
#     # Part 2
#     #cv2.cvtColor(im,)
#     ret,thresh = cv2.threshold(imgray,127,255,0)
#     contours,hierarchy = cv2.findContours(thresh, 1, 2) 
#     cnt = contours[0]
#     M = cv2.moments(cnt)
# 
#     #print M
#     perimeter = cv2.arcLength(cnt,True)
#     #print perimeter
#     area = cv2.contourArea(cnt)
#     #print area
#     epsilon = 0.1*cv2.arcLength(cnt,True)
#     approx = cv2.approxPolyDP(cnt,epsilon,True)
#     #print epsilon
#     #print approx
#     for c in contours:
#         rect = cv2.boundingRect(c)
#         if rect[2] < 100 or rect[3] < 100: continue
#         #print cv2.contourArea(c)
#         x,y,w,h = rect
#         cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),8)
#         cv2.putText(img2,'p',(x+w+40,y+h),0,2.0,(255,255,255))
#     cv2.imshow("With contours on frame",img2)
    #cv2.waitKey()  
    #cv2.destroyAllWindows()
    # ---------------------------
#     
    detector = cv2.SimpleBlobDetector()
#     
    keypoints = detector.detect(im)
#     
#     im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     
#     cv2.imshow('Keypoints', im_with_keypoints)
#     cv2.waitKey(0)
    
    # ---------------------------
#     k = cv2.isContourConvex(cnt)
# 
#     #to check convexity
#     #print (k)
#     #blur
#     blur = cv2.blur(im,(5,5))
#     #guassian blur 
#     gblur = cv2.GaussianBlur(im,(5,5),0)
#     #median 
#     median = cv2.medianBlur(im,5)
#     #erosion
#     kernel = np.ones((5,5),np.uint8)
#     erosion = cv2.erode(median,kernel,iterations = 1)
#     dilation = cv2.dilate(erosion,kernel,iterations = 5)
#     #erosion followed dilation
#     closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
#     #canny edge detection
#     edges = cv2.Canny(dilation,9,220)
#     cv2.imshow("Finale result", edges)
# 
#     
    
    
    #cv2.destroyAllWindows()
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# -------------------------------------------------------------------------------------

#plotting using matplotlib
# plt.subplot(332),plt.imshow(blur),plt.title('BLURRED')
# plt.xticks([]), plt.yticks([])
# plt.subplot(333),plt.imshow(gblur),plt.title('guassianblur')
# plt.xticks([]), plt.yticks([])        
# plt.subplot(334),plt.imshow(median),plt.title('Medianblur')
# plt.xticks([]), plt.yticks([]) 
# plt.subplot(337),plt.imshow(img,cmap = 'gray')
# plt.title('dilated Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(338),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(335),plt.imshow(erosion),plt.title('EROSION')
# plt.xticks([]), plt.yticks([])
# plt.subplot(336),plt.imshow(closing),plt.title('closing')
# plt.xticks([]), plt.yticks([])
# plt.show()
# #alerting the driver
# pygame.init()
# pygame.mixer.music.load("buzz.mp3")
# pygame.mixer.music.play()
# time.sleep(5)

#content ="detection of pothole in locality basapura road hosur road junction "
#mail = smtplib.SMTP('smtp.gmail.com',587)
#mail.ehlo()
#mail.starttls()
#mail.login('harika3196@gmail.com','hariammu3196@gmail.com')
#mail.sendmail('fromemail','receiver',content)
#mail.close()
