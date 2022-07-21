import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#load the saved model

model=pickle.load(open( 'C:/Users/Srivatsan/OneDrive/Documents/d/disease.sav','rb'))

st.title("Parkinson Disease Predictor")

#Enter input types



col1, col2 = st.columns(2)  
    
with col1:
    Fo=st.text_input("MDVP:Fo(Hz)")
with col2:
    fhi=st.text_input("MDVP:Fhi(Hz)")
with col1:
    flo=st.text_input("MDVP:Flo(Hz)")  
with col2:  
    jitter=st.text_input("MDVP:Jitter(%)")
with col1:
    shimmer=st.text_input("MDVP:Shimmer")
with col2:
    HNR=st.text_input("HNR")
with col1:
    RPDE=st.text_input("RPDE")
with col2:
    DFA=st.text_input("DFA")
with col1:
    spread1=st.text_input("spread1")
with col2:
    spread2=st.text_input("spread2")
with col1:
    d2=st.text_input("D2")


# code for Prediction
parkinsons_diagnosis = ''

# creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    parkinsons_prediction = model.predict([[Fo, fhi, flo,jitter,shimmer, HNR,RPDE,DFA,spread1,spread2,d2]])                          
    
    if (parkinsons_prediction[0] == 1):
      parkinsons_diagnosis = "The person has Parkinson's disease"
    else:
      parkinsons_diagnosis = "The person does not have Parkinson's disease"
    
st.success(parkinsons_diagnosis)
