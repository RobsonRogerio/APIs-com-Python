import requests

# Retire os comentários das URLs abaixo para testar os erros

url = "https://httpbin.org/get"  # Código 200: sucesso
# url = "https://httpbin.org/get/pagina-que-nao-existe"  # Código 404: página não encontrada
# url = "https://httpbin.org/post"  # Código 405: método incorreto para a URL

resposta = requests.get(url=url)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Impossível fazer requisição!\nErro: {e}')
else:
    print('Resultado:')
    print(resposta.json())
