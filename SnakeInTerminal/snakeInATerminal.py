import random

global SNAKE, APPLE, SCORE
global GROUND, SIZE

global KEYS, ACTIVEKEY, DIRECTION

SNAKE = [(4, 3), (4, 4)]
DIRECTION = 4
ACTIVEKEY = 4
KEYS = ["q", "w", "a", "s", "d"]
APPLE = (1, 3)
SIZE = (8, 8)
GROUND = []
SCORE = 0

# Ground Decleration
# 0 = None
# 1 = Apple
# 2 = Body
# 3 = Head
# Keys Decleration
# q = 0
# w = 1
# a = 2
# s = 3
# d = 4

def __updateGround():
    global GROUND, SIZE, APPLE
    GROUND = []
    for heigth in range(SIZE[0]):
        GROUND.append([])
        for width in range(SIZE[1]):
            GROUND[heigth].append(0)
    __updateApple()
    __updateSnake()


def __updateApple():
    GROUND[APPLE[0]][APPLE[1]] = 1


def __updateSnake():
    for i, part in enumerate(SNAKE):
        GROUND[part[0]][part[1]] = 2
        if i == len(SNAKE) - 1:
            GROUND[part[0]][part[1]] = 3


def __printGround():
    SYMBOLS = {
        0: " ",
        1: "A",
        2: "O"
    }
    HEADSYMBOLS = {
        1: "^",
        2: "<",
        3: "v",
        4: ">"
    }
    print("\b\b\b\b")
    for width in range(SIZE[1] - 1):
        print("\t_", end="")
    print()
    for heigth in range(SIZE[0]):
        print("|", end="")
        for width in range(SIZE[1]):
            if GROUND[heigth][width] == 3:
                print(HEADSYMBOLS[DIRECTION], "\t", end="")
            else:
                print(SYMBOLS[GROUND[heigth][width]], "\t", end="")
        print("|")
    for width in range(SIZE[1] - 1):
        print("\t_", end="")
    print()
    print(f"SCORE: {SCORE}")


def __handleMovement():
    global ACTIVEKEY, SNAKE, DIRECTION, SCORE
    DIRECTION = ACTIVEKEY
    lastPosition = SNAKE[0]
    if __isColliding():
        ACTIVEKEY = 0
    else:
        if DIRECTION == 1:
            for i, part in enumerate(SNAKE):
                if i == len(SNAKE) - 1:
                    SNAKE[i] = (part[0] - 1, part[1])
                else:
                    SNAKE[i] = SNAKE[i + 1]
        elif DIRECTION == 2:
            for i, part in enumerate(SNAKE):
                if i == len(SNAKE) - 1:
                    SNAKE[i] = (part[0], part[1] - 1)
                else:
                    SNAKE[i] = SNAKE[i + 1]
        elif DIRECTION == 3:
            for i, part in enumerate(SNAKE):
                if i == len(SNAKE) - 1:
                    SNAKE[i] = (part[0] + 1, part[1])
                else:
                    SNAKE[i] = SNAKE[i + 1]
        elif DIRECTION == 4:
            for i, part in enumerate(SNAKE):
                if i == len(SNAKE) - 1:
                    SNAKE[i] = (part[0], part[1] + 1)
                else:
                    SNAKE[i] = SNAKE[i + 1]
        if __isOnApple():
            SNAKE.insert(0, lastPosition)
        __updateGround()
        SCORE += 1


def __isColliding():
    head = SNAKE[len(SNAKE) - 1]
    if DIRECTION == 1 and head[0] == 0:
        return True
    elif DIRECTION == 2 and head[1] == 0:
        return True
    elif DIRECTION == 3 and head[0] == SIZE[0] - 1:
        return True
    elif DIRECTION == 4 and head[1] == SIZE[1] - 1:
        return True
    return False


def __isOnApple():
    global APPLE, SNAKE, SCORE
    if APPLE == SNAKE[len(SNAKE) - 1]:
        __newApple()
        SCORE += 10
        return True
    return False


def __newApple():
    global APPLE, SIZE
    size = (random.randrange(0, SIZE[0]), random.randrange(0, SIZE[1]))
    if SNAKE.count(size) > 0:
        __newApple()
    APPLE = size
    __updateApple()


def main():
    global ACTIVEKEY
    if ACTIVEKEY == 0:
        return 0
    __printGround()
    print("Keyinput [W, A, S, D, Q]:\t", end="")
    keyInput = input().lower()
    if KEYS.count(keyInput) > 0:
        ACTIVEKEY = KEYS.index(keyInput)
    if ACTIVEKEY == 0:
        return 0
    elif 1 <= ACTIVEKEY <= 4:
        __handleMovement()

    main()


def __new__():
    __updateGround()
    main()


__new__()
