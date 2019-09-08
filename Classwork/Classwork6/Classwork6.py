def choise():
    """Перевірка числа на парність"""
    print('Привіт! Введи ціле число:')
    try:
        number = int(input())
    except ValueError:
        print('Схоже Ви ввели не цифру...')
    else:
        if number % 2 == 0:
            print(f'Число {number} - парне!')
        else:
            print(f'Число {number} - не парне!')

choise()


def age():
    """Перевірка віку на парність"""
    print('Привіт! Введи свій вік:')
    try:
        age = int(input())
        if age < 0:
            raise Exception
    except ValueError:
        print('Схоже Ви ввели не цифру...')
    except Exception:
        print("Вік не може бути від'ємним")
    else:
        if age % 2 == 0:
            print(f'Вік парний!')
        else:
            print(f'Вік не парний!')

age()


def ages(age):
    """Перевірка віку на парність(інший спосіб)"""
    if age % 2 == 0:
        print(f'Вік парний!')
    else:
        print(f'Вік не парний!')

print('Привіт! Введи свій вік:')
try:
    age = int(input())
    if age < 0:
        raise Exception
except ValueError:
    print('Схоже Ви ввели не цифру...')
except Exception:
    print("Вік не може бути від'ємним")
else:
    ages(age)


def chastka():
    """Частка двох чисел"""
    print('Введіть два числа через кому (приклад: "x,y")')
    string = str(input())
    try:
        fst = int(string.split(',')[0])
        scnd = int(string.split(',')[1])
        chs = fst / scnd
    except ValueError:
        print('Схоже, Ви ввели не числа...')
    except ZeroDivisionError:
        print('Ділення на нуль!')
    except Exception:
        print("Ой, щось пішло не так...")
    else:
        print(f'Частка чисел {fst} та {scnd} = {chs}')
    finally:
        print('Вихід з програми.')

chastka()


# class CustomError(Exception):
#     def __init__(self, data):
#         self.data = data

#     def __str__(self):
#         return repr(self.data)


def days():
    """Дні тижня"""
    days = {"1": "Понеділок", "2": "Вівторок", "3": "Середа", "4": "Четвер", "5": "П'ятниця", "6": "Субота", "7": "Неділя"}
    try:
        numb = int(input("Введіть число, яке відповідає дню тижня:\n"))
        # if numb > 7:
        #     raise CustomError('Є лише 7 днів тижня')
        # elif numb <= 0:
        #     raise CustomError('Число не може бути від\'ємним')
    except ValueError:
        print('Ви ввели не ціле число')
    except Exception as e:
        print(e)
    else:
        print(f'{numb} день тижня - це {days.get(str(numb), "Немає такого дня тижня...")}')

days()