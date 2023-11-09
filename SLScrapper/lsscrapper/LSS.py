import os
import cv2
from tqdm import tqdm
import cv2
import numpy as np
import imutils
#preprocessing_image_path = '../ejemploAMLO.png'
preprocessing_image_path = '../ce.png'
#preprocessing_image_path = '../example.png'
video_path = '../ejemploAMLO.mp4'
#1280 × 720
img = cv2.imread(preprocessing_image_path)
haar_scale_factor=1.1 
haar_min_neighbors=4
canny_min_value=25
canny_max_value=500
canny_aperture_size=3
structuring_kernel_length=7
structuring_kernel_opening_size=3
morph_open_iterations=10
alpha_addition=0.5
    
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#resized = imutils.resize(img, width=380)
#ratio = img.shape[0] / float(resized.shape[0])
#gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('blah',gray)
    #j=input()
faces = face_cascade.detectMultiScale(gray, haar_scale_factor, haar_min_neighbors)
face_centers = []
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    face_centers.append((x + w/2, y + h/2))
#print(faces)
#cv2.imshow('blah',img)
#cv2.waitKey(0)
edges = cv2.Canny(gray,canny_min_value, canny_max_value, apertureSize = canny_aperture_size)
#cv2.imshow('hhhh',edges)
#cv2.waitKey(0)
#jj=input()
# Straight line detection 
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, structuring_kernel_length))
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (structuring_kernel_length, 1))
opening_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(structuring_kernel_opening_size,structuring_kernel_opening_size))
# vertical lines
vertical_edges_img = cv2.erode(edges, vertical_kernel, iterations=morph_open_iterations)
vertical_edges_img = cv2.dilate(vertical_edges_img, vertical_kernel, iterations=morph_open_iterations)
   
# Morphological operation to detect horizontal lines from an image
horizontal_edges_img = cv2.erode(edges, horizontal_kernel, iterations=morph_open_iterations)
horizontal_edges_img = cv2.dilate(horizontal_edges_img, horizontal_kernel, iterations=morph_open_iterations)
#cv2.imshow('kkk',horizontal_edges_img)
#cv2.waitKey(0)
alpha2_addition = 1.0 - alpha_addition
straight_edges_img = cv2.addWeighted(vertical_edges_img, alpha_addition, horizontal_edges_img, alpha2_addition, 0.0)
#cv2.imshow('Antes',straight_edges_img)  
# Invert image for contours
straight_edges_img = cv2.erode(~straight_edges_img, (structuring_kernel_opening_size, structuring_kernel_opening_size), iterations=2)
(threshold, straight_edges_img) = cv2.threshold(~straight_edges_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#cv2.imshow('despues',straight_edges_img)
# Obtaining contours
#cv2.waitKey(0)
selected_contours = []
(contours, _) = cv2.findContours(straight_edges_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    # approximate contour
    perimeter = cv2.arcLength(contour, True)
    approximation = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    #print(len(approximation))
        
    # approximation has four points, so it is a box
    if len(approximation) >= 4:
        #print('jjj')
        rect_from_polygon = cv2.boundingRect(approximation)
        x, y, w, h = rect_from_polygon
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        #cv2.imshow('Rectan',img)
        #cv2.waitKey(0)
        # height must be greater than width

        for face_index, face_center in enumerate(face_centers):
            if x < face_center[0] < x+w:
                if y < face_center[1] < y+h:
                    selected_contours.append((face_index, rect_from_polygon))
    
print(selected_contours)
    # Only one contour per face
face_to_regions = {}
for face_index, region in selected_contours:
    _, _, w, h = face_to_regions.get(face_index, (0, 0, 0, 0))
    saved_area = w * h

    _, _, w, h = region
    new_area = w * h
        # Keep the largest area
    if saved_area < new_area:
        face_to_regions[face_index] = region
#ff=input()
candidates = face_to_regions.values()


 
for x, y, w, h in candidates:
    cv2.imshow("frame", img[y:y+h,x:x+w])
    
    print("Read signer region from image: %s\n\n Press ESC to continue..." % preprocessing_image_path)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
# Use the region to create videos
video = cv2.VideoCapture(video_path)
if video.isOpened() == False:
    raise Exception("Couldn't open video :(")

# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# Get FPS
if int(major_ver)  < 3 :
    fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
else:
    fps = video.get(cv2.CAP_PROP_FPS)

# Get length
if int(major_ver)  < 3 :
    frame_count = int(video.get(cv2.cv.CAP_PROP_FRAME_COUNT))
else:
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Get output codec
if os.name == "nt":
    ext = "avi"
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
else:
    ext = "mkv"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Get a video for every possible sign language region
video_outputs = []
for i, candidate in enumerate(candidates):
    _, _, video_width, video_height = candidate
    video_outputs.append(cv2.VideoWriter("../newvideo_{0}.{1}".format(i, ext), 
                                         fourcc,
                                         fps,
                                         (video_width, video_height)
                                         )
                        )
with tqdm(total=frame_count, unit=" frames") as pbar:
    while video.isOpened():
        return_code, frame = video.read()
        pbar.update(1)
        if return_code == True:
            for i, candidate in enumerate(candidates):
                x, y, w, h = candidate
                video_outputs[i].write(frame[y:y+h,x:x+w])
        else:
            break

# Close streams
video.release()
for i in range(len(candidates)):
    video_outputs[i].release()
