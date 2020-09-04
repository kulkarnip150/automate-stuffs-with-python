#https://play2048.co/
import pyautogui, time
from PIL import Image, ImageGrab, ImageOps

# global
currentgrid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
scoregrid = [50, 25, 12, 6, 25, 0, 0, 0, 12, 0, 0, 0, 6, 0, 0, -1]
# global


class Getcords:
    cord00 = (250, 380)  # 00
    cord01 = (370, 380)
    cord02 = (490, 380)
    cord03 = (610, 380)  # 03

    cord10 = (250, 505)  # 10
    cord11 = (370, 505)
    cord12 = (490, 505)
    cord13 = (610, 505)  # 13

    cord20 = (250, 630)  # 20
    cord21 = (370, 630)
    cord22 = (490, 630)
    cord23 = (610, 630)  # 23

    cord30 = (250, 750)  # 30
    cord31 = (370, 750)
    cord32 = (490, 750)
    cord33 = (610, 750)  # 33

    cordarray = [
        cord00,
        cord01,
        cord02,
        cord03,
        cord10,
        cord11,
        cord12,
        cord13,
        cord20,
        cord21,
        cord22,
        cord23,
        cord30,
        cord31,
        cord32,
        cord33,
    ]


class Allvalues:
    empty = 195  # 0
    two = 230  # 1
    four = 225  # 2
    eight = 190
    sixteen = 172
    thirtyTwo = 157
    sixtyFour = 135
    oneTwentyEight = 205
    twoFiftySix = 202
    fiveOneTwo = 197
    oneZeroTwoFour = 193
    twoZeroFourEight = 189  # 11

    valueArray = [
        empty,
        two,
        four,
        eight,
        sixteen,
        thirtyTwo,
        sixtyFour,
        oneTwentyEight,
        twoFiftySix,
        fiveOneTwo,
        oneZeroTwoFour,
        twoZeroFourEight,
    ]


def getgrid():
    while True:
        image = ImageGrab.grab()  # grab current screen
        grayImage = ImageOps.grayscale(image)  # BnW for more performance
        for index, i in enumerate(
            Getcords.cordarray
        ):  # index will hold index of array of cord & i for traking forloop
            pixel = grayImage.getpixel(i)  # get data of pixels with using i
            posi = Allvalues.valueArray.index(pixel)  # get index of matching pixel
            if posi == 0:  # n is 0,1,2,3...11
                currentgrid[index] = 0  # 2^n = 1,2,4,8,16... to get 0
            else:
                currentgrid[index] = pow(2, posi)  # to get power of n base 2
        # grayImage.show()
        break
    return currentgrid


def printgrid(grid):
    for i in range(0, 16):
        if i % 4 == 0:  # formating
            print(
                grid[i], grid[i + 1], grid[i + 2], grid[i + 3],
            )


def swipeRow(row):
    prev = -1
    i = 0
    temp = [0, 0, 0, 0]
    for element in row:
        if element != 0:  # to avoid 0
            if prev == -1:  # if element is new
                prev = element
                temp[i] = element
                i += 1
            elif prev == element:  # if element is same as previous
                temp[i - 1] = 2 * prev
                prev = -1
            else:  # if element is diffrent
                prev = element
                temp[i] = element
                i += 1
    return temp


def getNextGrid(grid, move):
    temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if move == UP:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + 4 * j])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[i + 4 * j] = val

    elif move == LEFT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4 * i + j])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[4 * i + j] = val

    elif move == DOWN:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + 4 * (3 - j)])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[i + 4 * (3 - j)] = val

    elif move == RIGHT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4 * i + (3 - j)])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[4 * i + (3 - j)] = val

    return temp


def guessmove(grid):
    scoreUP = getscore((getNextGrid(getNextGrid(currentgrid, UP), UP)))
    scoreDOWN = getscore((getNextGrid(getNextGrid(currentgrid, DOWN), DOWN)))
    scoreLEFT = getscore((getNextGrid(getNextGrid(currentgrid, LEFT), LEFT)))
    scoreRIGHT = getscore((getNextGrid(getNextGrid(currentgrid, RIGHT), RIGHT)))
    maxscore = max(scoreUP, scoreDOWN, scoreLEFT, scoreRIGHT)
    if not ismovevalid(grid, UP):
        scoreUP = 0
    if not ismovevalid(grid, DOWN):
        scoreDOWN = 0
    if not ismovevalid(grid, LEFT):
        scoreLEFT = 0
    if not ismovevalid(grid, RIGHT):
        scoreRIGHT = 0

    if maxscore == scoreUP:
        makemovement("up")
    elif maxscore == scoreDOWN:
        makemovement("down")
    elif maxscore == scoreLEFT:
        makemovement("left")
    else:
        makemovement("right")


def makemovement(key):
    pyautogui.press(key)
    print(key)


def ismovevalid(grid, move):
    if getNextGrid(grid, move) == grid:
        return False
    else:
        return True


def getscore(grid):
    score = 0
    for i in range(4):
        for j in range(4):
            score += grid[4 * i + j] * scoregrid[4 * i + j]
    return score


def main():
    for i in range(3):
        print(i + 1)
        time.sleep(1)
    while True:
        getgrid()
        guessmove(currentgrid)
        time.sleep(0.5)



main()
