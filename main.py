# gets the text of the book in the main specified filepath and prints to the console
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

# accepts the text from a book as a string and returns the word count
def book_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def main():
    filepath = "/home/sarge/workspace/github.com/sarge101/bookbot/books/frankenstein.txt"
    text = get_book_text(filepath)
    word_count = book_word_count(text)
    print(f"{word_count} words found in the document")

main()