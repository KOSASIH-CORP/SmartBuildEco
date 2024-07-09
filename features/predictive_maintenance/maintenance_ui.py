import streamlit as st

st.title("Predictive Maintenance")

equipment_id = st.text_input("Equipment ID")
equipment_type = st.text_input("Equipment Type")
location = st.text_input("Location")
sensor_data = st.text_area("Sensor Data")

if st.button("Predict"):
    equipment = {"id": equipment_id, "type": equipment_type, "location": location, "sensor_data": sensor_data}
    prediction = maintenance_api.predict_maintenance(equipment)
    st.write("Predicted Maintenance Needs:", prediction)
