dbase = [
	'+5(4671)849-6225',
	'+394(63)128-1148',
	'535(02)715-68-89',
	'+72(23)661-8520',
	'+194(455)628-2961',
	'092158146777',
	'+862(179)416-6138',
	'+3(2697)794-4711',
	'+98(393)874-4458',
	'+5(07)958-7521',
	'+3(632)626-8042',
	'+7611528-9013',
	'+88135130-7172',
	'94(3005)670-58-48',
	'+264925558-7301',
	'58(6929)091-8491',
	'+581(067)254-6659',
	'+4(838)997-1720',
	'+7(163)228-1948',
	'72236618520',
	'507958-7521',
	'967(28)959-4951',
	'+53(2121)207-3793',
	'+80(922)2856718',
	'7121-2173999'
]

# 0. remove all brackets, hyphens and + signs from strings (use the .replace() function)

def remove_characters_from_phone_number(phone_numbers):
    
    characters_to_remove = '()-+'
    number_phone_list = []

    for number in phone_numbers:
        for character in characters_to_remove:
            number = number.replace(character, '')

        number_phone_list.append(number)

    return number_phone_list     

# print(remove_characters_from_phone_number(dbase))      

# 1. bring the dbase to a form where instead of a string there will be a tuple of three numbers 
# (country code, city/operator code, user code)

def to_tuple(phone_numbers):

    p_numbers = remove_characters_from_phone_number(phone_numbers)
    phone_number_list = []

    for number in p_numbers:
        user_code = number[-7:]
        city_code = number[-10:-7]
        country_code = number[:-10]

        phone_number_list.append((country_code, city_code,user_code))

    return phone_number_list    

# print(to_tuple(dbase))


# 2. how many numbers in this base

def count_phone_numbers(phone_number):
    print(f'There are {len(phone_number)} numbers in the database')

# count_phone_numbers(dbase)    


# 3. how many numbers in this base.

def count_countries_by_phone_number(phone_numbers): 
    
    count = 0 
    numbers = to_tuple(phone_numbers)
    
    for number in numbers:
        if number[0] :
            count += 1

    print(f'There are {count} countries in the database')
    
# count_countries_by_phone_number(dbase)


# 4. what is the longest number ?
       
def longest_numbers(phone_number):

    numbers = remove_characters_from_phone_number(phone_number)
    length = len(max(numbers, key= len))

    numbers_list = []

    for number in numbers:
        
        if len(number) == length :            
            numbers_list.append(number)

    print(f'The longest numbers {[number for number in numbers_list]} is {length} digits long')

# longest_numbers(dbase) 


# 5. if there are some duplicates in the database - delete from the database

def remove_duplicates_phone_numbers(phone_numbers):

    numbers = remove_characters_from_phone_number(phone_numbers)

    for number in numbers :
        if numbers.count(number) > 1 :
            numbers.remove(number)

    return numbers

# print(remove_duplicates_phone_numbers(dbase))


# 5. create a variable of the list type, where there will be only Russian phone numbers (country code +7)

def phone_number_to_russian(phone_numbers):

    numbers = remove_characters_from_phone_number(phone_numbers)

    for number in numbers :
        if number[0] == '7':
            print(f"+{number[:1]}({number[1:4]}) {number[4:]}")

phone_number_to_russian(dbase)            