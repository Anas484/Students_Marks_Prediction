import streamlit as st
import pandas as pd
import pickle
import numpy as np

df = pd.read_csv(r'C:\Users\anas1\OneDrive\Desktop\ML\Student_Performance_Predictor\Cleaned_student_performance')
model = pickle.load(open(r"Student_Performance_Predictor\student_performance_predictor_Model.pkl",'rb'))
st.title("Student Marks predictor")

hours_studied = st.number_input("Hours Studied", value=None, placeholder="Type a number...")
st.text("")
attendance = st.number_input("Attendance (0 to 100)", value=None, placeholder="Type a number...")
st.text("")
sleep = st.number_input("Sleeping Hours", value=None, placeholder="Type a number...")
st.text("")
parent_inv = st.selectbox(label="Parental Involvement",options=df['Parental_Involvement'].unique())
st.text("")
access_resource = st.selectbox(label="Resource Access",options=df['Access_to_Resources'].unique())
st.text("")
col1, col2,col3,col4 = st.columns(4)
with col1:
    ex_activity = st.radio(label="Extracurricular Activities",options=df['Extracurricular_Activities'].unique())
with col2:
    internet = st.radio(label="Internet Access",options=df['Internet_Access'].unique())
with col3:
    s_type = st.radio(label="School Type",options=df['School_Type'].unique())
with col4:
    gender = st.radio(label="Gender",options=df['Gender'].unique()) 


sorted_options = sorted(df['Physical_Activity'].unique())
st.text("")
col5, col6 = st.columns(2)
with col5:
    tutoring = st.number_input("Tutoring Hours", value=None, placeholder="Type a number...")
with col6:
    p_activity = st.number_input("Physical Activity Hours", value=None, placeholder="Type a number...")

st.text("")
col7, col8,col9 = st.columns(3)

with col7:
    f_income = st.radio(label="Family Income",options=df['Family_Income'].unique())
with col8:
    t_quality = st.radio(label="Teacher Quality",options=df['Teacher_Quality'].unique())
with col9:
     disable = st.radio(label="Learning Disabilities",options=df['Learning_Disabilities'].unique())
     
st.text("")
if st.button(label="Predict"):
    input_data = pd.DataFrame([[hours_studied,attendance,parent_inv,access_resource,ex_activity,sleep,internet,tutoring,f_income,t_quality,s_type,p_activity,disable,gender]],
                 columns=['Hours_Studied','Attendance','Parental_Involvement','Access_to_Resources','Extracurricular_Activities','Sleep_Hours',
                               'Internet_Access','Tutoring_Sessions','Family_Income','Teacher_Quality','School_Type','Physical_Activity',
                               'Learning_Disabilities','Gender'])
    
    prediction = model.predict(input_data)
    rounded_prediction = int(prediction[0])

    st.markdown(f"### Predicted Exam Scores is:  {rounded_prediction}")