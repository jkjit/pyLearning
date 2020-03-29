import sys

import sysconfig

print('path names')
for path in sys.path:
    print(path)

print('Printing sysconfig scheme names line by line here')

for path in sysconfig.get_scheme_names():
    print(path)
# sysconfig.get_platform()
