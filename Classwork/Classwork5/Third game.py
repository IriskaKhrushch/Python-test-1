1

# tkinter бібліотека для розробки графічного інтерфейсу

from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна

root.title("Сaught the BALL")

#створ. об'єкт класу canvas

canv = Canvas(root,bg='white')

#pack пакувальник, який дозволяє розміщати 
#зображення одне за одним
#fill=BOTH дозволяє заповнювати все доступне місце і по ширині і по висоті
# expand=1 при розширенні вікна мітка завжди буде посередині 

canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
###################################################
def new_ball():
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    
    #(x-r,y-r)-координати верхнього лівого кута
    #(x+r,y+r)- координати нижнього правого кута
    #квадрата, в якому промальовується коло

    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    
    #root.after(1000,new_ball) 
    # через 1000 мілісек викон.
    # функцію  new_ball()
    
    root.after(1000,new_ball)
#######################################################     

new_ball()
mainloop()

2

from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сaught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
######################################################
def new_ball():
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
######################################################### 

 #додали обробку події click
 #     

def click(event):
    print('click the button')   
     
#############################################

new_ball()

#canv.bind зв'язує між собою декілька подій

canv.bind('<Button-1>', click)
mainloop()


3
from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сaught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
#використання global не найкраща ідея
#краще використовувати ООП
#global означає, що змінні будуть 
#вважатися глобальними, і їх 
# значення збережеться і після 
# завершення роботи функції, а не буде
# знищене як це станеться з усіма локальними 
# змінними після завершення виконання функції

#################################################3
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
#######################################################
     
 #щоб визначити, чи попали ми в круг,
 # необхідно знати його координати, 
 # радіус круга і координати мишки в момент кліку.
 # Координати мишки легко отримати через 
 # event.x, event.y.    
def click(event):
    print(x,y,r)    
     


new_ball()
canv.bind('<Button-1>', click)
mainloop()

4

from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сaught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
############################################################
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    #canv.create_text(20,20,text=str(points), font = 'Arial 20')
    
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
###################################################################

 # функція, яка провіряє, чи не лежить 
 # точка event.x,event.y дальше, ніж r 
 # від точки x,y. Для цього, з допомогою
 # теореми Піфагора ми знаходимо
 # відстань між двома точками і порівнюємо 
 # з радіусом круга.
 #  
 # якщо відстань(гіпотенуза) більша за радіус 
 # круга, то клік відбувся зовні круга
 #  
 # якщо відстань(гіпотенуза) менша за радіус 
 # круга, то клік відбувся всередині круга    
     
def click(event):
    global points
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1 #змінна підрахунку кількості співпадінь (вгадувань)
 
points = 0
new_ball()
canv.bind('<Button-1>', click)
 
mainloop()

5
from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сaught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    #виводити рахунок в консоль незручно
    #зручніше його вивести на canvas
    #використавши функцію canv.create_text()
    canv.create_text(60,20,text="Score: "+str(points), font = 'Arial 20')
    
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
     
     
def click(event):
    global points
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
 
points = 0
new_ball()
canv.bind('<Button-1>', click)
 
mainloop()

6
from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сaught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r,ball
    canv.delete(ball)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)

     
     
def click(event):
    global points, x, text
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        x = -1000
#видалення круга при кліку
        canv.delete(text)
        canv.delete(ball)
        text = canv.create_text(60,20,text="Score: " + str(points), font = 'Arial 20')
 


        

#щоб не можна було «накручувати» очки, 
# клікаючи багато разів по кругу, 
# поки він не зникне

#Після кліку круг не зникає і це не ok.
#Можна видалити все 
# canv.delete(ALL), 
# але тоді буде видалятись і рахунок

#краще дати імена всім графічним примітивам
# (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
#щоб можна було видалити ball, треба перед викликом 
#функції ball() намалювати цей ball
ball = canv.create_oval(-100,0,0,0)
text = canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
points = 0
new_ball()
canv.bind('<Button-1>', click)


mainloop()

7
from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сaught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r,ball
    canv.delete(ball)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)

     
     
def click(event):
    global points, x, text
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        x = -1000
#видалення круга при кліку
        canv.delete(text)
        canv.delete(ball)
        text = canv.create_text(60,20,text="Score: " + str(points), font = 'Arial 20')
 


        

#щоб не можна було «накручувати» очки, 
# клікаючи багато разів по кругу, 
# поки він не зникне

#Після кліку круг не зникає і це не ok.
#Можна видалити все 
# canv.delete(ALL), 
# але тоді буде видалятись і рахунок

#краще дати імена всім графічним примітивам
# (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
#щоб можна було видалити ball, треба перед викликом 
#функції ball() намалювати цей ball
ball = canv.create_oval(-100,0,0,0)
text = canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
points = 0
new_ball()
canv.bind('<Button-1>', click)


mainloop()







  