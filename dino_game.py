import pyautogui  # pip install pyautogui
from PIL import ImageGrab  # pip install pillow

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
    # for birds
    """for x in range(100, 220):
        for y in range(400, 420):
            if data[x, y] > 100:
                hit("down")
                return"""
    return


def dayCollide(data):
    print("day")
    # for cactus
    for x in range(250, 400):
        for y in range(570, 650):
            if data[x, y] < 100:
                hit("up")
                return
    # for birds
    """for x in range(100, 220):
        for y in range(400, 420):
            if data[x, y] < 100:
                hit("down")
                return"""
    return


if __name__ == "__main__":
    time.sleep(2)
    # hit('up')
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
        # Draw the rectangle for birds
        for i in range(100, 220):
            for j in range(400, 420):
                data[i, j] = 171
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

