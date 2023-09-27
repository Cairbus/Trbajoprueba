import streamlit as st 
from PIL import Image


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



st.video("https://www.youtube.com/watch?v=wohwc9MQt6A&pp=ygUNZXNjbGF2YSByZW1peA%3D%3D")


 edad=st.number_input("Ingresa tu edad",key=int,min_value=0)
if edad==0:
    st.write(" ")
elif edad<20:
    st.error('Todavía no te podemos prestar', icon="🚫")
elif 20<=edad<=25:
    edad="20-25"
elif 26<=edad<=35 :
    edad="26-35"
elif 36<=edad<=45 :
    edad="36-45"
        
elif 46<=edad<=55:
    edad="46-55"
elif 56<=edad<=65:
    edad="56-65"
ingreso_anual=st.number_input("¿Cuánto ganas al año?",min_value=0)
if 0<ingreso_anual<25000:
        ingreso_anual="Bajo"
elif 25000<=ingreso_anual<50000:
        ingreso_anual="Medio-Bajo"
elif 50000<=ingreso_anual<75000:
        ingreso_anual="Medio-Alto"
elif ingreso_anual>=75000:
        ingreso_anual="Alto"
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
tipo_vivienda=st.selectbox('¿En qué tipo de vivienda vives?',('Propia', 'Arrendada', 'Hipotecada'),placeholder="Escoge una opción")
loan_grade=st.selectbox("¿Cuál es tu calificación crediticia?",("A","B","C","D","F"))
anos_empleo=st.number_input("¿Cuántos años llevas en tu trabajo actual?",min_value=0)
