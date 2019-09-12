from tkinter import *

calc = Tk()

calc.title("Calculator")

calc.minsize(230, 300)

calc.configure(background="purple")


calc.resizable(width=False, height=False)

#global variables
bufValue = 0
bufAction = ""
isNewNumber = True 


outputScreen = Text(calc, font="Arial 20", width=20, height=1, pady=10, padx=10, background="pink")
outputScreen.grid(row=0, column=1, columnspan=4, sticky=W + E)
outputScreen.insert(1.0, bufValue)



def clickButton(num):
    global bufValue
    global bufAction
    global isNewNumber

    value = float(outputScreen.get('1.0', END))

    if isNewNumber:
        outputScreen.delete('1.0', END)

    if (num == 0 and value > 0) or num != 0:
        isNewNumber = False

    outputScreen.insert(END, num)



def action(act):
    global bufValue
    global bufAction
    global isNewNumber

    value = float(outputScreen.get('1.0', END))

    if bufAction != '':
        if bufAction == "+":
            bufValue += value
            outputScreen.delete('1.0', END)
            outputScreen.insert(1.0, str(bufValue))
        elif bufAction == "-":
            bufValue -= value
            outputScreen.delete('1.0', END)
            outputScreen.insert(1.0, str(bufValue))
        elif bufAction == "*":
            bufValue *= value
            outputScreen.delete('1.0', END)
            outputScreen.insert(1.0, str(bufValue))
        elif bufAction == ":":
            outputScreen.delete('1.0', END)

            if value == 0:
                outputScreen.insert(1.0, "Cannot divide by zero")
            else:
                bufValue /= value
                outputScreen.insert(1.0, str(bufValue))
    else:
        bufValue = float(outputScreen.get('1.0', END))

    bufAction = act
    isNewNumber = True



def clearAction():
    global bufValue
    global bufAction
    global isNewNumber

    bufValue = 0
    bufAction = ""
    isNewNumber = True

    outputScreen.delete('1.0', END)
    outputScreen.insert(1.0, str(bufValue))



def clickDot():
    global isNewNumber

    outputScreen.insert(END, '.')
    isNewNumber = False

#=

def totalAction():
    global bufValue
    global bufAction
    global isNewNumber

    if bufAction != '':
        if bufAction == "+":
            action("+")
        elif bufAction == "-":
            action("-")
        elif bufAction == "*":
            action("*")
        elif bufAction == ":":
            action(":")

    bufAction = ''
    isNewNumber = True



button1 = Button(calc, text="1", command=lambda: clickButton(1), font='arial 14', background="pink")
button1.grid(row=3, column=1, padx=(10, 0), sticky=W + E)
button2 = Button(calc, text="2", command=lambda: clickButton(2), font='arial 14', background="pink")
button2.grid(row=3, column=2, padx=(10, 0), sticky=W + E)
button3 = Button(calc, text="3", command=lambda: clickButton(3), font='arial 14', background="pink")
button3.grid(row=3, column=3, padx=(10, 0), sticky=W + E)
button4 = Button(calc, text="4", command=lambda: clickButton(4), font='arial 14', background="pink")
button4.grid(row=4, column=1, padx=(10, 0), sticky=W + E)
button5 = Button(calc, text="5", command=lambda: clickButton(5), font='arial 14', background="pink")
button5.grid(row=4, column=2, padx=(10, 0), sticky=W + E)
button6 = Button(calc, text="6", command=lambda: clickButton(6), font='arial 14', background="pink")
button6.grid(row=4, column=3, padx=(10, 0), sticky=W + E)
button7 = Button(calc, text="7", command=lambda: clickButton(7), font='arial 14', background="pink")
button7.grid(row=5, column=1, padx=(10, 0), sticky=W + E)
button8 = Button(calc, text="8", command=lambda: clickButton(8), font='arial 14', background="pink")
button8.grid(row=5, column=2, padx=(10, 0), sticky=W + E)
button9 = Button(calc, text="9", command=lambda: clickButton(9), font='arial 14', background="pink")
button9.grid(row=5, column=3, padx=(10, 0), sticky=W + E)
button0 = Button(calc, text="0", command=lambda: clickButton(0), font='arial 14', background="pink")
button0.grid(row=6, column=2, padx=(10, 0), sticky=W + E)
button0 = Button(calc, text=".", command=lambda: clickDot(), font='arial 14', background="pink")
button0.grid(row=6, column=3, padx=(10, 0), sticky=W + E)

buttonClear = Button(calc, text="C", command=lambda: clearAction(), font='arial 14', background="pink")
buttonClear.grid(row=6, column=1, padx=(10, 0), sticky=W + E)
buttonPlus = Button(calc, text="+", command=lambda: action("+"), font='arial 14', background="pink")
buttonPlus.grid(row=3, column=4, padx=(10, 0), sticky=W + E)
buttonMinus = Button(calc, text="-", command=lambda: action("-"), font='arial 14', background="pink")
buttonMinus.grid(row=4, column=4, padx=(10, 0), sticky=W + E)
buttonMultiply = Button(calc, text="*", command=lambda: action("*"), font='arial 14', background="pink")
buttonMultiply.grid(row=5, column=4, padx=(10, 0), sticky=W + E)
buttonDivision = Button(calc, text=":", command=lambda: action(":"), font='arial 14', background="pink")
buttonDivision.grid(row=6, column=4, padx=(10, 0), sticky=W + E)
buttonTotal = Button(calc, text="=", command=lambda: totalAction(), font='arial 14', background="pink")
buttonTotal.grid(row=7, column=4, padx=(10, 0), sticky=W + E)

calc.mainloop()