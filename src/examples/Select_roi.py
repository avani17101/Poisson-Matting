import cv2
import os
import sys
def selectROI(img):
    roi = cv2.selectROI(img)
    print(roi)
    st = ""
    for r in roi:
    	st += str(r)
    	st += " "
    f = open('coords.txt','w+')
    f.write(st)
    f.close()
    	
IMAGES_FOLDER_PATH = "../img"
img_path = os.path.join(IMAGES_FOLDER_PATH, 'img3.png')
if(len(sys.argv)>1):
	img_path = (sys.argv[1])
img3 = cv2.imread(img_path)
selectROI(img3)
