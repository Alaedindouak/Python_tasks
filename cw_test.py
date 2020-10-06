# 0. Combine all arguments (via *argc) into the list

def merge_list(*args):

    # just here I couldn't make else statement
    # return [item for items in args if isinstance(items, (tuple, list, set)) for item in items]
   
    ls = []
    for items in args:
        if isinstance(items, (tuple, list, set)):
            for item in items:
                ls.append(item)
        else:
            ls.append(items)

    return ls

# print(merge_list([0,0], 'nice', {5,4,1}, (12,9), None))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

            
# 1. Merge elements of separated lists into one list

def merge_to_list(lists):
    return [item for sub_list in lists for item in sub_list]
    
# print(merge_to_list([[1, 8, 3], [-5, 0], [4], [2, 3, 3]]))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 2. Raise to the power each element of the list by another list

def multi_power(original, powers):
    return [org_items ** pow_items for org_items, pow_items in zip(original, powers)]


original = (3, 2, 0, -2, -7)
powers = (1/3, 7, 10, -2, 3)
result = multi_power(original, powers)

# print(result)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 3. Remove duplicates from a list of list

def remove_duplicates(lists):
    new_list = []
    for item in lists:
        if item not in new_list:
            new_list.append(item)

    return new_list
    

# print(remove_duplicates([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 4. Expand the list element inside the tuple at i index without using list() or tuple() built-in functions

def expand(unchangeable, index=None, expandby=None):
    for i in range(len(unchangeable)):
        if i == index:
            unchangeable[i][0:] += expandby 

    return unchangeable

# print(expand(([1, 2], [3, 4], [5, 6])))