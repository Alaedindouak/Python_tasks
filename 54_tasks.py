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

def func_6(amount, per):
    print('{:.2f}'.format(amount * ( 1 + per/100 )**5))
   
# func_6(200000, 2)    

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

def func_12(ls, slice):
    return sum(ls[slice[0]:slice[1] + 1])

# print(func_12([1, 5, -1, 9, 0, 2], (2, 5)))  

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

def func_18(str, *args):
    words = str.split(' ')
    for i in args:
        for j in words:
            for l in range(len(j)):
                if (j[l] == i):
                    del words[words.index(j)]
    return words             

# print(func_18("In the hole in the ground there lived a hobbit",'t', 'h', 'r'))

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

def func_25(ls):
    pass

# print(func_25([1,2,-5,1,4,2]))

# 26 --
''' проверяет есть ли в массиве повторяющиеся элементы'''

def func_26(ls):
    return any(ls.count(item) > 1 for item in ls) 

# print(func_26([1,2,0,0,4,0]))      

# 27 -- 
''' возвращает количество элементов списка, которые отличны от наибольшего элемента не более чем на 10% '''

def func_27(ls):
    ten_percent=( 10 * max(ls) ) / 100
    total=[]
     
    for i in range(len(ls)):
        if ls[i] >= max(ls) - ten_percent:
            total.append(ls[i])
    return total

# print(func_27([50,40,71,100,95,97,96]))

# 28 --
''' на вход получает список C, и меняет знак у элементов, значения которых между A и B '''

def func_28(ls, a, b):
    for i in range(len(ls)):
        if ls[i] in range(a, b):
            ls[i] *= -1
    return ls

# print(func_28([1,5,-7,13,-1], 2, 11))    

# 29 --
''' проверяет одинаковы ли 2 списка '''

def func_29(ls_1, ls_2):
    return ls_1 == ls_2

# print(func_29([1,2,4], [3,2,4]))    

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

def func_32(ls):
    res = sorted(range(len(ls)), key=lambda sub: ls[sub])[-2:]
    ls.sort(reverse=True)
    x = (ls[:2])
    return res, x

# print(func_32([1,2,8,8,5,10,11,0,-1]))

# 33 --
''' находит наименьшее расстояние между локальными максимумами списка '''

def func_33(ls):
    flag = max(ls)
    x = max(ls)
    for i in range(len(ls)):
        if flag - ls[i] < x and flag - ls[i] != 0:
            x = flag - ls[i]
    return x

# print(func_33([0,6,1,-1,4,1,-1,0]))

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
    flip = {}
    for key , value in dic.items():
        if value not in flip:
            flip[value] = [key]
        else:
            flip[value].append(key)
    return flip

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
    pass

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

from random import randrange

def func_41(row, column):
    
    ls = []

    while row != 0:
        row -= 1

        ls_x = [randrange(2,15) for c in range(column)]
        ls.append(ls_x)

    return ls
    
# mul_list = func_41(2, 3)
# print(mul_list)    

# 42 --
''' находит минимум и максимум матрицы из предыдущей задачи '''

def func_42(ls):

    min = max = ls[0][0]

    for i in range(len(ls)):
        for j in range(len(ls[i])):

            if min < ls[i][j]:
                min = ls[i][j]

            elif max > ls[i][j]:
                max = ls[i][j]

    return min, max            

# print(func_42(mul_list))   

# 43 --
''' находит максимум матрицы для каждой строки '''

def func_43(matrix):
    
    max_elements = []
    max_elem = 0

    for i in range(len(matrix)):
        max_elem = matrix[i][0]

        for j in range(len(matrix[i])): 

            if max_elem < matrix[i][j]:
                max_elem = matrix[i][j]
        
        max_elements.append(max_elem)

    return max_elements  

# print(func_43([[2,5,7,6], [8,8,13,5], [9,11,4,8], [8,6,12,5]]))        


# 44 --
''' находит максимум матрицы для каждого столбца '''

def func_44(matrix):
    
    max_elements = []
    max_elem = 0

    for i in range(len(matrix)):
        max_elem = matrix[0][i]

        for j in range(len(matrix[i])):
            
            if max_elem < matrix[j][i]:
                max_elem = matrix[j][i]

        max_elements.append(max_elem)
    
    return max_elements
    
# print(func_44([[2,5,7,6], [8,8,13,5], [9,11,4,8], [8,6,12,5]]))

# 45 --
''' находит максимум матрицы для каждого столбца '''

def func_45(matrix):
    max_element = 0
    x = 0
    y = 0

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if matrix[i][j] > max_element:
                max_element = matrix[i][j]

                x = i
                y = j

    matrix[x][y] = 0

    return matrix
        
# print(func_45([[2,5,7,6], [8,8,13,5], [9,11,4,8], [8,6,12,5]]))    
    
# 46 --
''' заполняет 0 содержимое матрицы и 1 границы матрицы '''

def func_46(matrix):

    for i in range( len(matrix) ):
        for j in range(len( matrix[i] )):

            if i == 0 or j == 0 or i == len(matrix[i]) - 1 or j == len(matrix[i]) - 1:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    print(matrix)                
 

# func_46([[2,5,7,6], [8,8,13,5], [9,11,4,8], [8,6,12,5]])

# 47 --
''' находит наиболее частое значение в матрице '''

def func_47(matrix):

    numbers= []
    num = 0
    counter = 0

    for i in range( len(matrix) ) :
        for j in range( len( matrix[i] ) ) :

           numbers.append( matrix[i][j] ) 

           for n in numbers:
                frequency = numbers.count(n)

                if frequency > counter:
                    counter = frequency
                    num = n
 

    return num
       

# print(func_47( [[2,5,7,6], [8,8,13,5], [9,11,4,8], [8,6,12,5]] ))

# 48 --
''' меняет местами строки матрицы указанные пользователем '''

def func_48(matrix, a, b):
    
    temp_row = matrix[a]
    matrix[a] = matrix[b]
    matrix[b] = temp_row

    return matrix


# print(func_48( [[2,5,7,6], [8,8,13,5], [9,11,4,8], [8,6,12,5]], 0, 2))

# 49 --
''' меняет местами столбцы матрицы указанные пользователем '''

def func_49(matrix, a, b):

    for i in range( len(matrix) ):
        temp_column = matrix[i][a]
        matrix[i][a] = matrix[i][b]
        matrix[i][b] = temp_column

    return matrix        

# print(func_49( [[2,5,7,6], [8,8,13,5], [9,11,4,8], [8,6,12,5]], 1, 2))

# 50 --
''' на вход получает два списка, и если они одинаковой длины, 
     то возвращает список из произведения элементов друг на друга, 
     иначе объединяет в один список и возвращает разницу всех элементов '''

def func_50(ls_1, ls_2):

    if len( ls_1 ) == len( ls_2 ):
        return [num_1 * num_2 for num_1, num_2 in zip(ls_1, ls_2)]
    else:
        return [*ls_1, *ls_2], len(ls_1) - len(ls_2)

# print(func_50([1,2,1,0], [5,-2, 0]))   

# 51 -- 
''' удаляет строку матрицы, в которой количество нулей максимально '''

def func_51(matrix):
    for i, v in enumerate(matrix):
        print(v) 
          

func_51( [[2,5,0,6], [8,0,13,0], [9,11,4,8], [8,6,12,5]] )
# print(func_51([[2,5,0,6], [8,0,13,0], [9,11,4,8], [8,6,12,5]]))




