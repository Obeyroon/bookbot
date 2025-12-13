def get_num_words(filepath):

    with open(filepath) as f:
        file_txt = f.read()
        words = file_txt.split()

    num_words = str(len(words))
    return num_words

def get_num_each_char(filepath):

    num_char = {}

    with open(filepath) as f:
        file_txt = f.read().lower()
        each_char = list(file_txt)
        for i in each_char:
            if i not in num_char:
                num_char[i] = 1
            elif i in num_char:
                num_char[i] += 1

    return num_char

def sort_on(items):
    return items["num"]

def sorted_list_num_char(char_counts):

    final = []
    char_list = []
    char_key, num_key = "char", "num"

    for i in char_counts:
        char = {char_key : i, num_key : char_counts[i]}
        
        if i.isalpha():
            char_list.append(char)
        
        
    char_list.sort(reverse = True, key=sort_on)

    for i in char_list:
        final.append(i["char"] + ": " + str(i["num"]))
    
    return final
