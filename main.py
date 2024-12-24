def main():
    BOOK_PATH = "books/frankenstein.txt"

    num_words = get_word_count(BOOK_PATH)
    
    print(type(num_words))

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



main()