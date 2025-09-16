# gets the text of the book in the main specified filepath and prints to the console
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

from stats import book_word_count
from stats import book_character_count
from stats import sort_and_filter_alpha

def main():
    filepath = "/home/sarge/workspace/github.com/sarge101/bookbot/books/frankenstein.txt"
    shortpath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    word_count = book_word_count(text)
    character_count = book_character_count(text)
    sorted_alpha_characters = sort_and_filter_alpha(character_count)
    print("============ BOOKBOT ============\n"
        f"Analyzing book found at {shortpath}...\n"
        "----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        "--------- Character Count -------")
    for line in sorted_alpha_characters:
        print(line)
    print("============= END ===============")

main()