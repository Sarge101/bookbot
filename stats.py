# accepts the text from a book as a string and returns the word count
def book_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

# takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string
def book_character_count(book_text):
    all_lower = book_text.lower()
    char_count = {}
    for c in all_lower:
        if c in char_count:
            char_count[c] += 1
        else: 
            char_count[c] = 1   
    return char_count
