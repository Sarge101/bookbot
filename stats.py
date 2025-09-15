# accepts the text from a book as a string and returns the word count
def book_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count