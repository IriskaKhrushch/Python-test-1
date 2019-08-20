1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())


import random
ans=random.randint(1, 100)
user_input=0
while user_input!=ans:
    user_input=int(input("Guess number from 1 to 100:"))
    if user_input>ans:
        print("Try smaller number")
    elif user_input<ans:
        print("Try larger number")
print("YOU WIN!")



2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
import math

a = int(input("ВВедіть сторону а: "))
b = int(input("ВВедіть сторону б: "))
rectangle_area = a*b
print(rectangle_area)

a = int(input("ВВедіть сторону а: "))
h = int(input("ВВедіть висоту h: "))
triangle_area = 0.5*h*a
print(triangle_area)

r = int(input("ВВедіть радіус кола: "))

circle_area=math.pi *math.pow(r, 2)
print(circle_area)




3 PyOWM Weather API
import pyowm
owm = pyowm.OWM('38af86c6bc90dca541eec2efc84fbd66')
observation = owm.weather_at_place('Lviv')
w=observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
wind=w.get_wind()
humidity=w.get_humidity()




print(w)
print("In Lviv city is now the temperature of the air "+"" +str(temperature)+ " for the Celsius. The wind: "+str(wind)+". The humidity humidity is: " + str(humidity))