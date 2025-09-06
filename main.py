from stats import num_of_words, get_characters, sort_dict
import sys

def get_book_text(filepath):
    filecontents =""
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents


def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    x= num_of_words(book)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing books at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {x} total words")
    print("--------- Character Count -------")
    for item in sort_dict(get_characters(book)):
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()