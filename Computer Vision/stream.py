import cv2
from apple_detector import YoloAppleDetector
import sys
# initializing global variables
apple_detector = YoloAppleDetector('/home/spritle/Desktop/kitchenX/weights/yolov3-tiny_apples.weights', '/home/spritle/Desktop/kitchenX/cfg/yolov3-tiny.cfg', '/home/spritle/Desktop/kitchenX/cfg/food.data', ["apples"])
# define a function to read from gstreamer
def gstreamer_pipeline(capture_width=1280,
                       capture_height=720,
                       display_width=1280,
                       display_height=720,
                       framerate=60,
                       flip_method=0,
                       ):
    return (
            "nvarguscamerasrc ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (
                capture_width,
                capture_height,
                framerate,
                flip_method,
                display_width,
                display_height,
            )
    )
def draw_rectangle(img, apple_coords):
    for x1,y1,x2,y2 in apple_coords:
        cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,0))
    return img
#img = cv2.imread("test_image.jpg")
#yolo_out = apple_detector.detect(img, conf=0.2, non_max_suppression=False)
#print("yolo output: ", yolo_out)
#img = draw_rectangle(img, yolo_out)
#cv2.imwrite("output.jpg", img)
#sys.exit()
cap = cv2.VideoCapture(gstreamer_pipeline())
ret, frame = cap.read()
while ret:
    yolo_out = apple_detector.detect(frame, conf=0.2, non_max_suppression=False)
    print("yolo output: ", yolo_out)
    frame = draw_rectangle(frame, yolo_out)
    cv2.imshow("apple detector", frame)
    key_press = cv2.waitKey(1) & 0xFF
    if key_press == ord('q'):
        break
    ret, frame = cap.read()
cap.release()
cv2.destroyAllWindows()

