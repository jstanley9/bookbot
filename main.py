import stats
import sys

def get_book_txt(path):
    with open(path) as text_file:
        file_data = text_file.read()

    return file_data

def print_heading(caption):
    print(f"============ {caption} ============")

def print_sub_heading(caption):
    print (f"----------- {caption} ----------")

def print_report(file_path, word_count, char_counts):
    print_heading("BOOKBOT")
    print(f"Analyzing book found at {file_path}...")
    print_sub_heading("Word Count")
    print(f"Found {word_count} total words")
    print_sub_heading("Character Count")

    for char_count in char_counts:
        print(f"{char_count[stats.CHAR]}: {char_count[stats.COUNT]}")

    print_heading("END")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_to_use = sys.argv[1]
    document = get_book_txt(file_to_use)
    word_count = stats.count_words(document)
    #print(f"{word_count} words found in the document")
    character_counts = stats.count_each_character(document)
    #print(character_counts)
    sorted_alpha_counts = stats.sort_char_counts(character_counts)
    #print(sorted_alpha_counts)
    print_report(file_to_use, word_count, sorted_alpha_counts)

main()    