import streamlit as st 
from PIL import Image
from streamlit_option_menu import option_menu

st.title("Credit Risk Score \n :red[By Analizadores de Realidades]")

st.markdown("""
            <style>
            .e1nzilvr1 {
                text-align: center;
            }
            
            .e1nzilvr5 p {
                text-align:center;
                font:bold;
                font-size:20px;
            }
            
            </style>
            """, unsafe_allow_html= True
    
)

with st.sidebar:
    selected = option_menu("BIENVENIDOS", ["Video Tutorial", 'Ingresa tus datos'], 
        icons=['film projector', 'clipboard'], menu_icon="house", default_index=1)
    selected

if selected=="Video Tutorial":
    st.write(
        "En la era digital actual, comprender y gestionar tu salud financiera es más crucial que nunca. "
        "Camilo Andrés Granada Mejía, estudiante de ingeniería administrativa, y Alejandro Zapata Quintero, "
        "estudiante de ingeniería de sistemas, nos complacemos en presentar 'Credit Score', tu puerta de acceso a "
        "un conocimiento profundo de tu historial crediticio."
    )

    st.write(
        "Nuestra plataforma ha sido cuidadosamente diseñada con el propósito de simplificar el proceso de evaluación "
        "crediticia. ¿Te preguntas cuál es tu score crediticio? ¿Cómo impacta en tus posibilidades financieras? Estamos "
        "aquí para proporcionarte respuestas claras y valiosas."
    )

    st.write(
        "Gracias a la combinación de la experiencia en ingeniería administrativa y de sistemas, hemos creado una herramienta "
        "intuitiva que te permite ingresar tus datos financieros de manera segura y obtener un análisis instantáneo de tu score "
        "crediticio. No importa si eres estudiante, profesional o empresario, 'Credit Score' está aquí para empoderarte con "
        "información precisa y útil sobre tu salud crediticia."
    )

    st.write(
        "Descubre la clave para tomar decisiones financieras informadas. Únete a nosotros en 'Credit Score' y da el primer paso "
        "hacia un futuro financiero más sólido. ¡Tu éxito financiero comienza aquí!"
    )
    st.video("https://www.youtube.com/watch?v=33wNNT4QXSk")
    
    st.caption(
        "**Tratamiento de Datos en Cumplimiento con la Ley Colombiana**\n\n"
        "En 'Credit Score', nos tomamos en serio la privacidad y seguridad de tus datos. "
        "En cumplimiento con la legislación colombiana, especialmente la Ley Estatutaria 1581 de 2012, "
        "reguladora del derecho fundamental de habeas data y otras disposiciones, garantizamos un tratamiento "
        "transparente y responsable de la información que compartes con nosotros."
    )

elif selected=="Ingresa tus datos" :
    edad=st.number_input("Ingresa tu edad",key=int,min_value=0)
    income=st.number_input("¿Cuánto ganas al año?",min_value=0)
    monto_credito=st.number_input("Ingresa el valor del crédito deseado",min_value=0)
    if 0<monto_credito<=5000:
        monto_credito="Pequeño"
    elif 5000<monto_credito<=10000:
        monto_credito="Mediano"
    elif 10000<monto_credito<=15000:
        monto_credito="Grande"
    elif monto_credito>15000:
        monto_credito="Muy Grande"
        
    interes_deseado=st.number_input("¿A qué tasa de interés deseas tomarlo?",key=float,min_value=0.0)
    home=st.selectbox('¿En qué tipo de vivienda vives?',('Propia', 'Arrendada', 'Hipotecada'),placeholder="Escoge una opción")
    loan_grade=st.selectbox("¿Cuál es tu calificación crediticia?",("A","B","C","D","F"))
    anos_empleo=st.number_input("¿Cuántos años llevas en tu trabajo actual?",min_value=0)
    
    
    if home=="Propia":
            home="OWN"
    elif home=="Arrendada":
            home="RENT"
    def score(edad, home, income):
            score = 0
            
            if 20 <=edad < 22:
                score = score + 100
            elif 22 <= edad < 26:
                score = score + 120
            elif 26 <= edad < 29:
                score = score + 185
            elif 29 <= edad < 32:
                score = score + 200
            elif 32 <= edad < 37:
                score = score + 210
            elif 37 <= edad < 42:
                score = score + 225
            else:
                score = score + 250
                
            if home == 'OWN':
                score = score + 225
            elif home == 'RENT':
                score = score + 110
            else:
                score = score + 0
                
            if income < 10000:
                score = score + 120
            elif 10000 <= income < 17000:
                score = score + 140
            elif 17000 <= income < 28000:
                score = score + 180
            elif 28000 <= income < 35000:
                score = score + 200
            elif 35000 <= income < 42000:
                score = score + 225
            elif 42000 <= income < 58000:
                score = score + 230
            else:
                score = score + 260
            
            return score
    score_final=score(edad,home,income)
    if st.button("Calcular mi Score"):
        import time
        with st.spinner('Calculando meticulosamente...'):
            time.sleep(5)
        st.info(f"Tu Credit Scores es de: {score_final} ")
    st.caption(
        "**Tratamiento de Datos en Cumplimiento con la Ley Colombiana**\n\n"
        "En 'Credit Score', nos tomamos en serio la privacidad y seguridad de tus datos. "
        "En cumplimiento con la legislación colombiana, especialmente la Ley Estatutaria 1581 de 2012, "
        "reguladora del derecho fundamental de habeas data y otras disposiciones, garantizamos un tratamiento "
        "transparente y responsable de la información que compartes con nosotros."
    )
