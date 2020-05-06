# Recommended method below:
# n = int(input())
#
# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")
##################################
# advanced method below:

# def wierd(n):
#     if n % 2 == 1 or 6 <= n <= 20:
#         print('Weird')
#     else:
#         print('Not Weird')
#
#
# wierd(int(input()))
##################################
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     # print(f'{a+b},{a-b},{a*b}', sep="\n")
#     print(a+b,a-b,a*b, sep="\n")
##################################

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a//b,a/b,sep="\n")

##################################

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i**2)
##################################
#
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):
#         print(i,end="")
# print(*range(1, n + 1), sep='')
##################################

# if __name__ == '__main__':
#     # x = int(input())
#     # y = int(input())
#     # z = int(input())
#     # n = int(input())
#     # gen = ([i, j, k] for i in range(x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j + k ) != n ))
#     # print(list(gen))
#
#     x, y, z, n = (int(input())
#     for _ in range(4))
#     print([[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n])

##################################
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     uniq_set = set(arr)
#     uniq_list = sorted(uniq_set)
#     print(uniq_list[-2])
#     # perfect way is :
#     # print(sorted(list(set(arr)))[-2])
##################################
# 0
# if __name__ == '__main__':
#     # for _ in range(int(input())):
#     #     name = input()
#     #     score = float(input())
#     # students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#     # name, grade = zip(*students)
#     # min_grade = min(grade)
#     # for name,grade in students:
#     #     print(name,grade)
#     # for name, grade in students:
#     #     print(name[int(min(grade))])
#     # students =[]
#     # for _ in range(int(input())):
#     #     name = input()
#     #     score = float(input())
#     #     students.append([name,score])
#     # print(students)
#     #
#     # max = ['',0]
#     # second_max = ['',0]
#     # for entry in students:
#     #     if entry[1]> max[1]:
#     #         second_max = max
#     #         max = entry
#     #     elif entry[1]>second_max[1]:
#     #         second_max =entry
#     # print(second_max)
#     #
#     # print(max)
#     grade_sheet = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#     # inset = set(grades for name, grades in grade_sheet)
#     # print(inset)
#
#     # second_lowest_val = sorted(list(inset))[1]
#
#     # print('\n'.join(name for name, grades in grade_sheet if (grades==second_lowest_val)))
#
#     # grade_sort = sorted(grade for grade in students)[1]
#     name, grade = zip(*grade_sheet)
#     print(grade)
#     print(sorted(grade))
#     second_lowest_val = sorted(grade)[1]
#     print(second_lowest_val)
#     for name, grades in grade_sheet:
#         if (grades == second_lowest_val):
#             print(name)

##################################



