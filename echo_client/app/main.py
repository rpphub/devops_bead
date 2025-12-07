import requests
import streamlit as st

SERVER_URL = "http://echo_server:8000/echo"  # docker-compose service esetén
#SERVER_URL = "http://localhost:8000/echo"  # Dev container esetén, illetve lokálisan futtatva
st.set_page_config(page_title="Devops beadandó", page_icon="💬")

# Title
st.markdown("<h1 style='text-align: center;'>Devops beadandó projekt</h1><h2 style='text-align: center;'>Echo chat bot</h2>", unsafe_allow_html=True)
st.markdown("***")


# Chat state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Meglévő üzenetek kirajzolása
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Új üzenet bekérése
user_input = st.chat_input("Írj egy üzenetet...")

if user_input:
    # User üzenet mentése
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Küldés az echo szervernek
    try:
        response = requests.post(SERVER_URL, json={"message": user_input}, timeout=5)
        response.raise_for_status()
        data = response.json()
        echo_text = data.get("echo", "")

    except Exception as e:
        echo_text = f"Hiba történt a szerver hívásakor: {e}"

    # Válasz megjelenítése
    st.session_state.messages.append({"role": "assistant", "content": echo_text})
    with st.chat_message("assistant"):
        st.markdown(echo_text)