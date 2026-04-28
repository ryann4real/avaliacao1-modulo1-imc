import streamlit as st

st.title("Calculadora IMC 📱")
st.subheader("Feito com streamlit ❤️")

altura = st.number_input("Digite sua altura", min_value=0.0)

peso = st.number_input("Digite seu peso", min_value=0.0)

if st.button("Calcular"):
    imc = peso / altura ** 2
    st.success(f"Seu imc é {imc: .2f}")

    if imc < 18.5:
        st.image("https://i.ytimg.com/vi/ydAjWzeSz0s/maxresdefault.jpg")
        st.error("Abaixo do peso ☠️")

    if imc <= 24.9:
        st.image("https://tse1.explicit.bing.net/th/id/OIP.6gB_bdjJ7GygfvaRGIFAIAHaHa?rs=1&pid=ImgDetMain&o=7&rm=3")
        st.info("Seu peso esta perfeito!")

    if imc >= 29.9:
        st.image("https://tse1.mm.bing.net/th/id/OIP.Z47e1SbM_WltJEbb_oEAWQAAAA?rs=1&pid=ImgDetMain&o=7&rm=3")
        st.warning("Acima do peso")  
              
    if imc >= 34.9:
        st.error("Obesidade Grau I")
               
    if imc >= 39.9:
        st.error("Obesidade Grau II")
    
    else:
        print("Obesidade Grau III(Mórbida)")
