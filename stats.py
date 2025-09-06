def num_of_words(book):
    x=book.split()
    return len(x)

def get_characters(book_text):
    book_text = book_text.lower()
    book_text = book_text.split()
    characters = {}
    for text in book_text:
        for char in text:
            if char in characters and char.isalpha():
                characters[char] +=1
            elif char not in characters and char.isalpha():
                characters[char] =1
    return characters

def sort_helper(individual_dicts):
    return individual_dicts["num"]

def sort_dict(char_dict):
    list_of_dicts = []
    for item in char_dict:
        list_of_dicts.append({"char" : item, "num":char_dict[item]})
    list_of_dicts.sort(reverse=True, key=sort_helper)
    return list_of_dicts