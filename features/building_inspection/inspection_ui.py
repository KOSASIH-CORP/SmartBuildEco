import streamlit as st

st.title("Building Inspection")

building_id = st.text_input("Building ID")
building_type = st.text_input("Building Type")
location = st.text_input("Location")
inspection_data = st.text_area("Inspection Data")

if st.button("Inspect"):
    building = {"id": building_id, "type": building_type, "location": location, "inspection_data": inspection_data}
    inspection = inspection_api.inspect_building(building)
    st.write("Building Inspection:", inspection)
