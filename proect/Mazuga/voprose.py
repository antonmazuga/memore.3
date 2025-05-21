import random as r
import time
import turtle as t
voprosis=[]
voprosis_tape=["какой формы фигура номер один?","какой формы фигура номер два?","какой формы фигура номер три?","какой формы фигура номер четыре?","какой формы фигура номер пять?","какой формы фигура номер шесть?"]
a=''
def zadaha():
    while len(voprosis)<4:
        q = r.randint(1, len(voprosis_tape)-1)
        a = voprosis_tape[q]
        voprosis.append(a)
        voprosis_tape.pop(voprosis_tape.index(a))
    print(voprosis)
j=0
def otvet():
    def onKey1():
        a="квадрат"

    def onKey2():
        a="треуольник"

    def onKey3():
        a="круг"

    screen = t.Screen()
    screen.onkey(onKey1, "1")
    screen.listen()

    screen = t.Screen()
    screen.onkey(onKey2, "2")
    screen.listen()

    screen = t.Screen()
    screen.onkey(onKey3, "3")
    screen.listen()
i=0
if voprosis[i]=="какой формы фигура номер один?":
    print(1)

