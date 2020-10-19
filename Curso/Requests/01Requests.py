import requests

r = requests.get('https://www.google.com/')

n = int(input('1 for dir 2 for help: '))
if n == 1:
    print(dir(r))
elif n == 2:
    print(help(r))
