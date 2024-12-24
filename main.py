def main():
    BOOK_PATH = "books/frankenstein.txt"

    num_words = get_word_count(BOOK_PATH)
    char_count = get_character_count(BOOK_PATH, True)
    
    print(num_words)
    print(char_count)
    

def open_file(path):
    """
    Functino to open a file

    Args:
        path (string): This is normally defined as a constant in main

    Returns:
        string: Contents of the file that was opened
    """
    with open(path) as f:
        file_contents=f.read()
        return file_contents       

def get_word_count(path):
    """
    Returns the number of grouped characters, in other worsd, "words"

    Args:
        path (string): This is normally defined as a constant in main

    Returns:
        int: the number of words
    """
    word_list = []
    word_list = open_file(path).split()
    return len(word_list)

def get_character_count(path, alpha_only): 
    """
    This function returns the count of individual characters in a document. It can count all characters, including special characters, or only letters in the english alphabet.


    Args:
        path (string): This is normally defined as a constant in main
        alpha_only (boolean): When set to True this functiono will only return the count of letters only.
    """
    dict = {}

    text = open_file(path).split()
    for word in text:
        for char in word:
            if alpha_only:
                if char.isalpha():
                    lowered = char.lower()
                    if lowered in dict:
                        dict[lowered] += 1
                    else:
                        dict[lowered] = 1
            else:
                lowered = char.lower()
                if lowered in dict:
                    dict[lowered] += 1
                else:
                    dict[lowered] = 1
    return(dict)



main()