def lpy_1(i):
    if i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
        return "{} is a leap year".format(i)
