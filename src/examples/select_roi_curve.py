import cv2
import os
import sys
import numpy as np

def selectROI_curve(img):
    mask = np.zeros(image.shape, dtype=np.uint8)
    roi_corners = np.array(points, dtype=np.int32) #pointsOf the polygon Like [[(10,10), (300,300), (10,300)]]
    white = (255, 255, 255)
    cv2.fillPoly(mask, roi_corners, white)

    # apply the mask
    masked_image = cv2.bitwise_and(image, mask)

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
#selectROI_curve(img3)
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
            
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()