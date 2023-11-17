import streamlit as st
import pickle


model = pickle.load(open('FinalAssignment3.pkl', 'rb'))


st.title('Customer Churn Prediction App')
st.write('Enter customer details here to predict their likelihood of churning.')

# User Input Form
Tenure = st.number_input('Tenure', min_value=0, max_value=100)
MonthlyCharge = st.number_input('Monthly Charge', min_value=0, max_value=500)


gender = st.radio("Gender", ["Male", "Female"])
gender_mapping={"Male":0, "Female:":1}
encoded_gender= gender_mapping[gender]

Partner = st.radio("Does the customer have a partner?", ["Yes", "No"])
Partner_mapping = {"No": 0, "Yes": 1}
encoded_Partner = Partner_mapping[Partner]

MultipleLines = st.radio("Multiple Lines", ["Yes", "No","No Phone Service"])
MultipleLines_mapping = {"No": 0, "No Phone Service": 1, "Yes":2}
encoded_MultipleLines = MultipleLines_mapping[MultipleLines]

InternetService = st.radio("Internet Service", ["DSL", "Fiber Optic","No"])
InternetService_mapping = {"DSL": 0, "Fiber Optic": 1, "No":2}
encoded_InternetService = InternetService_mapping[InternetService]

OnlineSecurity = st.radio("Online Security", ["Yes", "No", "No Internet Service"])
OnlineSecurity_mapping = {"No": 0, "No Internet Service": 1, "Yes":2}
encoded_OnlineSecurity = OnlineSecurity_mapping[OnlineSecurity]

OnlineBackup = st.radio("Online Backup", ["Yes", "No", "No Internet Service"])
OnlineBackup_mapping = {"No": 0, "No Internet Service": 1, "Yes":2}
encoded_OnlineBackup = OnlineBackup_mapping[OnlineBackup]

TechSupport = st.radio("Tech Support", ["Yes", "No", "No Internet Service"])
TechSupport_mapping = {"No": 0, "No Internet Service": 1, "Yes":2}
encoded_TechSupport = TechSupport_mapping[TechSupport]

Contract = st.radio("Contract", ["Month-to-month", "One Year", "Two Year"])
Contract_mapping = {"Month-to-month": 0, "One Year": 1, "Two Year":2}
encoded_Contract = Contract_mapping[Contract]

PaperlessBilling = st.radio("Paperless Billing", ["Yes", "No"])
PaperlessBilling_mapping = {"No": 0, "Yes": 1}
encoded_PaperlessBilling = PaperlessBilling_mapping[PaperlessBilling]

PaymentMethod = st.radio("Payment Method", ["Bank Transfer(automatic)", "Credit Card(automatic)", "Electronic Check", "Mailed Check"])
PaymentMethod_mapping = {"Bank Transfer(automatic)": 0, "Credit Card(automatic)": 1, "Electronic Check":2, "Mailed Check":3}
encoded_PaymentMethod = PaymentMethod_mapping[PaymentMethod]


def predict_likelihood(Tenure, MonthlyCharge, encoded_gender, encoded_Partner, encoded_MultipleLines, encoded_InternetService, encoded_OnlineSecurity, encoded_OnlineBackup, encoded_TechSupport, encoded_Contract, encoded_PaperlessBilling,encoded_PaymentMethod):
    
    
    prediction = model.predict([[Tenure, MonthlyCharge ,encoded_gender, encoded_Partner, encoded_MultipleLines, encoded_InternetService, encoded_OnlineSecurity, encoded_OnlineBackup, encoded_TechSupport, encoded_Contract, encoded_PaperlessBilling,encoded_PaymentMethod]])[0]
    return prediction

if st.button(' Will Customer Churn? Predict'):
    rating = predict_likelihood(Tenure, MonthlyCharge,encoded_gender, encoded_Partner, encoded_MultipleLines, encoded_InternetService, encoded_OnlineSecurity, encoded_OnlineBackup, encoded_TechSupport, encoded_Contract, encoded_PaperlessBilling,encoded_PaymentMethod)
    st.write(f'No:0 Yes:1-- {rating}')



#cd "c:/Users/david/OneDrive - University of Calgary/Desktop/ASHESI/FALL 2023/Intro to AI/Assignments/Assignment 3/"
#streamlit run "Customer Churn Predictor.py"

