import streamlit as st

st.title("Material Analysis")

material_id = st.text_input("Material ID")
material_type = st.text_input("Material Type")
properties = st.text_area("Material Properties")

if st.button("Analyze"):
    material = {"id": material_id, "type": material_type, "properties": properties}
    analysis = material_api.analyze_material(material)
    st.write("Material Analysis:", analysis)
