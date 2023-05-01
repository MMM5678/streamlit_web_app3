import cv2
import os
import streamlit as st
import numpy as np
from PIL import Image


def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while n < 2:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)

    # 表示
    file_name = '{}_{}.{}'.format(base_path, n, ext)
    img = cv2.imread(file_name)

    st.header("Photo Display")
    st.image(file_name, width=400 )

save_frame_camera_key(0, 'data', 'camera_capture')
