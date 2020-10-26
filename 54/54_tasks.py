# -->
sqrt = lambda a : a**(1/2)

# 1 --
'''на вход получает два числа. 
     Верните tuple суммы и произведения данных чисел'''

def func_1(number_1, number_2):
    return (number_1 + number_2, number_1 * number_2)

# print(func_1(4, 10))    

# 2 --
'''вычисляет sqrt(x + sqrt(y))'''

def func_2(x, y):
    return sqrt(x + sqrt(y)) 

# print(func_2(12, 50))

# 3 --
'''выводит на экран числа между 1000 и 4250 (оба включены),
     которые делятся на 5, но не кратны 3'''

def func_3():    
    # here I defined the range 4251, to include 4250 as well
    return [number for number in range(1000, 4251) if number % 5 == 0 and number % 3 != 0]     

# print(func_3())

# 4 --
''' принимает на вход число. Если оно от 3 до 6 включительно, то уменьшить его на 13. 
     Если оно от 8 до 41, то уменьшить на 50. Если оно не более 0 или более 2000, 
     то увеличить в 4 раза. Иначе занулить это число. Вернуть результат'''

def func_4(number):
    if number > 3 and number <= 6 :
        number -= 13
    elif number > 8 and number < 41 :
        number  -= 50
    elif number < 0 or number > 2000 :
        number *= 4
    else:
        number = 0
    
    return number

# print(func_4(-9))    

# 5 --
''' принимает значение в градусах Цельсия, 
     а выводит температуру  в градусах Фаренгейта'''

def func_5(c_degree):
    return (c_degree * 9/5) + 32

# print(func_5(8))

# 6 --
''' на вход получает сумму вклада в банк и годовой процент. 
     Вывести на экран сумму вклада через 5 лет.'''

def func_6():
    pass
    

# 7 --
''' получает на вход количество недель, месяцев, 
     лет и выводит количество дней за это время. Считать, что в месяце 30 дней.'''

def func_7(weeks, months, years):
    return (weeks * 7) + (months * 30) + (years * 360)     

# print(func_7(1, 4, 3))

# 8 --
''' возвращает простые множители данного числа '''

def func_8(number):

    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    divisor = 3
    
    while number != 0 and divisor <= number:

        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 2

    return factors

# print(func_8(40))

# 9 --
'''возвращает все делители данного натурального числа'''

def func_9(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]

# print(func_9(36))

# 10 --
''' возвращает длину отрезка, когда даны координаты начала и конца '''

def func_10(x_1,y_1, x_2, y_2):
    return sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))

# print(func_10(0,0,1,1))

# 11 --
''' выводит все квадраты натуральных чисел, не превосходящие N, в порядке возрастания'''

def func_11(number):
    # maybe like this !!
    return [sqs**2 for sqs in range(number) if sqs**2 < number]
   

# print(func_11(100))

# 12 --
''' находит сумму элементов в указанном срезе (конец включителен) '''

def func_12():
    pass

# 13 --
''' возвращает список размера N, заполненного значениями M '''

def func_13(value, iterator):
    return [value] * iterator

# print(func_13(-1, 6))    

# 14 --
''' удаляет все элементы списка с данным значением'''

def func_14(ls, item):
    return [l for l in ls if l != item]
    
# print(func_14([1,2,4,5,4,3,4], 4))    

# 15 --
''' меняет местами наименьшую и наибольшую цифру в числе '''

def func_15(number):
    numbers_list = [int(n) for n in str(number)]

    index_max_value, index_min_value = numbers_list.index(max(numbers_list)), numbers_list.index(min(numbers_list)) 

    min_value, max_value = min(numbers_list), max(numbers_list)

    numbers_list[index_max_value], numbers_list[index_min_value] = min_value, max_value

    return numbers_list 

# print(func_15(45321))    

# 16 --
'''проверяет число, если в нем цифры расположены по убыванию. Вернуть True если это так'''

def func_16(ls):
    return all(ls[i] >= ls[i + 1] for i in range(len(ls) - 1))
    
# print(func_16([5,4,3,2,2,1,8,9,4,3]))

# 17 --
'''determines if the list is symmetric'''

def func_17(ls):
  pass
    
    
# print(func_17([9,8,5,5,8,9]))


#18 --
''' возвращает строку, в которой удаляются слова, 
     где есть хотя бы одна буква указанная пользователем (*argc)'''
def func_18(*args):
    print(args)

# func_18()

# 19 -- 
'''проверяет, является ли строка корректной записью IP-адреса. 
     Если да, вернуть True, иначе False'''

def func_19(ip):
    ip_node = list(map(int, ip.split('.')))
    
    if len(ip_node) != 4 :
        return False

    for ip in ip_node:
        if ip < 0 or ip > 255:
            return False

    return True          

# print(func_19("127.0.0.280") ) 

# 20 -- 
''' извлекает из строки все символы, 
     являющиеся цифрами и возвращает эту новую строку '''

def func_20(str):
    new_str = ''
    for number in str:
        if number.isdigit():
            new_str += number

    return new_str


# print(func_20("ab = 2 + 278"))  

# 21 -- 
''' принимает множество чисел на вход (*argc) и выводит среднее арифметическое 
     для нечетных чисел и отдельно среднее арифметическое для четных'''

def func_21(*args):
    odd_numbers = [n for n in args if n % 2 != 0]
    even_numbers = [n for n in args if n % 2 == 0] 

    mean = lambda arg : sum(arg) // len(arg)

    return mean(odd_numbers), mean(even_numbers)
    
# print(func_21(6, 1, 2, 1))

# 22 --
''' возвращает индексы ненулевых элементов списка '''

def func_22(ls):
    return [index for index, value in enumerate(ls) if value != 0]     

# print(func_22([1,2,0,0,4,0]))

# 23 ---
''' возвращает ближайший элемент к заданному значению списка'''

def func_23(ls, n):
    diff = lambda ls: abs(ls - n)
    return min(ls, key=diff)

# print(func_23([1,2,8,0,4,0], 7))    
     
#24 --
''' после каждой гласной добавляет букву "с" и повторяет эту
     гласную (аса, еса, иса, и т.д.)'''

def func_24(sentence):
    rus_vowels = ['а', 'э', 'ы', 'у', 'о', 'я', 'е', 'ё', 'ю', 'и']
    new_sentence = ''
    for cons in sentence:
        if cons in rus_vowels:
            new_sentence += cons + 'с' + cons
        else:
            new_sentence += cons    

    return new_sentence        
   

# print(func_24("привет, как дела"))

# 25 --
''' возвращает три последовательных элемента в списке, сумма которых максимальна'''

def func_25():
    pass

# 26 --
''' проверяет есть ли в массиве повторяющиеся элементы'''

def func_26(ls):
    return any(ls.count(item) > 1 for item in ls) 

# print(func_26([1,2,0,0,4,0]))      

# 27 -- 
''' возвращает количество элементов списка, которые отличны от наибольшего элемента не более чем на 10% '''

def func_27():
    pass

# 28 --
''' на вход получает список C, и меняет знак у элементов, значения которых между A и B '''

def func_28():
    pass

# 29 --
''' проверяет одинаковы ли 2 списка '''

def func_29(ls_1, ls_2):
    return ls_1 == ls_2

# print(func_29([1,2,4], [1,2,4]))    

# 30 --
''' "сжимает" список, то есть перемещает все ненулевые элементы в левую часть списка, 
     не меняя их порядок, а все нули - в правую часть '''

def func_30(ls):
    count = 0
    for item in range(len(ls)):
        if ls[item] != 0:
            ls[count] = ls[item]
            count += 1

    while count < len(ls) :
        ls[count] = 0
        count += 1

    return ls       

# print(func_30([4, 0, 5, 0, 3, 0, 0, 5]))                 

# 31 --
''' выводит все элементы списка с четными индексами '''

def func_31(ls):
    return [ls[i] for i in range(len(ls)) if i % 2 == 0]

# print(func_31([1,2,8,8,5,10,11,0,-1]))  

#32 -- 
''' находит индексы локальных максимумов списка '''

def func_32():
    pass

# 33 --
''' находит наименьшее расстояние между локальными максимумами списка '''

def func_33():
    pass

# 34 --
''' выводит название месяца по введенному номеру месяца (hint: создать словарь) '''

def func_34(month_number):
    months = {
              1:'Январь',
              2:'Февраль',
              3:'Март',
              4:'Апрель',
              5:'Май',
              6:'Июнь',
              7:'Июль',
              8:'Август',
              9:'Сентябрь',
              10:'Октябрь',
              11:'Ноябрь',
              12:'Декабрь'}

    return months[month_number]
    
# print(func_34(5))    

# 35 --
''' выводит название поры года (весна, лето и т.д.) по номеру месяца '''

def func_35(month_number):
    seasons = {
        'Лето': [6, 7, 8],
        'Осень': [9, 10],
        'Зима': [1, 2, 3, 11, 12],
        'весна': [4, 5]
    }

    for season, months in seasons.items():
        if month_number in months:
            return season

# print(func_35(1))

# 36 --
''' из двух списков одинаковой длины создает словарь, 
     где ключами будут элементы первого списка, а значениями -- второго '''

def func_36(ls_1, ls_2):
    return dict(zip(ls_1, ls_2))

# print(func_36([1,2,3,4], ['a', 'b', 'c', 'd']))    

# 37 -- 
''' проверяет, есть ли в словаре повторяющиеся значения (элементы), если есть, 
     то сделать ключом этот элемент, а бывшие ключи сделать значениями в списке. 
     Удалить старые записи повторяющихся элементов со старыми ключами '''

def func_37(dic):
    pass
    # result = {}
    # for key, value in dic.items():
    #     print(key, value)
        # print(key, value)
    
    #     if value in result:
    #         result.setdefault(value, []).append(key)
    # return result        
# func_37({1: 'a', 2: 'a', 3: 'a', 4: 'd'})
# print(func_37({1: 'a', 2: 'a', 3: 'a', 4: 'd'}))

# 38 -- 
''' в словаре меняет местами ключи со значениями'''

def func_38(dic):
    return dict((v, k) for k, v in dic.items())

# print(func_38({1: 'a', 2: 'b', 3: 'c', 4: 'd'}))

# 39 --
''' добавляет пару ключ:значение в словарь, и если есть такой ключ, 
     то добавить к существующему элементу этого ключа новое значение '''

def func_39(dic, key=None):
    key_ls = [key for key in dic.keys()]
    if key[0] in key_ls:
        return True
        
    # for key in dic.get(item[0]):
    #     print((key,te))
    # for k in dic.keys():
    #     if item[0] == k :
    #         dic[k].(item[1])
    # print(dic)        
    # for i in item:
    #     print(i)
    # print(item[0])

# print(func_39({1: 'a', 2: 'b', 3: 'c'}, (1, 'ff')))     

# 40 -- 
''' генерирует словарь следующим образом: на вход функции подаётся число N, 
     от 1 до N генерируются ключи, а значениями является их квадрат (i, i * i) '''

def func_40(n):
    dic = dict()
    for i in range(1, n + 1):
        dic[i] = i * i
    
    return dic

# print(func_40(6))             
                 
# 41 --
''' генерирует список списков (это матрица, число строк N и число столбцов M) 
     и заполняет их случайными целыми числами от 2 до 14  '''

from random import sample

def func_41(row, column=0, start=0, end=0):
   pass
            

# print(func_41(4, 4, 2, 14))             


