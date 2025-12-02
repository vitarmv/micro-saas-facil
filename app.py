import streamlit as st
import google.generativeai as genai

# Título de la App
st.title('🕵️ Detector de Modelos de Gemini')

# --- PON TU CLAVE AQUÍ ABAJO ---
api_key = "AIzaSyDvsWVKPUMFXRDDIbtLQIr9krB5nrs9EtQ"  # <--- BORRA ESTO Y PEGA TU CLAVE REAL ENTRE LAS COMILLAS

if not api_key or api_key == "AIzaSy...":
    st.error("¡Ojo! Te falta poner tu API Key real en el código.")
else:
    # Configuramos la conexión
    genai.configure(api_key=api_key)
    
    st.write("Conectando con Google para ver qué modelos tienes disponibles...")
    
    try:
        # Preguntamos a Google qué modelos existen
        modelos_disponibles = []
        for m in genai.list_models():
            # Buscamos solo los que sirven para generar texto
            if 'generateContent' in m.supported_generation_methods:
                modelos_disponibles.append(m.name)
        
        # Mostramos el resultado
        if modelos_disponibles:
            st.success(f"¡Éxito! Tienes acceso a {len(modelos_disponibles)} modelos:")
            st.code(modelos_disponibles) # Muestra la lista para que puedas copiar el nombre
            
            # Prueba automática con el primer modelo de la lista
            modelo_a_probar = modelos_disponibles[0].replace("models/", "")
            st.info(f"Probando conexión con: {modelo_a_probar}...")
            
            model = genai.GenerativeModel(modelo_a_probar)
            response = model.generate_content("Hola, ¿me escuchas?")
            st.write("Respuesta de la IA:", response.text)
            
        else:
            st.warning("Tu clave funciona, pero Google dice que no tienes modelos disponibles. ¿Quizás es una cuenta nueva sin activar?")
            
    except Exception as e:
        st.error(f"Error de conexión: {e}")
