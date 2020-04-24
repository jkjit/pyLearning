
from collections import Counter

str1 = " This is a    very big string example with      lot of spaces"

print(str1.split())
# str2 = (str1.split()).remove(" ")
print(str1)
res = " ".join(str1.split())
print(res)

res1 = " ".join(res)
print(res1)

word_set = " This is a series of strings to count " \
   "many words . They sometime hurt and words sometime inspire "\
   "Also sometime fewer words convey more meaning than a bag of words "\
   "Be careful what you speak or what you write or even what you think of. "\

word_list = word_set.split()
print(word_list)

word_count = Counter(word_set)
print(word_count)
print(word_count.most_common(6))

tup1 = ("abc",2,3)
print(tup1)
print(tup1[0])
print(tup1[:2])

str2 = "Sample     "
print(str2,str2)
