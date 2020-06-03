# Problem 1.2 Given two strings, write a method to decide if one is a 
# permutation of the other

import hash_table_chain as htc

# Time Complexity -> O(n)
# Space Complexity -> O(n)
def isPermutationHash(s1,s2):
    if len(s1) != len(s2):
        return False
    s1.lower()
    s2.lower()
    h = htc.HashTableChain(len(s1)) # Hashtable that contains each char in s1
    for char in s1:
        h.insert(char,char) 
    for char in s2:
        val = h.retrieve(char)
        if val == None: # char is not on the hashtable
            return False
    return True
 # Note: If the characters from s2 are different than those of s1, then
 # it means s2 is not a permutation of s1.

# Time Complexity -> O(n)
# Space Complexity -> O(n)
def isPermutationArray(s1,s2):
    if len(s1) != len(s2):
        return False
    char_set = [0] * 128
    for char in s1:
        index = ord(char)
        char_set[index] += 1
    for char in s2:
        index = ord(char)
        char_set[index] -= 1
        if char_set[index] < 0:
            return False
    return True
    
 
print('~~~~ Using HashTable ~~~~~~~')
print(isPermutationHash('Ana','anA'))   
print(isPermutationHash('Google','eGgool'))   
print(isPermutationHash('Hash','sHa'))   
print(isPermutationHash('Android','Adxdinro'))   

print('~~~~ Using Array ~~~~~~~')
print(isPermutationHash('Ana','anA'))   
print(isPermutationHash('Google','eGgool'))   
print(isPermutationHash('Hash','sHa'))   
print(isPermutationHash('Android','Adxdinro'))   