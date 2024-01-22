
def main():
    path_to_file = __file__.rsplit("/",1)[0] + "/books/frankenstein.txt"
    file_text = get_book_text(path_to_file)
    
    num_words = get_words(file_text)
    print(f"{num_words} words found in this text")

    num_letters = get_letters(file_text)
    print(num_letters)

    for i in num_letters.keys():
        if i.isalpha():
            print(f"The {i} character was found {num_letters[i]} times")
            
        else:
            continue
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_words(text):
    words = text.strip(",./n").split(" ")
  
    return len(words)

def get_letters(text_file):
  
    letters = {}
    for c in text_file:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered]+=1
        else:
            letters[lowered] =1
        

#    for word in t_words:
#        word = word.replace(",", "")
#        word = word.replace(".", "")
#        word = word.lower()
#        letter_list = list(word)
        
#        for char in letter_list:
#            if char.isalpha():
#                letters[char]  = letters.get(char,0) +1

    return dict(sorted(letters.items()))

        
main()