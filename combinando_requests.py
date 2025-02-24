import requests

def pegar_ids_estados():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    params = {
        'view': 'nivelado'
        }
    dados_estados = fazer_request(url=url, params=params)
    dict_estado = {}
    for dados in dados_estados:
        id_estado = dados['UF-id']
        nome_estado = dados['UF-nome']
        dict_estado[id_estado] = nome_estado
    return dict_estado

def pegar_frequencia_nome_por_estado(nome):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    params = {
        'groupBy': 'UF',
        }
    dados_frequencias = fazer_request(url=url, params=params)
    dict_frequencias = {}
    for dados in dados_frequencias:
        id_estado = int(dados['localidade'])
        frequencia = dados['res'][0]['proporcao']
        dict_frequencias[id_estado] = frequencia
    return dict_frequencias

def fazer_request(url, params=None):
    resposta = requests.get(url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        resultado = None
    else:
        resultado = resposta.json()
    return resultado

def main(nome):
    try:
        dict_estados = pegar_ids_estados()
        dict_frequencia = pegar_frequencia_nome_por_estado(nome)
        print(f'Frequência do nome {nome} nos estados (por 100.000 habitantes)')
        for id_estado, nome_estado in dict_estados.items():
            frequencia_estado = dict_frequencia[id_estado]
            print(f'-> {nome_estado}: {frequencia_estado}')
    except:
        print('''\nO nome consultado não consta na base de dados do IBGE.\n 
        Quando a quantidade de ocorrências for suficientemente pequena a ponto de permitir a identificação delas,
        o IBGE não informa essa quantidade. No caso da API de Nomes, a quantidade mínima de ocorrências para que
        seja divulgado os resultados é de 10 por município, 15 por Unidade da Federação e 20 no Brasil\n''')

if __name__ == '__main__':
    main('rubia')