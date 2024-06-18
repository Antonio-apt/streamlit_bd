import streamlit as st
import requests
from dotenv import load_dotenv
import os
from urllib.parse import urljoin

load_dotenv()
API_URL = os.getenv("API_URL")

ENDPOINT = urljoin(API_URL, "/handle_user_message")

st.title('WhatsApp AirBnb Assistant')

user_message = st.text_input("Digite sua mensagem:")

if st.button('Enviar'):
    if user_message:
        response = requests.post(ENDPOINT, json={"content": user_message})

        if response.status_code == 200:
            data = response.json()
            st.write(f"Resposta do assistente: {data['response']}")
            st.write(f"ID do Thread: {data['thread_id']}")
        else:
            st.error("Erro ao gerar resposta. Tente novamente.")
    else:
        st.warning("Por favor, digite uma mensagem.")
