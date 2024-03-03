#!/usr/bin/python3

a = 10
b = 5

if __name__ == "__main__":
    import calculator_1 as calc
    x = calc.add(a, b)
    y = calc.sub(a, b)
    z = calc.mul(a, b)
    w = calc.div(a, b)
    print("{} + {} = {}".format(a, b, x))
    print("{} - {} = {}".format(a, b, y))
    print("{} * {} = {}".format(a, b, z))
    print("{} / {} = {}".format(a, b, w))
