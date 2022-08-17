# Program : record screen
# Description : This function allow you to record (only)the screen
# Date : 07/08/22
# Author : Christophe Lagaillarde
# Version : 1.0

from datetime import datetime
import PIL
from PIL import ImageGrab
import numpy
import cv2
from win32api import GetSystemMetrics
import keyboard
import pause


def record_screen(time_record_start: datetime) -> None:

    width: int = GetSystemMetrics(0)
    height: int = GetSystemMetrics(1)
    fourcc: int = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video: cv2.VideoWriter = cv2.VideoWriter('recorded_screen_of_video.mp4', fourcc, 20.0, (width, height))

    pause.until(time_record_start)
    while True:
        img: PIL.Image.Image = ImageGrab.grab(bbox=(0, 0, width, height))
        img_numpy: numpy.ndarray = numpy.array(img)
        img_final: numpy.ndarray = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2RGB)
        captured_video.write(img_final)

        if keyboard.is_pressed('q'):
            break

    return None


if __name__ == '__main__':
    record_screen()

