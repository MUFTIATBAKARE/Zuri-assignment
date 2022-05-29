
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from pickletools import string1


def find_anagram(word, anagram):
   # [assignment] Add your code here
    str1 = "word"
    str2 = "anagram"
    if (sorted(str1)) == sorted((str2)):
       return True
    else:
     return False
print(find_anagram("str1", "str2"))


