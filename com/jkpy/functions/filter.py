
str1 = ['a','b','c','e','f','i','o','j','u']

def find_non_vowels(alphabet):
    vowels = ['a','e','i','o','u']
    if alphabet in vowels:
        return True
    else: return False

list1 = filter(find_non_vowels,str1)
print(list(list1))