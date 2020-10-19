import requests

r = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')

with open('02RequestsImage.png', 'wb') as f:
    f.write(r.content)
