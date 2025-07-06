""" File for analyzing texts """

# Count number of words in the book
def count_words(text):
    words = text.split()
    return len(words)

# Count how many times each character appears
def count_char(text):
    words = text.split()
    character_count = {}
    for word in words:
        lwrcase_word = word.lower()
        for letter in lwrcase_word:
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1
    return character_count

# A function that takes a dictionary and returns the value of the "num" key
def sort_on(items):
    return items["num"]

# Return a sorted list of the dictionary
def sort_dictionary(character_count):
    sorted_characters = []
    # Create a dictionary with two values and append it to a list
    for key in character_count:
        dictionary_count = {}
        if key.isalpha():
            dictionary_count["char"] = key
            dictionary_count["num"] = character_count[key]
            sorted_characters.append(dictionary_count)
    # Sort characters according to count value
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
 
