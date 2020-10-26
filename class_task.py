def my_func(string, dup):
    return string * dup

# print(my_func('alaedin', 3))


def shift(ls, steps):
    return ls[-steps:] + ls[:-steps]

# print(shift([4, 5, 6, 7, 8, 9, 0], 2))

def has_equal_diff(arr):

    diff = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] == diff : 
            return True
        else : 
            return False 

print(has_equal_diff([5,10,15,25,30])) 



def intersection(list_1, list_2):

    new_list = []

    for item in list_1:
        if item in list_2:
            new_list.append(item)
    
    print(new_list) 


# intersection([1, 3, 1, 2, 3, 5], [2, 1, 1, 4, 5, 13, 1])           

