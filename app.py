import streamlit as st

st.title("Calculadora IMC 📱")
st.subheader("Feito com streamlit ❤️")

altura = st.number_input("Digite sua altura", min_value=0.0)

peso = st.number_input("Digite seu peso", min_value=0.0)

if st.button("Calcular"):
    imc = peso / altura ** 2
    st.success(f"Seu imc é {imc: .2f}")

    if imc < 18.5:
        st.error("Abaixo do peso ☠️")

    if imc <= 24.9:
        st.info("Seu peso esta perfeito!")

    if imc >= 29.9:
        st.warning("Acima do peso")  
              
    if imc >= 34.9:
        st.error("Obesidade Grau I")
               
    if imc >= 39.9:
        st.error("Obesidade Grau II")
    
    else:
        print("Obesidade Grau III(Mórbida)")
