import requests
import streamlit as st
import pandas as pd

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

def pegar_nome_por_decada(nome):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    dados_decadas = fazer_request(url=url)
    if not dados_decadas:
        return {}
    dict_decadas = {}
    for dados in dados_decadas[0]['res']:
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decadas[decada] = quantidade
    return dict_decadas

def main():
    st.title('Web App Nomes')
    st.write('Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2#api-_)')
    nome = st.text_input('Consulte um nome: ')
    if not nome:
        st.stop()

    dict_decadas = pegar_nome_por_decada(nome)
    if not dict_decadas:
        st.warning(
        '''\nO nome consultado não consta na base de dados do IBGE.\n 
            Quando a quantidade de ocorrências for suficientemente pequena a ponto de não permitir a identificação delas,
    o IBGE não informa essa quantidade. No caso da API de Nomes, a quantidade mínima de ocorrências para que
    seja divulgado os resultados é de 10 por município, 15 por Unidade da Federação e 20 no Brasil\n'''
        )
        st.stop()

    df = pd.DataFrame.from_dict(dict_decadas, orient='index')

    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.write('Frequência por década')
        col1 = st.dataframe(df)
    with col2:
        st.write('Evolução ao longo do tempo')
        col2 = st.line_chart(df)

if __name__ == '__main__':
    main()