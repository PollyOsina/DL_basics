# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 03:21:21 2022

@author: Polly
"""

# Задание 1
# Реализуйте функцию almost_double_factorial(n), вычисляющую произведение всех 
# нечётных натуральных чисел, не превосходящих nn.
# В качестве аргумента ей передаётся натуральное (ноль -- натуральное) число n⩽100.
# Возвращаемое значение - вычисленное произведение.

# Комментарий. В случае, если n = 0, требуется вернуть 1.

# В этом задании функция print вам не понадобится. Результаты выполнения функций нужно возвращать, а не печатать!

def almost_double_factorial(n):
    factorial = 1
    if n == 0:
        factorial
    else:
        for i in range(1, n+1,2):
            factorial *= i
    return factorial

# Задание 2
# Пусть у нас есть следующий список, в котором элементы -- tuple из строк:

# items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
# Мы хотим отсортировать этот список по последней букве второго элемента каждого tuple, т.е. получить такой список:

# sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six'),]
# Напишите код вместо "<YOUR CODE>" в следующем выражении, чтобы получить верную сортировку.

# sorted_items = sorted(items, key=lambda x: <YOUR CODE>)

# items объявлять не нужно
sorted_items = sorted(items, key=lambda x:x[1][::-1] )


# Задание 3
# Дан list x:

# x = [1, 2, 3, 4, 5]
# x[<YOUR CODE>] = [-1, -3, -5]

# x
# Заполните слайс вместо <YOUR CODE>, чтобы результатом стал следующий list:

# [-5, 2, -3, 4, -1]
# Ничего больше менять в коде, например, создавать x или печатать его, не нужно! 

x[4::-2] = [-1, -3, -5]

# Задание 4
# Дан массив А[0,..., N-1]. Реализуйте функцию cumsum_and_erase(...), 
# ринимающую один обязательный аргумент A и один опциональный аргумент erase, по 
# умолчанию равный 1.

# Функция должна выполнять следующие действия: 

#  *сформировать массив B[0,...N-1], где Bi = A0+...+Ai -  массив частичных сумм
#   массива А
#  *удалить из массива В все элементы, равные параметру erase; получить массив C;
#  *вернуть C в качестве ответа
# Постарайтесь сделать это за время O(N) без использования Numpy.
# A = [5, 1, 4, 5, 14] 
# B = cumsum_and_erase(A, erase=10) 
# assert B == [5, 6, 15, 29], "Something is wrong! Please try again"
# В этом задании функция print вам не понадобится. Результаты выполнения функций 
# нужно возвращать, а не печатать!

def cumsum_and_erase(A, erase = 1):
    b=0
    C=[]
    for i in A:
        b += i
        if b != erase:
            C.append(b)
    return C

# Задание 5
# Дан список текстов, слова в которых разделены пробелами (можно считать, 
# что знаков препинания нет). 
# Часть слов является "мусорными": в них присутствуют цифры и спецсимволы. 
# Отфильтруйте такие слова из каждого текста.

# Используйте функции str.split, str.isalpha, str.join, а также list comprehensions. 
# Пример ввода:

# ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']

# Пример вывода: 

# ['thousand devils', 'My name is', 'Ro

def process(sentences):
    result = [' '.join([word for word in item.split() if word.isalpha()]) for item in sentences]
    return result

# Задание 6
# Реализуйте класс "Нейрон", у которого будет несколько методов: 
# __init__. Принимает на вход массив весов нейрона w = (w1,...,wn), а также 
# функцию активации f (аргумент по умолчанию f(x) = xf(x)=x) Сохраняет веса и 
# функцию внутри класса.

# forward. Принимает на вход массив x = (x1,...,xn) - входы нейрона. 
# Возвращает f(w1*x1,...,wn*xn)

# backlog. Возвращает массив x, который подавался на вход функции forward при 
# её последнем вызове. Если ранее функция forward не вызывалось, возвращает None.

class Neuron:

    def __init__(self, w: list, f=lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x: list):
        self.x = x
        return self.f(sum([w_el * x_el for w_el, x_el in zip(self.w, x)]))
    
    def backlog(self):
        return self.x    

