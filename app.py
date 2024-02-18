import pandas as pd
import streamlit as st

import joblib

model = joblib.load("./placement_prediction_model.joblib" )

# Main function to run the Streamlit app
def main():
    st.title('Placement Prediction App')

    # Add input fields
    st.subheader('Enter Student Information')
    age = st.number_input("Age", min_value=0, max_value=100, value=20)
    gender = st.selectbox("Gender", ['Male', 'Female'])
    stream = st.selectbox("Stream", ['Electronics And Communication', 'Computer Science',
       'Information Technology', 'Mechanical', 'Electrical', 'Civil'])
    internships = st.number_input("Internships", min_value=0, max_value=10, value=0)
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=0.0)

    # Predict placement
    if st.button('Predict'):
        input_data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Stream': [stream],
            'Internships': [internships],
            'CGPA': [cgpa]
        })

        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.success("Congratulations! Based on the provided information, the student is likely to be placed.")
        else:
            st.error("Based on the provided information, the student is not likely to be placed.")

if __name__ == '__main__':
    main()
