import streamlit as st

st.title("Climate Resilience Analysis")

building_id = st.text_input("Building ID")
building_type = st.text_input("Building Type")
location = st.text_input("Location")
climate_data = st.text_area("Climate Data")

if st.button("Analyze"):
    building = {"id": building_id, "type": building_type, "location": location, "climate_data": climate_data}
    analysis = resilience_api.analyze_climate_resilience(building)
    st.write("Climate Resilience Analysis:", analysis)
