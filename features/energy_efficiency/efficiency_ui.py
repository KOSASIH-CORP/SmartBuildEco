import streamlit as st

st.title("Energy Efficiency Optimization")

building_id = st.text_input("Building ID")
building_type = st.text_input("Building Type")
location = st.text_input("Location")
energy_usage = st.text_area("Energy Usage Data")

if st.button("Optimize"):
    building = {"id": building_id, "type": building_type, "location": location, "energy_usage": energy_usage}
    optimization = efficiency_api.optimize_energy_efficiency(building)
    st.write("Optimized Energy Efficiency:", optimization)
