string = ' xoxo love xoxo   '

# Leading whitepsace are removed
print(string.strip())

print(string.strip(' xoxoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('sti'))

string = 'android is awesome'
print(string.strip('an'))
