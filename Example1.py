
from math import e
from re import I
import sys 
import collections
import random

# 2 semester

# example 3 Ввод-вывод и базовые переменные
# task 1

a=str(input("Please enter type of enimal "))
b=str(input("Please enter its age "))
c=str(input("Please enter its nickname "))
print("Its a " + a + " Its nickname is " + c + " And its age is " + b)

#task 2

d=str(input("Enter first stage "))
e=str(input("Enter second stage "))
f=str(input("Enter third stage "))
g=str(input("Enter fourth stage "))
h=str(input("Enter fifth stage "))
i=str(input("Enter sixth stage "))
j=str(input("Enter seventh stage "))
print(d,e,f,g,h,i,j, sep='=>')


#example 4 Float, int и арифметические операции
#task 1

a = float(input('Please enter first side of rectangle: '))
b = float(input('Please enter second side of rectangle: '))
print('Perimeter is ')
print((a + b)*2)
print('area is ')
print(a * b)

#task 2 

a = int(input('Please enter 5 digit number(its first digit) '))
b = int(input('Please enter 5 digit number(its second digit) '))
c = int(input('Please enter 5 digit number(its third digit) '))
d = int(input('Please enter 5 digit number(its fourth digit) '))
e = int(input('Please enter 5 digit number(its fifth digit) '))
f = ((d**e)*c)/(a-b)
print(f)



#example 5 Логические и условные операторы
#task 1

a = int(input())
if a % 2 == 0:
   if a * (-1) > 0:
       print('chetnoe otric')
   elif a * (-1) < 0:
       print('chetnoe polozh')
else:
   print('nechet')

#task 2

s = str(input("VVEDITE STROKU: "))
count = 0
count1 = 0
vowels = set("aeiouy")
no_vowels = set('bcdfghjklmnpqrstvwxzy')
for letter in s:
   if letter in vowels:
       count += 1
   if letter in no_vowels:
       count1 += 1
print("GLASNIH: ")
print(count)
print("SOGLASNIH: ")
print(count1)

#task 3

sum1 = int(input())
mike = int(input())
ivan = int(input())
if mike >= sum1 and ivan >= sum1:
   print('2')
elif mike >= sum1 and ivan < sum1:
   print('mike')
elif mike < sum1 and ivan >= sum1:
   print('ivan')
elif (mike < sum1) and (ivan < sum1) and ((ivan + mike) > sum1):
   print('1')
else:
   print('0')



#example 6 Циклы While и For
#task 1 

num_zeroes = 0
for i in range(int(input())):
   if int(input()) == 0:
       num_zeroes += 1
print(num_zeroes)

#task 2

amount = 0
n = int(input())
f = 0
for i in range(n):
   f += 1
   if n%f == 0:
       amount += 1
print(amount + 1)

#task 3

a = int(input())
b = int(input())
f = a
if a > b:
   print('enter a <= b')
   exit()
for i in range(a,b+1):
   f += 1
   if f%2 == 0:
       print(f, end=' ')
print()



#example 7 Строки
#task 1 

def palindrome_check(s):
   reverse = ''.join(reversed(s))
   if s == reverse:
       return "Строка является палиндромом"
   return "Строка не является палиндромом"
s = input("Введите строку: ")
print(palindrome_check(s))

#task 2

a = input()
while "  " in a:
   a= a.replace("  ", " ")
print(a)



#example 8 Списки
#task 1

n = int(input("Please enter desired amount of numbers "))
a = []
for i in range(n):
   b = int(input())
   a.append(b)
a.reverse()
print(a)

#task 2

n = int(input('Please enter a number between 1 and 100000: '))
if n > 100000 or n < 1:
   print('Please enter a valid number between 1 and 100000')
   exit()
a = list(map(int, input('Please enter the array of {} numbers: '.format(n)).split()))
last_element = a[-1]
a[1:] = a[:-1]
a[0] = last_element
print(*a)

#task 3

n = int(input('Введите количество рыбаков: '))
m = int(input('Введите максимальную массу: '))
weights = [int(input(f'Масса рыбака {i + 1}: ')) for i in range(n)]
weights.sort()
boats = 0
left = 0
right = n - 1

while left <= right:
   if weights[left] + weights[right] <= m:
       left += 1
   right -= 1
   boats += 1

print(f'Количество необходимых лодок: {boats}')



#example 9 Множества
#task 1 

n = int(input())
b = set()
for i in range(n):
   a = int(input().split())
   b.add(a)
print(len(b))

#task 2

n = int(input())
a = set()
b = set()
for i in range(n):
    c = int(input())
    a.add(c)
m = int(input())
for j in range(m):
    d = int(input())
    b.add(d)
print(a.intersection(b))

#task 3

n = int(input('Enter amount of elements '))
a = set()
for i in range(n):
    b = int(input())
    if b in a:
        print('YES')
    else:
        print('NO')
    a.add(b)



#example 10 Словари
#task 1

pets = {}
pet_name = input("Введите имя питомца: ")
pet_kind = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")
if pet_age % 10 == 1 and pet_age != 11:
    age_string = f"{pet_age} год"
elif pet_age % 10 in [2, 3, 4] and pet_age not in [12, 13, 14]:
    age_string = f"{pet_age} года"
else:
    age_string = f"{pet_age} лет"
pet_info = {
    "Вид питомца": pet_kind,
    "Возраст питомца": age_string,
    "Имя владельца": owner_name
}
pets[pet_name] = pet_info
print(f"\nИмя: {pet_name}")
print(f"Вид: {pet_kind}")
print(f"Возраст: {age_string}")
print(f"Имя владельца: {owner_name}")
print("\nРезультирующий словарь:")
print(pets)

#task 2 

n = int(input('Please enter a begin dot '))
m = int(input('Please enter a finish dot '))
dict = {}
while n >= m:
    n -= 1
    f = n**n
    dict[n] = f
print(dict)



#example 11 Функции
#task 1

def func(a):
    b = 1
    c = []
    for i in range(1,a+1):
        b *= i
        c.append(b)
    c.reverse()
    return(b,c)

a = int(input())
print(func(a))

#task 2

Словарь с питомцами
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
    и так далее
}

def create():
    last = collections.deque(pets, maxlen=1)[0]  # Получаем последний ключ
    new_id = last + 1  # Увеличиваем на единицу
    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    Создаем новую запись
    pets[new_id] = {name: {"Вид питомца": pet_type, "Возраст питомца": age, "Имя владельца": owner_name}}

def read(ID):
    pet_info = get_pet(ID)
    if pet_info:
        pet_name, details = list(pet_info.items())[0]
        print(f'Это {details["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {details["Возраст питомца"]} '
              f'{get_suffix(details["Возраст питомца"])}. Имя владельца: {details["Имя владельца"]}')
    else:
        print("Питомец с таким ID не найден.")

def update(ID):
    pet_info = pet_name, details = list(pet_info.items())[0]
    print(f'Текущая информация о питомце:')
    print(f'Имя: {pet_name}, Вид питомца: {details["Вид питомца"]}, Возраст: {details["Возраст питомца"]}, Владелец: {details["Имя владельца"]}')
    new_name = input("Введите новое имя питомца (если не хотите менять, нажмите Enter): ")
    new_pet_type = input("Введите новый вид питомца (если не хотите менять, нажмите Enter): ")
    new_age = input("Введите новый возраст питомца (если не хотите менять, нажмите Enter): ")
    new_owner_name = input("Введите новое имя владельца (если не хотите менять, нажмите Enter): ")

        Обновляем информацию
    if new_name:
            details["Вид питомца"] = new_name
    if new_pet_type:
            details["Вид питомца"] = new_pet_type
    if new_age:
            details["Возраст питомца"] = int(new_age)
    if new_owner_name:
            details["Имя владельца"] = new_owner_name

    print(f'Информация о питомце обновлена.')

def delete(ID):
    if ID in pets:
        del pets[ID]
        print(f'Запись о питомце с ID {ID} удалена.')
    else:
        print("Питомец с таким ID не найден.")

def get_pet(ID):
    return pets.get(ID)

def get_suffix(age):
    if age % 10 == 1 and age != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):
        return 'года'
    else:
        return 'лет'

def pets_list():
    for pet_id, pet_info in pets.items():
        pet_name, details = list(pet_info.items())[0]
        print(f'ID: {pet_id}, Имя: {pet_name}, Вид питомца: {details["Вид питомца"]}, Возраст: {details["Возраст питомца"]}, Владелец: {details["Имя владельца"]}')


Пример использования:

command = ''
while command != 'stop':
    command = input('Введите команду (create, read, update, delete, stop): ')
    
    if command == 'create':
        create()
    elif command == 'read':
        ID = int(input('Введите ID питомца: '))
        read(ID)
    elif command == 'update':
        ID = int(input('Введите ID питомца: '))
        update(ID)
    elif command == 'delete':
        ID = int(input('Введите ID питомца: '))
        delete(ID)

Если пользователь введет "stop", программа завершит работу.

#эту программу признаюсь не сам писал но есть огромное желание понять и разобратся как самому её написать.



#example 13 Двумерные списки
#task 1

def sum(a, b, c):
    for i in range(10):
        print('')
        for j in range(10):
            k = a[i][j] + b[i][j]
            c.append(k)
    print(c, end='') 
n = int(input())
m = int(input())
b = [[random.randint(-200, 200) for i in range(n)] for i in range(m)]
k = [[random.randint(-200, 200) for i in range(n)] for i in range(m)]
c = []
print(b)
print('____________________________')
print(k)
print('____________________________')
sum(b, k, c)




#example 14 Рекурсия
#task 1

def recursion(a, b = 0):
    if len(a) > b:
        print(a[b])
        recursion(a, b + 1)
    else:
        print('Конец списка.')

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recursion(my_list)



#Example 15 ООП
#task 1

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def output(self):
        print(f'Name auto: {self.name} speed: {self.max_speed} car mileage: {self.mileage}')

Autobus = Transport('Renaul Logan', 180, 12)
Gruzovik = Transport('Gaz', 120, 150000)
Autobus.output()
Gruzovik.output()

#task 2

class Transport:

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
 

    def seating_capacity(self, capacity):

        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

n = Autobus('Renault Logan', 120, 200000)    
a = n.seating_capacity()
print(a)
