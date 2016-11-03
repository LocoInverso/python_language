#task1------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции. 
"""
from math import sqrt
def distance(x1, y1, x2, y2):
    res = sqrt(pow((x2-x1),2) + pow((y2-y1),2))
    return res
print(distance(float(input()), float(input()),float(input()),float(input())))
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя. 

"""
a,n = float(input()),int(input())
def power(a, n):
      if n == 0:
            return 1
      elif n > 0:
            return a * power(a, n-1)
      else: 
            return 1 / a * power(a, n+1)
print (power(a,n))
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1. 
"""
a = float(input())
n = int(input())
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(a, n))
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию. 
"""
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))
#-----------------------------------------------------------------


