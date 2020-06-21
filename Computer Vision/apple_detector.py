import cv2
import numpy as np
import math
import requests
from darknet import detect, load_net_custom, load_meta


class YoloAppleDetector:
    def __init__(self, model_weights, model_cfg, obj_data, classes):
        print(model_cfg, model_weights)
        self.net = load_net_custom(model_cfg.encode("ascii"),
                                   model_weights.encode("ascii"),
                                   0, 1)
        self.meta = load_meta(obj_data.encode("ascii"))
        self.class_id = {k:i for i, k in enumerate(classes)}
        self.classes = classes

    def detect(self, img, conf=0.2, nms_thresh=0.3, non_max_suppression=False, class_conf=[]):
        if len(class_conf) < len(self.classes):
            conf = [conf] * len(self.classes)
        else:
            # print("got individual confidences")
            conf = class_conf
        final_result = {}
        apples = []
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print(type(self.net),type(self.meta),type(img),min(conf))
        detections = detect(self.net, self.meta, img, thresh=min(conf), debug=False)
        print("detections are: ", detections)
        for a_detection in detections:
            name, confidence, detection = a_detection
            name = name.decode("utf-8")
            if confidence > conf[int(self.class_id[name])]:
                center_x = int(detection[0])
                center_y = int(detection[1])
                w = int(detection[2])
                h = int(detection[3])
                x = int(center_x - (w / 2))
                y = int(center_y - (h / 2))
                if name == "apples":
                    apples.append((x, y, x + w, y + h))
                    #send post
                    try:
                        url = 'https://flask-iot-kitchen.scm.azurewebsites.net:443/flask-iot-kitchen.git'
                        requests.post(url, data = {'apple': -1}, timeout = None)
                        print("successfully sent post request")
                    except Exception as e:
                        print(e)
                        print("unable to send post request")

                # print(self.classes[class_id], confidence)    
        return apples
