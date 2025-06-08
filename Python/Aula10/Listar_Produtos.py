import streamlit as st
from db import produtos


st.set_page_config(
    page_title='Listagem de Produtos'
)


produtos_formatados = []

for produto in produtos:
    preco_formatado = f'{produto['preco']:.2f}'
    preco_formatado = f'R$ {preco_formatado.replace('.', ',')}'

    produto_formatado = {
        'Nome': produto['nome'],
        'Preço': preco_formatado,
        'Quantidade': produto['quantidade'],
        'Categoria': produto['categoria']
    }
    produtos_formatados.append(produto_formatado)


st.title('Listagem de Produtos')
st.table(produtos_formatados)

ir_para_cadastro = st.button('Ir para o cadastro de produtos')

if ir_para_cadastro:
    st.switch_page('./pages/Cadastrar_Produto.py')