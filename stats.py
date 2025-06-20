CHAR = "char"
COUNT = "count"

def count_words(document):
    word_list = document.split()
    word_count = len(word_list)
    return word_count

def count_each_character(document):
    lowered = document.lower()
    character_dictionary = {}
    for character in lowered:
        counter = 1
        if character in character_dictionary:
            counter = character_dictionary[character] + 1
        character_dictionary[character] = counter

    return character_dictionary

def sort_on(items):
    return items[COUNT]

def sort_char_counts(dictionary):
    char_dictionaries = []
    char_dict = {}
    for char, count in dictionary.items():
        if char.isalpha():
            char_dict = {CHAR: char, COUNT: count}
            char_dictionaries.append(char_dict)

    char_dictionaries.sort(reverse = True, key = sort_on)

    return char_dictionaries

def main():
    dict = {"a": 25, "b": 33, "c": 19, "-": 203}
    print(dict)
    new_dict = sort_char_counts(dict)
    print(new_dict)

if __name__ == "__main__":
    main()
