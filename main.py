import os

def main():
    ################ WELCOME ################
    print("Welcome to the Bookbot!")
    print("This program will analyze the text of a book and report the number of words\nand the number of times each alphabetical character appears in the text.")
    

    # Creates a list with the .txt files in in books/ directory so it can be prompted
    books_directory = "books"
    books = []
    for filename in os.listdir(books_directory):
        if filename.endswith(".txt"):
            books.append(filename)

    # Input handeling, so the user can either input a filename from the shown list or 'exit'
    # while == True -> reprompting the input to the user when the file does not exist or a report was generated
    while True:
        print()
        print("Which book would you like to analyze?")
        print("There are currently the following files in the 'books' directory:")
        for book in books: 
            print(f"- {book}")
        selected_book = input("Please enter the name of the file (including the .txt extension) or 'exit': ")
        print()
        # so the user can exit the input and end the program
        if selected_book == "exit":
            print("Goodbye!")
            return False

        # if file does not exist --> input reprompted as while input_sate still True:
        if selected_book not in books:
            print("The file you entered does not exist in the 'books' directory.")

        # if the file exists the program will proceed
        else:       
            book_path = "books/" + selected_book
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