from __future__ import division, print_function, absolute_import
import cv2
import threading
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import os
from timeit import time
import warnings
import sys
import numpy as np
from PIL import Image
from yolo import YOLO
from deep_sort import preprocessing
from deep_sort import nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker
from tools import generate_detections as gdet

class Display:
    def __init__(self, ui, mainWnd):
        self.ui = ui
        self.mainWnd = mainWnd

        # 默认视频源为相机
        self.ui.radioButtonCam.setChecked(True)
        self.isCamera = True

        # 信号槽设置
        ui.Open.clicked.connect(self.Open)
        ui.Close.clicked.connect(self.Close)
        ui.radioButtonCam.clicked.connect(self.radioButtonCam)
        ui.radioButtonFile.clicked.connect(self.radioButtonFile)

        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

    def radioButtonCam(self):
        self.isCamera = True

    def radioButtonFile(self):
        self.isCamera = False

    def Open(self):
        if not self.isCamera:
            self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '')
            self.cap = cv2.VideoCapture()
            if not self.cap.open(self.fileName):
                print("can not open the video")
                exit(1)
            self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        else:
            self.cap = cv2.VideoCapture(0)

        # 创建视频显示线程
        th = threading.Thread(target=self.Display)
        th.start()

    def Close(self):
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()

    def Display(self):
        self.ui.Open.setEnabled(False)
        self.ui.Close.setEnabled(True)

        while self.cap.isOpened():
            # Definition of the parameters
            max_cosine_distance = 0.3
            nn_budget = None
            nms_max_overlap = 1.0

            # deep_sort
            model_filename = 'model_data/mars-small128.pb'
            encoder = gdet.create_box_encoder(model_filename, batch_size=1)

            metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
            tracker = Tracker(metric)

            writeVideo_flag = True

            if writeVideo_flag:
                # Define the codec and create VideoWriter object
                w = int(self.cap.get(3))
                h = int(self.cap.get(4))
                fourcc = cv2.VideoWriter_fourcc(*'MJPG')
                out = cv2.VideoWriter('output.avi', fourcc, 15, (w, h))
                list_file = open('detection.txt', 'w')
                frame_index = -1

            fps = 0.0

            while True:
                ret, frame = self.cap.read()  # frame shape 640*480*3
                if ret != True:
                    break;
                t1 = time.time()

                image = Image.fromarray(frame)
                boxs = YOLO.detect_image(image)
                # print("box_num",len(boxs))
                features = encoder(frame, boxs)

                # score to 1.0 here).
                detections = [Detection(bbox, 1.0, feature) for bbox, feature in zip(boxs, features)]

                # Run non-maxima suppression.
                boxes = np.array([d.tlwh for d in detections])
                scores = np.array([d.confidence for d in detections])
                indices = preprocessing.non_max_suppression(boxes, nms_max_overlap, scores)
                detections = [detections[i] for i in indices]

                # Call the tracker
                tracker.predict()
                tracker.update(detections)

                for track in tracker.tracks:
                    if not track.is_confirmed() or track.time_since_update > 1:
                        continue
                    bbox = track.to_tlbr()
                    cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255, 255, 255), 2)
                    cv2.putText(frame, str(track.track_id), (int(bbox[0]), int(bbox[1])), 0, 5e-3 * 200, (0, 255, 0), 2)

                for det in detections:
                    bbox = det.to_tlbr()
                    cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255, 0, 0), 2)

                cv2.imshow('', frame)

                if writeVideo_flag:
                    # save a frame
                    out.write(frame)
                    frame_index = frame_index + 1
                    list_file.write(str(frame_index) + ' ')
                    if len(boxs) != 0:
                        for i in range(0, len(boxs)):
                            list_file.write(str(boxs[i][0]) + ' ' + str(boxs[i][1]) + ' ' + str(boxs[i][2]) + ' ' + str(
                                boxs[i][3]) + ' ')
                    list_file.write('\n')

                fps = (fps + (1. / (time.time() - t1))) / 2
                print("fps= %f" % (fps))

            # 判断关闭事件是否已触发
            if True == self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.DisplayLabel.clear()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                break

            self.cap.release()
            if writeVideo_flag:
                out.release()
                list_file.close()
            cv2.destroyAllWindows()