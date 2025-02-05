import streamlit as st
import datetime
import time as tm

st.title('Olá, :red[*meu amor*], tudo bem com você?')
st.header('Preciso que :red[*você*] responda a esse questionário, se você errar vamos :red[*terminar*]')
st.markdown('---')

a = st.text_input(label = 'Qual a minha cor favorita?')
st.markdown('---')
b = st.text_input(label = 'Qual minha comida :red[comida] favorita? (bateu vontade de comer lasanha hoje...hmm...)')
st.markdown('---')
c = st.date_input('Quando começamos a ficar?', datetime.date(2025, 2, 5))
st.markdown('---')
pronta = st.text_input(label = 'Ta pronta para ser minha namorada?(escreva em minúsculas)')
if pronta.str.lower() == 'sim':
  certeza = st.text_input(label = 'Tem certeza?(também em minúsculas)')
  if certeza.str.lower() == 'sim':
    st.write('Hmmm, me convenceu, meu amor, vou conferir suas respostas, espera um minutinho')
    time.sleep(2)
    st.write(':red[*ANALIZANDO REPOSTAS*]')
    time.sleep(2)
    st.write(':red[*QUASE PRONTO*]')
    time.sleep(2)
    st.write('Tudo pronto, agora namoramos amor, já que minha cor favorita é',' ', a,'minha comida favorita é',' ', b,'e nos apaixonamos na data de',' ', c,'e justamente por isso vamos namorar e nos casar futuramente')
    st.header(':red[EU TE AMO]')
