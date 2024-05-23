def count_characters(word: str) -> dict:
    """
    Returns a count of how many times a character appears in word as a dict, where the key is the character and the
    value is the number of times the character appears in the word. Essentially what Counter does from the collections
    library

    >>> count_characters("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}


    :param word:
    :return:
    """
    char_count_dict = {}
    for c in word:
        char_count_dict[c] = char_count_dict.setdefault(c, 0) + 1
    return char_count_dict


def find_words(input_string: str, dictionary: list[str]) -> list[str]:
    """
    Solution:
    1) Count how many times a character appears in a string and store in a dict (hash-map)
    2) Iterate over the dictionary list of words
    3) Create a copy of the original characters count dict in order to maintain original state
    4) Iterate over every character of a word in the list of words, if it exists in teh character count map then
        decrement the associated value. If the character doesn't exist then exit the loop and prevent the word
        from being added to the valid words array
    5) If after looping through all the characters in the word and all char counters in the character counter map are
        greater than or equal to zero then add the word to valid words.

    Time Complexity:
     - There'll be one iteration over the input_string to build the character counter dict, let's call this 'K'
     - We iterate over the list of words in the dictionary list, this is 'M'
     - Then we iterate over every character in each word in the list but since we break from the loop if we encounter
        a character that doesn't exist in the input_string. This would be at worst the average length of the words in
        the dictionary list if all the words are valid and continue full execution, for example: input_string = 'ate',
        dictionary = ['eat','tea','ate'], and at best if none of the words in the dictionary start with a letter not in
        the input string then we exit immediately. input_string = 'ate', dictionary = ['dog', 'bat', 'car']. This loop
        will be referred to as 'N'
    - There is one final loop through the values in the dictionary which at most would be size K or less if there are
        repeating characters in the string. This will be 'L'

    Overall the time complexity will be 'K + L + (M * N)'


    >>> find_words("ate", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"])
    ['ate', 'eat', 'tea']

    >>> find_words('dog', ['god', 'good', 'tea'])
    ['god']

    >>> find_words('', ['bat', 'dad'])
    []

    >>> find_words('ate', [])
    []

    :param input_string:
    :param dictionary:
    :return:
    """
    # input_string_char_count = Counter(input_string)
    input_string_char_count = count_characters(input_string)
    valid_words = []
    for word in dictionary:
        input_string_char_count_copy = input_string_char_count.copy()
        contains_only_valid_characters = True
        for c in word:
            char_count = input_string_char_count_copy.get(c)

            if char_count is None:
                contains_only_valid_characters = False
                break

            input_string_char_count_copy[c] = char_count - 1

        if contains_only_valid_characters and all(count >= 0 for count in input_string_char_count_copy.values()):
            valid_words.append(word)

    return valid_words


