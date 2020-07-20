letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
        return False
    else:
        return True


filtered_vowels = filter(filterVowels, letters)
print(f'Type of filtered_vowels is : {type(filtered_vowels)}')
print(f'Printing Non Vowel characters: \n')
for vowel in filtered_vowels:
    print(vowel)
print(f'*'*120)
print(f'Without the FUnction inside filter: \n')

randomList = [1, 'a', 0, False, True, '0']

filtered_list = filter(None,randomList)
for item in filtered_list:
    print(item)