# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# list = input()
# print(max(map(int, list.split())))
# print(min(map(int, list.split())))



# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.


# a = list(range(10))

# print("парні, які діляться на 2: ")
# for i in a:
#     if a[i]%2==0:
#         print(a[i])

# print("непарні, які діляться на 3: ")    
# for i in a:
#     if a[i]%3==0:    
#         print(a[i])

# print("числа, які не діляться на 2 та на 3: ")   
# for i in a: 
#     if a[i]%2!=0 and a[i]%3!=0:
#         print(a[i])

                    
 # 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

# num = int(input("Enter a number: "))
# factorial = 1
#
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers.")
# elif num == 0:
#    print("The factorial of the number 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of {0} is {1}".format(num,factorial))     



# 4.Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)


# login = input("Enter your login: ")

# while login == ("Iriska"):
#     print("Hello Iriska")
#     break
# else:
#     print("Login is incorrect")





# # 5.  Перший випадок. 
# Написати програму, яка буде зчитувати 
# числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).


# list = input("Введіть список чисел: ")
# for i in list.split():
#     if int(i) <= 0:
#         break
#     print(i)

   



# 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# a = int(input("Введіть кількість елементів: "))
# list = input("Введіть список чисел: ")
# if a != len(list.split()):
#     print("Не відповідає кількості eлементів.",  "Кількість введенних елементів:", a ,". Кількість елементів в списку:", len(list.split()))
# for i in list.split():
#     if int(i) <= 0:
#         break
#     print(i)




#8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)

# s = input()
# s = s.split() 
# s.sort(key=len) 
# s = " ".join(s) 
# print(s)

######

# print(" ".join(sorted(input().split(), key = len)))
# print()





#  7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
# (наприклад 10 equals 2 * 5


# def prost_sost(a):
#     d=2
#     while d <= a-1:
#         if a%d == 0:
#             break
#         else:
#             d += 1
#     if a == 1 or d == a:
#         return ('Prost')
#     else:
#         return ('Sost')
# a=int (input('Enter value: '))
# print (prost_sost(a))

