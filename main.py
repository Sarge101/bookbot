def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)

def main():
    filepath = "/home/sarge/workspace/github.com/sarge101/bookbot/books/frankenstein.txt"
    get_book_text(filepath)

main()