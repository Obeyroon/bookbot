from stats import get_num_words, get_num_each_char, sorted_list_num_char

def main():

    book_path = "books/frankenstein.txt"
    c_var = get_num_each_char(book_path)

    print("Found " + get_num_words(book_path) + " total words")

    #print(get_num_each_char(book_path))

    print(sorted_list_num_char(c_var))


main()