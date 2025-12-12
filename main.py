from stats import get_num_words, get_num_each_char

def main():

    book_path = "books/frankenstein.txt"

    print("Found " + get_num_words(book_path) + " total words")

    print(get_num_each_char(book_path))


main()