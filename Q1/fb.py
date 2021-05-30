def fb_3_5(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        return "FizzBuzz"


def fb_3(i):
    if i % 3 == 0:
        print("Fizz")
        return "Fizz"


def fb_5(i):
    if i % 5 == 0:
        print("Buzz")
        return "Buzz"


def fb(func1, func2, func3):
    for i in range(1, 100):
        if i % 3 != 0 and i % 5 != 0:
            print(i)
        func1(i)
        func2(i)
        func3(i)


fb(fb_3_5, fb_3, fb_5)
