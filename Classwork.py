
#1. Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

# n = 100
# for i in range(n):
#     if i % 2 == 0:
#         print(i)

#######

# n = 100
# i = 1
# while i < n:
#     if i % 2 == 0:
#         print(i)
#     i+=1

#2.  Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).

# n = 100
# for i in range(n):
#     if i % 2 == 1:
#         print(i)  

#######

# n = 101
# i = 1
# while i < n:
#     i+=1 
#     if i % 2 == 1:
#         print(i-2)
#     else:
#         continue



#3.  Перевірити чи список містить непарні числа.
          #(Підказка: використати оператор break)

# list = [1, 9, 34, 114]
# for i in list:
#   if i % 2 == 1:
#         print("Має не парні числа")
#         break

#4.  Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
#(Підказка: використати вбудовану функцію float ()).

# list = [1, 13, 24, 100]
# idx = 0
# for i in list:
#     list[idx] = float(i)
#     idx += 1 
#     print(list.index(i), i)
# print(list)                   
# print(list[3])


######

# list = [2, 1, 4, 6, 1, 4, 8, 6]
# for i in range(len(list)):
#     list[i] = float(list[i])
# print(list)


#5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

# fib1 = 0
# fib2 = 1
# n = input ("Номер елемента Фібоначі: ")
# n = int(n)
# i = 0
# while i < n -2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1


#6.  Створити список, що складається з чотирьох елементів типу string. Потім, за допомогою циклу for, вивести елементи по черзі на екран.

# list = ["5", "34", "a", "117"]  
# for i in list:
#     print(i)
  


#7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”. 
          #(Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).


# list = ["5", "34", "a", "117"]  
# for i in list:
#     print(i + "#")


#8.  Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.

# n = int(input("Введіть ціле число: "))
# i = 1
# s = 0
# while i <= n:
#     if n % i == 0:
#         s += 1
#     i = i + 1
# if s > 2:
#     print("Число складне")    
# else:
#     print("Число просте")    



#10.  Визначити чи введене слово паліндром, тобто чи воно читається однаково зліва направо і навпаки.

# s = input()
# l = len(s)
# for i in range(l//2):
#    if s[i] != s[-1-i]:
#         print("It's not palindrome")
#         quit()
#print("It's palindrome")
