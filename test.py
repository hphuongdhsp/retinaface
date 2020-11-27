from retinaface import RetinafaceDetector
import cv2 as cv
import matplotlib.pyplot as plt
def draw_faces(im, bboxes):
    for bbox in bboxes:
        x0, y0, x1, y1 = [int(_) for _ in bbox][:4]
        img = cv.rectangle(im, (x0, y0), (x1, y1), (0, 0, 255), 2)
    return img

### Mobinet backbone 
detector  = RetinafaceDetector(net='mnet').detect_faces
img  = cv.imread('./imgs/DSC_8221.jpg')
bounding_boxes, landmarks = detector(img)

print(bounding_boxes)


### Resnet backbone 
detector  = RetinafaceDetector(net='mnet').detect_faces
img  = cv.imread('./imgs/DSC_8221.jpg')
bounding_boxes, landmarks = detector(img)

print(bounding_boxes)

img = draw_faces(img, bounding_boxes)

plt.imshow(img)

cv.imwrite('./imgs/detect_DSC_8221.jpg', img)
