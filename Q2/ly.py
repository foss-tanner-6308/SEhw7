def lpy_1(i):
    if i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
        return "{} is a leap year".format(i)


def lpy_2(i):
    if i % 100 == 0 and i % 400 != 0:
        return "{} is not a leap year".format(i)
