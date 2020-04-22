import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)

if r.status_code !=200:
    print (' GET/tasks is returning error code : {}'.format(r.status_code))

print(r.text)


response = requests.get('https://developer.github.com/v3', auth=('user','pass'))

response = requests.get('https://api.github.com/users/octocat/orgs')

print(response.text)
# dictionary1 = r.text

# if dictionary1.("http")
#     print("Yes it is")

# response = requests.get(dictionary1.get(documentation_url))
"""
response = requests.get('http://google.com')

print(response.status_code)
print(response.text)
"""
