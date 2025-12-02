import streamlit as st
import google.generativeai as genai
import os

# Configuración de página
st.set_page_config(page_title="Generador Micro-SaaS", page_icon="🚀")

st.title('🚀 Generador de Emails con IA')

# Recuperar la clave desde los Secretos de Streamlit Cloud
api_key = "AIzaSyACFXvIogwxvHETsvf0ub9XHXdtin_3W50"

if not api_key:
    st.error("No se encontró la API Key. Configúrala en los secretos.")
else:
    # Configurar Gemini
    genai.configure(api_key=api_key)

    # Interfaz
    producto = st.text_area("Describe tu producto o servicio:", height=150)

    if st.button('Generar Email de Venta'):
        if not producto:
            st.warning("Por favor escribe algo sobre tu producto.")
        else:
            with st.spinner('La IA está escribiendo...'):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    prompt = f"Actúa como un experto en copywriter. Escribe un email de ventas corto y persuasivo para este producto: {producto}"
                    response = model.generate_content(prompt)
                    st.success("¡Email Generado!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Ocurrió un error: {e}")
