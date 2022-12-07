import cv2
import numpy as np


drawing = False
ix, iy = -1, -1
img = None
orig_img = None
paint_img = None


# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, orig_img, paint_img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = paint_img.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(paint_img, (ix, iy), (x, y), (0, 255, 0), 2)
        img = paint_img.copy()


orig_img = np.ones((600, 800, 3), np.uint8)
img = orig_img.copy()
paint_img = orig_img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('c'):
        paint_img = orig_img.copy()
        img = orig_img.copy()
    elif k == 27:
        break
cv2.destroyAllWindows()
