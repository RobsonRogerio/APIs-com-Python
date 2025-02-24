import requests

url = 'http://www.google.com'

resposta = requests.get(url)

print(resposta, end="\n\n\n\n\n")
print(resposta.text)

with open('pagina_google.html', 'w') as arquivo:
    arquivo.write(resposta.text)

