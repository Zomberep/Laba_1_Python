from math import *
import matplotlib.pyplot as plt
# task 1

x = 2
print(f"task 1: Значение переменной x = {x}, а её тип {type(x)}")
x += 3
print(f"Значение переменной x = {x}, а её тип {type(x)}")
x = (x+1) / 2
print(f"Значение переменной x = {x}, а её тип {type(x)}")
x = x + 1/2
print(f"Значение переменной x = {x}, а её тип {type(x)}")
x = (x < 5)
print(f"Значение переменной x = {x}, а её тип {type(x)}")
x = str(x)
print(f"Значение переменной x = {x}, а её тип {type(x)}\n")

# task 2

amount = 1+2+3+4+5
average = amount/5
print(f"task 2: Среднее значение этих 5 чисел (1, 2, 3, 4, 5) равно {average:.5f}")

# task 3
def check(x):
    allowed_symbols = set('0123456789.-')
    while set(x) - allowed_symbols != set():
        x = input("Число введено неверно, попробуйте ещё раз: ")
    return x

amount = (1+2+3+4+5)
curr, count, entered_symbols = '', 5, '1 2 3 4 5'
while (curr != '0'):
    curr = input("\ntask 3: Введите действительное число (0 чтобы закончить): ")
    if curr != '0':
        curr = Check(curr)
        if curr == '0':
            break
        amount += float(curr)
        count += 1
        entered_symbols += " " + curr
        print(f"Среднее значение ({entered_symbols}) равно {amount / count:.5f}")

# task 4

# как далеко и высоко сможет прыгнуть котик:
v0, corner, g = 5, (40*pi)/180, 9.80665
t = (2*v0*sin(corner)) / g
print(f'\ntask 4: Дальность прыжка при таких входных данных равна: {v0*cos(corner)*t:.5f}')
print(f'Максимальная высота полёта равна: {v0*sin(corner)*(t/2) - (1/2)*g*(t/2)*(t/2):.5f}')

# при каком угле дальность/высота полёта будет максимальной (v0 = const)
# (задачу можно решить на бумажке за минуту используя производную, НООО мы пойдем иначе...)
curr_way, max_way, corner, time, answer1, g, curr_height, max_height, answer2 = 0, float(-inf), 0, 0, -1, 9.80665, 0, float(-inf), -1
for i in range(0, 90+1):
    corner = (i*pi) / 180
    time = (2*5*sin(corner)) / g
    curr_way = 5*cos(corner)*time
    curr_height = 5*sin(corner)*(time/2) - (1/2)*g*(time/2)*(time/2)
    if curr_way > max_way:
        answer1 = i
        max_way = curr_way
    if curr_height > max_height:
        answer2 = i
        max_height = curr_height
print(f"\nМаксимальная дальность полёта будет достигнута при угле: {answer1}")
print(f"Максимальная высота полёта будет достигнула при угле: {answer2}")

# чтобы попасть в точку (2, 3) за 1 секунду, какие должны быть v0 и угол?
# решая заданную систему аналитически приходим к уравнениям: tg(x) = 3/2 + g/4 v0 = 2/cos(x)
g = 9.80665
corner = atan(3/2+g/4)
v0 = 2 / cos(corner)
print(f"\nУгол, нужный для достижения условий равен {(corner*180)/pi:.5f}")
print(f"Скорость, с которой нужно прыгнуть коту для выполнения условий равна {v0:.5f}")

# строим график с помощью matplotlib
g = 9.80665
v0 = float(check(input("Введите начальную скорость кота (м/c): ")))
corner = float(check(input("Введите угол к горизонту, под которым кот прыгает (в градусах): ")))
corner = (corner*pi) / 180
time = (2*v0*sin(corner))/g
x, y = [], []
for i in range(0, 9+1):
    curr_moment = (time/10)*i
    x.append(curr_moment*v0*cos(corner))
    y.append(v0*sin(corner)*curr_moment-(g/2)*curr_moment*curr_moment)
x.append(v0*cos(corner)*time)
y.append(0)
plt.plot(x, y)
plt.show()

# task 5
def check2(x):
    allowed_symbols = set('0123456789')
    while set(x) - allowed_symbols != set():
        x = input("Число введено неверно, попробуйте ещё раз: ")
    return x

number = int(check2(input("\ntask 5: Введите натуральное число, сумму цифр которого нужно вычислить: ")))
if number < 10:
    print(f"Сумма цифр числа {number} равна {number}")
while number > 9:
    s = sum([int(x) for x in list(str(number))])
    print(f"Сумма цифр числа {number} равна {s}")
    number = s

# task 6
curr = input('\ntask 6: Вводите действительные числа по одному, чтобы закончить последовательность введите "finish": ')
mx, mn = float(-inf), float(inf)
while curr != "finish":
    curr = check(curr)
    a = float(curr)
    mx = max(mx, a)
    mn = min(mn, a)
    curr = input('Введите следующее число ("finish" чтобы закончить): ')
print(f"Максимальное число из последовательности равно {mx}")
print(f"Минимальное число из последовательности равно {mn}")











