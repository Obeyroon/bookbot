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

        #for i in range(0, each_char):
        
        for i in each_char:
            if i not in num_char:
                num_char[i] = 1
            elif i in num_char:
                num_char[i] += 1

    return num_char