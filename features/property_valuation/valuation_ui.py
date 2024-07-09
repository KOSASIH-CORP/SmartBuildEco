import streamlit as st

st.title("Property Valuation")

address = st.text_input("Address")
city = st.text_input("City")
state = st.text_input("State")
zip = st.text_input("Zip")
price = st.number_input("Price")

if st.button("Valuate"):
    property = {"address": address, "city": city, "state": state, "zip": zip, "price": price}
    valuation = valuation_api.valuate_property(property)
    st.write("Estimated Valuation:", valuation)
