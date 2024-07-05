import streamlit as st
import requests
import os

st.title("Asistente generador de bienestar emocional")
# Campo de entrada para la consulta
consulta = st.text_area("Describe la situacion que te gustaria gestionar:")

# Selección múltiple de tu estilo de vida
categoria =["Familia", "Amigos", "Arte", "Lectura", "Naturaleza", "Música", "Deporte", "Espiritualidad", "Calma", "Tecnología", "Mascotas"]
categoria_seleccionada = st.selectbox("Selecciona un elemento acorde con tu estilo de vida:", categoria)

if st.button('Enviar consulta'):
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
            
          
            result = response.json()
            st.markdown('### Resultado de la solicitud:')
            st.markdown(result['answer'])
      
      st.write("¡Recuerda siempre buscar apoyo profesional si necesitas mas ayuda!")
      st.write("¡Gracias por usar la aplicación! ¡Hasta luego!")
