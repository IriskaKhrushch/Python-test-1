1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 

def func(nums):
    return sum(map(int, nums.split()))/len(nums.split())
print(func(input("Введіть число: ")))


2.  Написати функцію, яка повертає абсолютне значення числа

def func(x):    
    print(abs(x))   
func(int(input("Введіть число: ")))

3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.   


def arithmetic_mean(*args):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """
    return  max(args)
 
print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))
print(arithmetic_mean.__doc__)




4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола 
(написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)


figure = input("Виберіть фігуру(1 - прямокутника, 2 - трикутник, 3 - коло): ")
if figure == '1':
    print("Довжина сторін прямокутника: ")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Площа: %2f" % (a*b))
elif figure == '2':
    print("Довжина сторін трикутника: ")   
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a+b+c) / 2
    import math
    s = math.sqrt(p* (p - a)) * (p - b) * (p - c)
    print("Площа: %.2f" %s)
elif figure == '3':
    r = float(input("Радіус круга R = ")) 
    import math
    print("Площа: %2f" % (math.pi*r**2))
else:
    print("Помилка вводу данних")

5.  Написати функцію, яка обчислює суму цифр введеного числа

def func(nums):
    sum=0
    for i in nums:
        sum+=int(i)
    return sum
print(func(input("Введіть число: ")))


6.  Написати програму калькулятор, яка складається з наступних функцій: 

головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти, 
поки ми не виберемо дію вийти з калькулятора, після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def my_calc(action, val1, val2):
    if action == "+":
        print(val1+val2)
    elif action == "-":
        print(val1-val2)
    elif action == "*":
        print(val1*val2) 
    elif action == "/":
        print(val1/val2) 
    else:
        print("Не вірна дія")     
a = input("Дія: ")
b = float(input("val1: "))
c = float(input("val2: "))
my_calc(a, b, c)


8.  Написати програму, яка обчислює дискримінант квадратного рівняння

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b**2-4*a*c
print(d)
