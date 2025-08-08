def get_num_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    char_counts = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_counts:
            char_counts[lowered] +=1
        else:
            char_counts[lowered] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sort_characters(character_count_dict):
    sorted = []
    for char in character_count_dict:
        if char.isalpha():
            sorted.append({"char": char, "num": character_count_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
