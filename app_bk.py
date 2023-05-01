import cv2
import pandas as pd
#import os
import streamlit as st
import numpy as np
from PIL import Image

#print(cv2.__version__)
#print(pd.__version__)
#print(os.__version__)
#print(st.__version__)
#print(np.__version__)
#print(Image.__version__)


def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    #os.makedirs(dir_path, exist_ok=True)
    #base_path = os.path.join(dir_path, basename)
    basename = "./data/camera_capture.jpg"

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imwrite(basename)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)

    # 表示
    #file_name = '{}_{}.{}'.format(base_path, n, ext)
    img = cv2.imread(basename)

    st.header("Photo Display")
    st.image(basename, width=400 )

save_frame_camera_key(0, 'data', 'camera_capture')

