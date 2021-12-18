import math
import random

import main


# Chooses random prime from 300 bit range when prime modulo 4 equals 3
# it is more efficient to just hardcode the primes and shuffle than to calculate them
def randomPrime():
    table = [153, 185, 413, 693, 1097]
    random.shuffle(table)
    return 2 ** 300 - table[0]


# task 1 probably gut
def randomEllipticalCurve(p):
    while True:
        A = random.randint(0, p)
        B = random.randint(0, p)
        delta = (4 * (A ** 3) + 27 * (B ** 2)) % p
        if delta != 0:
            break
    return A, B, p


# task 2
def randomPointTrue(A, B, p):
    while True:
        x = random.randint(0, p)
        fx = (x ** 3 + A * x + B) % p
        if fx / p != -1:
            break
    y = math.sqrt(fx) % p
    return y


def randomPoint(x, A, B, p):
    fx = ((pow(x, 3, p) + (A * x) % p + B % p) % p) % p
    return fx


def randomPoint2(x, A, B, p):
    while True:
        fx = (x ** 3 + A * x + B) % p
        if fx / p != -1:
            break
    y = math.sqrt(fx) % p
    return y


# task 3 good
def minusP(x1: int, y1: int, p: int):
    return x1, (-y1) % p


# task 4 bad, use from test.py
def pPlusQ(x1: int, y1: int, x2: int, y2: int, p: int):
    if x1 == 0 and y1 == 0:
        return x2, y2
    elif x2 == 0 and y2 == 0:
        return x1, y1
    delta = (((y2 - y1) % p) * (main.euclidInverse((x2 - x1), p))) % p
    x3 = (pow(delta, 2, p) - x1 - x2) % p
    y3 = (delta * (x1 - x3) - y1) % p
    return x3, y3


# task 4 - good, also you can use from test.py
def pPlusP(A: int, x1: int, y1: int, p: int):
    delta = (((3 * pow(x1, 2, p)) + A) % p * (main.euclidInverse(2 * y1, p))) % p
    x3 = (pow(delta, 2, p) - 2 * x1) % p
    y3 = ((delta * (x1 - x3)) - y1) % p
    return x3, y3


if __name__ == '__main__':
    # 1
    print(randomEllipticalCurve(randomPrime()))

    # 2
    print(randomPoint2(
        175757722742565321624944121270945167081993085306911405305303187535900979958321560252348498,
        230494833619330872742071433259892253887918924949625621075110348455162899582640562756609713,
        225785530019760328737805254637561350820485164307786402015943227616074411698429350907607751,
        523133468360889049404922330981983268743289535618129665870465316487757998439707462631766351
    ))

    # 3
    print(minusP(
        175757722742565321624944121270945167081993085306911405305303187535900979958321560252348498,
        226448623369642016063981880559768023550784441813507797884241707518308435413329534175311217,
        523133468360889049404922330981983268743289535618129665870465316487757998439707462631766351
    ))

    # 4
    #print(pPlusQ(
    #    1034654950084638831746002809911248199677955393345913144822633491391559186334287517468068227,
    #    622982739772524510034071074874168058444870189141442302327788893708975989454633062691443668,
    #    257099002269265375376865050026601393088527487503240282621829201756320470848852458906673263,
    #    300276749266133746608908605837094037847002543042721682292036203072905446961574457973827418,
    #    1287992807810354321139932844968535317703403098153583526161152862239590226063279579511578187
    #))
    print(pPlusP(
        464169141979840536991867611593246600861288635535739371605755567504129182107398241113941853,
        1034654950084638831746002809911248199677955393345913144822633491391559186334287517468068227,
        622982739772524510034071074874168058444870189141442302327788893708975989454633062691443668,
        1287992807810354321139932844968535317703403098153583526161152862239590226063279579511578187
    ))
