# a = int(input("введите число")) 
# if a%2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# a = input("введите название")
# name_len = len(name)
# if a == 0:
#     print("вы ничего не ввели")
#     if 


# a = int(input('введите первое число'))
# b = int(input('введите второе число'))
# if a + b<100:
#     print(a * b)
# else:
#    print(a + b)

# a = input('введдите ваше имя: ')
# if a == 'арсений':
#     print('Привет')
# elif a == 'бубубу':
#     print('Пасхалко!!!! аааааа')
# else:
#     print('а ти кто такой?')
     

# print('отгадай загадку)))))))0000)))))')
# a = input('висит груша нельзя скушать ')
# if a == 'испорченная груша':
#     print('ай маладес')
# else:
#     print('думай еще')

# print('напишите какая щас погода солнечно иле пасмурно')
# a = input('пасмурно или солнечно щас')
# b = int(input('а скока грудусов'))
# if a =='солнечно':
#     print('бери зонт')
# elif 0>=b and a =='пасмурно':
#         print('не бери зонт, но хорошо оденься')

# a = int(input('введите скорость машины '))
# b = int(input('введите расстояние между точками '))
# print('время за которое автомобиль проедет расстояние')
# t = b/a
# if t <= 1:
#     print('мб доедет если пробок нет',t)
# else: 
#     print('не даедет',t)

# a = int(input('под какой процент вы кладете ')) / 100
# b = int(input('ваш вклад в рубляхахахах '))
# c = int(input('на скока ложите '))
# for a in range(c):
#      b += b * a
#      print(f'{b + b} {int(b)}')
# print(b)

# a = input('купи слона) ')
# while True:
#     a = input(f'все говрят{a}а ты купи слона ')

# c = '*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*'
# colichestvo = 0
# for i in c:
#     if i == '*': 
#         colichestvo += 1
# print(colichestvo)

# a = input('введите слово ')
# glasnye = 'ауоыэяюёие'
# e = 0 
# s = 0
# for i in a:
#     if i in glasnye:
#         e += 1
#     else:
#        s +=1
# print(e, s)

# a = int(input('введите число'))
# q = 0
# for i in a:
#     if i == 1:
#         q += 1
#         print(q)

# def print_name(name):
#     print(f'Hello {name}')
#     return 321323123123123123


# print(print_name('алеша'))

# def make_negative(a):
#     if a > 0: 
#         return -a
#     elif a == 0:
#         return a
#     else:
#         return a
    
# print(make_negative(13345543344555664))
# print(make_negative(0))
# print(make_negative(-569696969))

# def between(a, b):
#     return list(range(a, b + 1))

# print(between(1, 494434353))

# def foo(x):
#     return x + 1

# def bar(y):
#     return foo(y) - 1

# s = bar(2)
# print(s)
# from random import randint
# def build_house(my_dream, colors):
#     house = False
    
#     roof_color = colors[0]
#     house_color = colors[1]
#     door_color = colors[2]
#     roof = my_dream[0]
#     walls = my_dream[1]

#     while not house:
#         roof_status = build_roof(roof, roof_color)
#         walls_status = build_walls(walls, house_color)
#         door_status = build_door(door_color, door_color)
#         if roof_status == True and walls_status == True and door_status == True:
#             house = True
#             print('поздравляю ты построил дома уааа')
#     return house
# def build_roof(r, rc):
#     print('строю крышу')
#     return randint(0,1)
# def build_walls(r, wc):
#     print('строю стены')
#     return randint(0,1)
# def build_door(r, dc):
#     print('двери ставлю')
#     return randint(0,1)

# idea = ('roof', 'walls')
# colors = ('red', 'голубой', 'белый')
# build_house(idea, colors)

# numbers = [1, 0, 3.14, -2]


# def apply_to_each(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])

# def change_direction(x):
#     return x * -1

# apply_to_each(numbers, change_direction)

# print

# n_user = int(input('введи число: '))  #.
# m_user = int(input('введи число: ')) # *

# n_and_m = []


# a = '.'
# for i in range(n_user):
#     q = []
#     for j in range(m_user):
#         q.append(a)
#         if a == '.':
#             a = '*'
#         else:
#             a = '.'
#     n_and_m.append(q)
#     if m_user % 2 == 0:
#         if a == '.':
#             a = '*'
#         else:
#             a = '.'
        
# print(n_and_m)
# for i in range(n_user):
#     q = []
#     for j in range(m_user):
#         if (i + j) % 2 == 0:
            
# n = 9
# suma = 0
# for i in range(1, n + 1):  
#     suma += i ** 3

# print(suma)
