# Importing functions from stats.py file
import sys
from stats import count_words, count_char, sort_dictionary

# Reads content of a book and returns it as a string
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents
    
# Print entire contents of the book in the console
def main():
    # Avoid hard coded input
    args = sys.argv
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    book_text = get_book_text(path)
    number_words = count_words(book_text)
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    number_char = count_char(book_text)
    sorted_char = sort_dictionary(number_char)
    for char in sorted_char:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

    

main()


