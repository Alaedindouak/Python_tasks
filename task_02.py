with open('book.txt', 'r') as book_file:
    
    words_list = []
    count_letters = 0

# 1. number of words
    for words in book_file:
        words_list.extend(words.split())

    print(">> number of words is ->", len(words_list))   

# 2. average word length of text
    # print(len(words_list))
# 3. number of letters
    for characters in words_list:
        count_letters += len(characters) 

    print(">> number of letters is ->", count_letters) 

# 4. top 10 words by length
    # words_list.sort(key=len, reverse=True)
    # print(">> top 10 words by length are : ")
    # for word in words_list[:10]:
    #     print(" -> ", word)   

# 5. top 10 most frequent letters
    # letters_dic = {}
    # counter = 0
    # for word in words_list:
    #     for character in word:
    #         letters_dic[character] = letters_dic.get(character, 0) + 1

    # print(">> top 10 most frequent letters : ")

    # for key in sorted(letters_dic, key=letters_dic.get, reverse=True):
    #     print(key,'->',letters_dic[key])
    #     counter += 1
    #     if counter == 10:
    #         break


# 6. number of lines (these are paragraphs)
# 7. replace 'Анна Павловна' in the whole text with 'Anna Pavlovna' (save changes to the same file)
    
    

    
