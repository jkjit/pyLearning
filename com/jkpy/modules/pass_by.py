import timeit

print(timeit.timeit('for n in filter(lambda n: n % 2 == 0, nums): n', setup = 'nums = [1,2,3,4,5,6,7,8,9]'))

print(timeit.timeit('for n in (n for n in nums if n % 2 == 0): n', setup = 'nums = [1,2,3,4,5,6,7,8,9]'))

