import requests

r = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')

print(r.status_code)

# Caso o retorno seja 200: Sucesso
# Caso o retorno seja 300: Redirecionamento
# Caso o retorno seja 400: Erro do cliente
# Caso o retorno seja 500: Erro do server

print(r.ok)

# O retorno deste comando será True ou False, sendo que True significa que o request foi executado com sucesso, e False
# Significa que há um problema com o request

print(r.headers)

# Vai retornar uma série de informações uteis para se usar
