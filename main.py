from stats import get_num_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    character_counts = count_characters(text)
    print(f"{num_words} words found in the document")
    print(character_counts)

main()
