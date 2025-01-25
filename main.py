def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path)
    num_words = count_words(text)
    
    # Create dictionary with count per character in text
    chars_dictionary = count_chars(text)

    # Create a list for dictionaries
    list_with_chars_dictionaries = convert(chars_dictionary)
    # Sort the list for dictionaries
    list_with_chars_dictionaries.sort(reverse=True, key=sort_on)

    

    ################ REPORT ################
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    report_characters_found(list_with_chars_dictionaries)
    print("--- End report ---")



# Returns the text of a file (defined by filepath) as a string 
def read_file(path):
    with open(path) as txt:
        return txt.read()
    
# Counts the words in a string        
def count_words(text):
    words = text.split()
    return len(words)

# Counts the characters in a string 
def count_chars(text):
    dictionary = {}
    for char in text.lower():
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary 

# Converts dictionary into a list of dictionaries
def convert(dict):
    return [{"char": key, "num": value} for key, value in dict.items()]

# A function that takes a dictionary and returns the value of the "num" key
def sort_on(dict):
    return dict["num"]

# A function to report the numbers of alphabetical characters found
def report_characters_found(list_with_chars_dictionaries):
    for char in list_with_chars_dictionaries:
        if char["char"].isalpha():
            print(f"The '{char["char"]}' character was found {char["num"]} times")

main()