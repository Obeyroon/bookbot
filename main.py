from stats import get_num_words, get_num_each_char, sorted_list_num_char
import sys

def main():

    if len(sys.argv) <= 1: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    c_var = get_num_each_char(book_path)

    print("Found " + get_num_words(book_path) + " total words")

    print(sorted_list_num_char(c_var))


main()