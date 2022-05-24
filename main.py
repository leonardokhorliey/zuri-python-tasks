# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    # [assignment] Add your code here
    for i in range(len(word)):
        if word[i].lower() != word[-1 - i].lower():
            return False

    return True

