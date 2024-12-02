import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier


st.write("""
    Penguin Prediction App
    This app predicts penguin species
         """)

st.sidebar.header('User Input Features')

uploaded_file=st.sidebar.file_uploader("upload your csv file",type=['csv'])
if uploaded_file is not None:
    input_df=pd.read_csv(uploaded_file) #if there is a uploaded file thrn read the file. else just take features externally
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
        sex=st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm=st.sidebar.slider('Bill length (mm)',32.1,59.6,43.9)
        bill_depth_mm=st.sidebar.slider('Bill depth (mm)',13.1,21.5,17.2)
        flipper_length_mm=st.sidebar.slider('flipper length (mm)',172.0,231.0,201.0)
        body_mass_g=st.sidebar.slider('Body mass (g)',2700.0,6300.0,4207.0)

        data={'island':island,
              'bill_length_mm':bill_length_mm,
              'sex':sex,
              'bill_depth_mm':bill_depth_mm,
              'flipper_length_mm':flipper_length_mm,
              'body_mass_g':body_mass_g
              }
        features=pd.DataFrame(data,index=[0])
        return features
    input_df=user_input_features()


penguins_raw=pd.read_csv('penguins_cleaned.csv')
penguins=penguins_raw.drop(columns=['species'])
df=pd.concat([input_df,penguins],axis=0)

#encoding of features
encode=['sex','island']
for col in encode:
    dummy=pd.get_dummies(df[col],prefix=col)
    df=pd.concat([df,dummy],axis=1)
    del df[col]

df=df[:1] # select only the first row


st.subheader('user input features')
st.write(df)


try:
    with open('C:\Users\Dell\Desktop\Data Science\StreamLit tutorial\Tutorial\Streamlit again\Second\penguin\penguins_clf.pkl', 'rb') as file:
        load_clf = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'penguins_clf.pkl' not found. Please ensure the file is in the correct directory.")


prediction=load_clf.predict(df)
prediction_proba=load_clf.predict_proba(df)


st.subheader('prediction')
penguins_species=np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])


st.subheader('Prediction Probability')
st.write(prediction_proba)
