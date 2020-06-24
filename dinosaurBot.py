from PIL import ImageGrab , ImageOps
import time
import pyautogui
from numpy import *

class XYposition():
    replay = (451,566)
    dinosaur = (217, 576)

    #for x cordinate 320
    #for y cordinate 592

def restart():
    pyautogui.click(XYposition.replay)

def doJump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Yooo...!")
    pyautogui.keyUp('space')

def imageGrab():
    area = (XYposition.dinosaur[0]+103, XYposition.dinosaur[1], XYposition.dinosaur[0]+143, XYposition.dinosaur[1]+30 )
    image = ImageGrab.grab(area)
    grayImage = ImageOps.grayscale(image)
    summation = array(grayImage.getcolors())
    #print(summation.sum())
    print("Running...")
    return summation.sum()

def playTheGame():
    restart()
    while True:
        if (imageGrab() != 1447):
            doJump()
            time.sleep(0.1)

playTheGame()
