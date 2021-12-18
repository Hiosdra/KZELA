from main import euclidInverse


def sumPoint(a, b, p, x1, y1, x2, y2):
    if x1 == "e" and y1 == "e":
        return x2, y2
    elif x2 == "e" and y2 == "e":
        return x1, y1

    if x1 != x2:
        delta = (((y2 - y1) % p) * euclidInverse((x2 - x1), p)) % p
        x3 = (pow(delta, 2, p) - (x1 % p) - (x2 % p)) % p
        y3 = (delta * (x1 - x3) - y1) % p
        return x3, y3

    if (x1 == x2) and (y1 == -y2):
        return "e", "e"

    if (x1 == x2) and (y1 == y2):
        delta = (((3 * pow(x1, 2, p) % p + a) % p) * euclidInverse(2 * y1, p)) % p
        x3 = (pow(delta, 2, p) - (x1 % p) - (x2 % p)) % p
        y3 = (delta * (x1 - x3) - y1) % p
        return x3, y3

    if (x1 == x2) and (y1 == y2 % p):
        return "e", "e"
