# accepts the text from a book as a string and returns the word count
def book_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

# takes the text from the book as a string, and returns the number of times each character,
# (including symbols and spaces), appears in the string
def book_character_count(book_text):
    all_lower = book_text.lower()
    char_count = {}
    for c in all_lower:
        if c in char_count:
            char_count[c] += 1
        else: 
            char_count[c] = 1   
    return char_count

def sort_and_filter_alpha(char_dict):
    """
    Convert a dictionary of character counts into a sorted list of single-key
    dictionaries containing only alphabetical characters.
    
    Args:
        char_dict (dict): Dictionary of characters and their counts.
    
    Returns:
        list of dict: List of dictionaries sorted by count descending.
    """
    # Step 1: Convert to list of single-key dictionaries
    list_of_characters = [{k: v} for k, v in char_dict.items()]
    
    # Step 2: Helper function to get the value from a dict
    def sort_on(d):
        return next(iter(d.values()))
    
    # Step 3: Sort in-place from greatest → least
    list_of_characters.sort(reverse=True, key=sort_on)
    
    # Filter only alphabetical and format as strings
    alpha_characters = [
        f"{next(iter(d.keys()))}: {next(iter(d.values()))}" 
        for d in list_of_characters if next(iter(d.keys())).isalpha()
    ]
    
    return alpha_characters
    
            



