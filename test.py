import cv2

def getcrop(x1,x2,y1,y2):
    img = cv2.imread(r"tmp/demo.png")
    cropimg = img[x1:s2,54:186]
