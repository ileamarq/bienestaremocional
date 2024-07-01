import streamlit as st
import requests
import os

st.title("Asistente generador de bienestar emocional")
# Campo de entrada para la consulta
consulta = st.text_area("Necesito que me ayudes a controlar:")

# Selección múltiple para mejorar la vida
categoria = ["Familia", "Amigos", "Arte", "Lectura", "Naturaleza", "Música", "Autoestima", "Espiritualidad", "Calma", "Tecnología", "Mascota"]
categoria_seleccionada = st.selectbox("Selecciona un elemento para mejorar tu vida:", categoria)

if st.button('Enviar consulta'):
      st.write(consulta)

# Botón para enviar la solicitud HTTP POST
base_url = "https://api.dify.ai/v1"
path = "/completion-messages"
my_secret = os.environ['DIFY_APP_KEY']

headers = {
"Authorization": f"Bearer {my_secret}",
"Content-Type": "application/json"
}

data = {
"inputs": {
"query": consulta,
"categoria": categoria_seleccionada
},

    "response_mode": "blocking",
    "user": "Buscador de bienestar emocional"
    }

url_completa = "https://api.dify.ai/v1/completion-messages" 


response = requests.post(f'{base_url}{path}', json=data, headers=headers)
    # Mostrar el resultado
if response.status_code == 200:
      st.success('Consulta enviada con exito')
      st.json(response.json())
    
result = response.json()
st.markdown('### Resultado de la solicitud:')
st.markdown(result['answer'])

st.write("¡Recuerda siempre buscar apoyo profesional si necesitas mas ayuda!")
st.write("¡Gracias por usar la aplicación! ¡Hasta luego!")
