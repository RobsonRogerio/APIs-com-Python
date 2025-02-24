# Nosso primeiro request GET
import requests

url = "https://httpbin.org/get"
resposta = requests.get(url=url)

print(resposta.json())

print('-----')


# Exemplo de request POST
import requests

url = "https://httpbin.org/post"
data = {
    "meus_dados": [1, 2, 3],
    "pessoa": {
        "nome": "Juliano",
        "professor": True,
    }
}
resposta = requests.post(url=url, data=data)

print(resposta.json())

print('-----')


# Exemplo de request GET com parâmetros
import requests

url = "https://httpbin.org/get"
params = {
    "dataInicio": "2023-01-01",
    "dataFim": "2023-12-31",
}
resposta = requests.get(url=url, params=params)

print(resposta.json())

print('-----')


# Exemplo de request POST com parâmetros
import requests

url = "https://httpbin.org/post"
data = {
    "meus_dados": [1, 2, 3],
    "pessoa": {
        "nome": "Juliano",
        "professor": True,
    }
}
params = {
    "dataInicio": "2023-01-01",
    "dataFim": "2023-12-31",
}
resposta = requests.post(url=url, data=data, params=params)

print(resposta.json())
