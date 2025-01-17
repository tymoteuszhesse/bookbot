def get_books_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_books_text(book_path)
    print(f"--- Begin report of books.frankenstein.txt --- {count_words(text)} words found in the document\n")
    char_count = count_chars(text)
    for char in char_count:
        if char != ' ' and char != '.' and char != '#' and char != '\n':
            print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report ---")      
    
def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count


main()



        