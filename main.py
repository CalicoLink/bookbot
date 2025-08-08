import sys
from stats import(
    get_num_words,
    count_characters,
    sort_characters
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    character_counts = count_characters(text)
    sorted_chars = sort_characters(character_counts)
    
    print_report(filepath, num_words, sorted_chars)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(filepath, word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for char in sorted_characters:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()
