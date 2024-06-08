def main():
    book_path = "books/frankenstein.txt"

    book = get_text(book_path)
    word_count = count_words(book)
    chars_count = count_chars(book)

    char_sorted_list = sort_char_list(chars_count)

    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document\n')
   
    for char in char_sorted_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
    
    print('--- End report ---')

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words_list = text.split()
    count = len(words_list)
    return count
        
def count_chars(text):
    chars = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i.isalpha():
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
    return chars

def sort_on(dict):
    return dict['num']

def sort_char_list(chars):
    sorted_char_list = []
    for char in chars:
        sorted_char_list.append({"char":char,"num":chars[char]})
    
    sorted_char_list.sort(key=sort_on,reverse=True)
    
    return sorted_char_list

       
main()