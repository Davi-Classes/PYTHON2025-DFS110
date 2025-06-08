import streamlit as st
from db import produtos


def cadastrar_produto(nome, preco, quantidade, categoria):
    if nome == '':
        st.error('O campo nome é obrigatório.')
        return

    if preco <= 0:
        st.error('O preço deve ser maior que 0')
        return
    
    if quantidade < 0:
        st.error('A quantidade deve ser maior ou igual que 0')
        return

    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade,
        'categoria': categoria
    }
    produtos.append(produto)

    st.success('Produto cadastrado com sucesso!')


st.title('Gerencimento de Produtos')


with st.form('cadastrar-produto', clear_on_submit=True) as form:
    nome = st.text_input('Nome', placeholder='Placa de Video RTX 3070')
    preco = st.number_input('Preço')
    quantidade = st.number_input('Quantidade', step=1)
    categoria = st.selectbox(
        'Categoria',
        placeholder='Selecione uma Opção',
        index=None,
        options=['Alimento', 'Informática', 'Higiene', 'Têxtil']
    )

    button = st.form_submit_button('Cadastrar')

    if button:
        cadastrar_produto(nome, preco, quantidade, categoria)