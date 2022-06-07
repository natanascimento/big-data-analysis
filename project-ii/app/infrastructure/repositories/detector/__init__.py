import cv2
import warnings
warnings.filterwarnings("ignore")
import numpy as np


class DrawDetector:

    @staticmethod
    def run(source_image):
        cv2.imshow("Draw Detector", source_image)

    @staticmethod
    def stop():
        cv2.destroyAllWindows()