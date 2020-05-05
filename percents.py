__author__ = "igor"


def percents(x, y):
    """what percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    # print(str(y) + " is " + str(result) + " percents of " + str(x))
    return result


def print_percents(x, y):
    """print what percents of x is y"""
    print(str(y) + " is " + str(percents(x, y)) + " percents of " + str(x))

print_percents(300,30)

