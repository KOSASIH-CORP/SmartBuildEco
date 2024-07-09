import streamlit as st

st.title("Augmented Reality Model Generation")

ar_model_id = st.text_input("AR Model ID")
ar_model_type = st.text_input("AR Model Type")
data = st.text_area("AR Model Data")

if st.button("Generate"):
    ar_model = {"id": ar_model_id, "type": ar_model_type, "data": data}
    ar_model = ar_api.generate_ar_model(ar_model)
    st.write("Generated AR Model:", ar_model)
