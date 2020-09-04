import pyautogui
from PIL import ImageGrab

# import numpy
import time


def hit(key):
    pyautogui.press(key)
    return


def nightCollide(data):
    print("night")
    # for cactus
    for x in range(250, 400):
        for y in range(570, 650):
            if data[x, y] > 100:
                hit("up")
                return
    return


def dayCollide(data):
    print("day")
    # for cactus
    for x in range(250, 400):
        for y in range(570, 650):
            if data[x, y] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        for i in range(60, 61):
            for j in range(150, 151):
                if data[i, j] > 100:
                    dayCollide(data)
                else:
                    nightCollide(data)

        """
        # print(asarray(image))
        # Draw the rectangle for cactus
        for i in range(250, 400):
            for j in range(570, 650):
                data[i, j] = 100
        #Draw the rectangle for time
        for i in range(60,61):
            for j in range(150,151):
                data[i, j] = 120
        image.show()
        break"""



