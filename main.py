# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) == len(anagram):
        if sorted(word) == sorted(anagram):
            return True
        else:
            return True

print(find_anagram('cat', 'act'))
