## Weekend Health Take Home 

#### Objective
Implement a function named findWords that accepts two arguments: 1) an input string and 2) a dictionary. This 
function should return an array of words from the dictionary that can be formed by rearranging some or all of the 
letters in the input string. Each letter in the input string may be used up to once per word.


#### Solution

1) Count how many times a character appears in a string and store in a dict (hash-map)
2) Iterate over the dictionary list of words
3) Create a copy of the original characters count dict in order to maintain original state
4) Iterate over every character of a word in the list of words, if it exists in teh character count map then
decrement the associated value. If the character doesn't exist then exit the loop and prevent the word
from being added to the valid words array
5) If after looping through all the characters in the word and all char counters in the character counter map are
greater than or equal to zero then add the word to valid words.


#### How to run?
 > python3 find_words.py
 

#### How to test?
There are already doctests that should be sufficient for the scale of this assignment. They cover most of the use
cases so a separate test suite doesn't seem necessary. 