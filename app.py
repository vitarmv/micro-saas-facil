import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="Generador Micro-SaaS", page_icon="🚀")
st.title('🚀 Generador de Emails de Venta')

# --- TU CLAVE API ---
# (Recuerda: al ser público en GitHub, úsalo para probar y luego bórralo si quieres privacidad)
api_key = "AIzaSyDvsWVKPUMFXRDDIbtLQIr9krB5nrs9EtQ" 

if not api_key or api_key == "TU_CLAVE_AIza_AQUI":
    st.error("⚠️ Por favor, edita el código y pon tu API Key real donde dice 'TU_CLAVE_AIza_AQUI'.")
else:
    try:
        # 1. Configuramos la conexión
        genai.configure(api_key=api_key)

        # 2. Creamos el campo para el usuario
        producto = st.text_area("Describe tu producto o servicio:", height=150, placeholder="Ejemplo: Un curso de cocina vegana para principiantes...")

        # 3. El Botón Mágico
        if st.button('✨ Generar Email'):
            if not producto:
                st.warning("Por favor escribe algo sobre tu producto.")
            else:
                with st.spinner('La IA está escribiendo tu email...'):
                    # --- AQUÍ ESTÁ EL CAMBIO CLAVE ---
                    # Usamos 'gemini-2.0-flash' que sí está en tu lista y es rápido
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    prompt = f"""
                    Actúa como un experto copywriter de ventas.
                    Escribe un email frío, corto y persuasivo para vender este producto: {producto}.
                    Usa un asunto llamativo. El tono debe ser profesional pero cercano.
                    """
                    
                    response = model.generate_content(prompt)
                    
                    st.success("¡Email Generado!")
                    st.markdown(response.text)

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")