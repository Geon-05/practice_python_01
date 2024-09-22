from copy import copy
import math


def print_hello():
    print("hello")


def hypotenuse(num1, num2):
    res1 = (num1**2 + num2**2) ** 0.5
    print(res1)

    res2 = math.sqrt(num1**2 + num2**2)
    print(res2)


def fileSize(r, t):
    size = r * t / 1000
    print(size)


def test01():
    a = [1, 2, 3]

    b = copy(a)
    print(b is a)
    print(a)
    print(b)

    print("-" * 50)

    b = a.copy()
    print(b is a)
    print(a)
    print(b)


def write_data():
    file = open("practice_py/text/new.txt", "w")

    for i in range(1, 11):
        data = f"{i}번째 줄입니다.\n"
        file.write(data)

    file.close()


def read_data():
    file = open("practice_py/text/new.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        print(line, end="")
    file.close()

    print("-" * 50)

    file = open("practice_py/text/new.txt", "r")
    for line in file:
        print(line, end="")
    file.close()

    print("-" * 50)

def add_data() :
    file = open("practice_py/text/new.txt", "a")
    for i in range(11,20) :
        data = f"{i}번째 줄입니다.\n"
        file.write(data)
    file.close()

def autoClose_data() :
    with open("practice_py/text/new2.txt", "w") as file :
        file.write("new file setting")