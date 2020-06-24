import time
import pyautogui
from mss import mss

initial_X = 650
initial_Y = 650

area = (initial_X, initial_Y, initial_X+538, initial_Y+3)

gaps_x = [0,150,300,450]

def playThePiano():
    with mss() as sct:
        while True:

            img = sct.grab(area)
            for gap in gaps_x:
                if img.pixel(gap , 0)[0] < 100:
                    pyautogui.click(initial_X + gap, initial_Y)
                    break

time.sleep(3)
playThePiano()
