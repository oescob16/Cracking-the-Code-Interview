# Problem 1.1 - Implement an algorithm to determine if a string has all
# unique characters

import hash_table_chain as htc

# Time Complexity -> O(n)
# Space Complexity -> O(n)
def isUniqueHash(s):
    h = htc.HashTableChain(len(s))
    for char in s:
        letter = h.retrieve(char) # Counter
        if letter == None: # Character is not on the hashtable yet
            h.insert(char,1)
        else: # Character appears 2 or more times in the string
            return False
    return True

# Time Complexity -> O(n)
# Space Complexity -> O(n) 
def isUniqueArray(s):
    if len(s) > 128: # String has duplicated characters
        return False
    char_set = [False] * 128
    for char in s:
        val = ord(char) # Variable to map the character 
        if char_set[val]: # Character appears 2 or more times in the string
            return False
        char_set[val] = True # Character appears at least once in the string
    return True
    
print('~~~~ Using HashTable ~~~~~~~')
print(isUniqueHash('Hello'))
print(isUniqueHash('Ana'))
print(isUniqueHash('Google'))
print(isUniqueHash('string'))

print('\n~~~~~~~~ Using Arrays ~~~~~~~~~')
print(isUniqueArray('Hello, World!'))
print(isUniqueArray('Oswaldo'))
print(isUniqueArray('Arrays'))
print(isUniqueArray('Microsoft'))

        