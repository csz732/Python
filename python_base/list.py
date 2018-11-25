# -*- coding: UTF-8 -*-
import time
listnum = (1, 2, 3)
liststr = ["csz", "cmf", "zyp", "cyz"]
word = "help" + "A"
print("Hello, World!")
print(u"你好")
print('word ' + word[0])
liststr[1] = "123"

print("liststr : " + liststr[1])
print("liststr : " + liststr[2])
print("listnum: ", listnum[1])

tick = time.time()
print("current time ", tick)


def pintfarg(arg1, *table):
    "___-______________"
    print("output")
    print(arg1)
    for vars in table:
        print(vars)

    return


pintfarg(1)
pintfarg(10, 20, 30)


class point:
    def __init__(self):
        print("init ")

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name)


pt1 = point()
pt2 = pt1
del pt1
