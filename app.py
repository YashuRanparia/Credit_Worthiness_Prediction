import pickle

import streamlit as st

from model import preprocess


def model_prediction(userdata):

    processed_data = preprocess(userdata)

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    prediction = model.predict(processed_data)[0]

    return prediction
    pass


def main():

    st.title("Credit Application Input")

    status_account = st.selectbox(
    "Status of Existing Checking Account",
    ("A11 : ... <    0 DM", 
     "A12 : 0 <= ... <  200 DM",
     "A13 : ... >= 200 DM / salary assignments for at least 1 year",
     "A14 : no checking account"),
    )
    credit_history = st.selectbox(
        "Credit History", 
        ("A30 : no credits taken/ all credits paid back duly",
         "A31 : all credits at this bank paid back duly",
         "A32 : existing credits paid back duly till now",
         "A33 : delay in paying off in the past",
         "A34 : critical account/  other credits existing (not at this bank)"
         ))
    duration_months = st.number_input("Duration in Months (Attribute 2)", min_value=0)
    credit_amount = st.number_input("Credit Amount (Attribute 5)", min_value=0.0)
    purpose = st.selectbox(
    "Purpose of taking credits",
    ("A40 : car (new)", 
     "A41 : car (used)", 
     "A42 : furniture/equipment", 
     "A43 : radio/television",
     "A44 : domestic appliances",
     "A45 : repairs",
     "A46 : education",
     "A47 : (vacation - does not exist?)",
     "A48 : retraining",
     "A49 : business",
     "A410 : others"),
    )
    savings_account = st.selectbox(
    "Savings account or bonds",
    ("A61 : ... <  100 DM", 
     "A62 : 100 <= ... <  500 DM", 
     "A63 : 500 <= ... < 1000 DM", 
     "A64 : .. >= 1000 DM",
     "A65 : unknown/ no savings account"),
    )
    present_employment = st.selectbox(
    "Present Employment Since", 
    ("A71: Unemployed", 
     "A72 :  ... < 1 year", 
     "A73 : 1  <= ... < 4 years",
     "A74 : 4  <= ... < 7 years",
     "A75 : .. >= 7 years"
     )
    )

    installment = st.number_input("Installment rate in percentage of disposable income", min_value=0.0)

    personal_status = st.selectbox(
    "Personal status and sex", 
    ("A91 : male   : divorced/separated", 
     "A92 : female : divorced/separated/married", 
     "A93 : male   : single",
     "A94 : male   : married/widowed",
     "A95 : female : single"
     )
    )

    guarantors = st.selectbox(
    "Other debtors / guarantors", 
    ("A101 : none", 
     "A102 : co-applicant", 
     "A103 : guarantor",
     )
    )

    residence = st.number_input("Present residence since", min_value=0)

    property = st.selectbox(
    "Property", 
    ("A121 : real estate", 
     "A122 : if not A121 : building society savings agreement/ life insurance", 
     "A123 : if not A121/A122 : car or other, not in attribute 6",
     "A124 : unknown / no property",
     )
    )

    age = st.number_input("Age (Attribute 13)", min_value=18)

    other_installment_plans = st.selectbox(
    "Other installment plans", 
    ("A141 : bank", 
     "A142 : stores", 
     "A143 : none"
     )
    )

    housing = st.selectbox("Housing Situation", ("A151 : Rent", "A152 : Own", "A153 : For Free"))

    existing_credits_this_bank = st.number_input("Number of existing credits at this bank", min_value=0)

    job = st.selectbox(
    "Job", 
    ("A171 : unemployed/ unskilled  - non-resident", 
     "A172 : unskilled - resident", 
     "A173 : skilled employee / official",
     "A174 : management/ self-employed/highly qualified employee/ officer",
     )
    )

    dependents = st.number_input("Number of people being liable to provide maintenance for", min_value=0)

    telephone = st.selectbox(
    "Telephone", 
    ("A191 : none", 
     "A192 : yes, registered under the customers name", 
     )
    )

    foreign_worker = st.selectbox(
    "Do have Foreign Workers ?", 
    ("A201 : yes", 
     "A202 : no", 
     )
    )

    userdata = {
        'Attribute1': status_account.split(' ')[0],
        'Attribute2': duration_months,
        'Attribute3': credit_history.split(' ')[0],
        'Attribute4': purpose.split(' ')[0],
        'Attribute5': credit_amount,
        'Attribute6': savings_account.split(' ')[0],
        'Attribute7': present_employment.split(' ')[0],
        'Attribute8': installment,
        'Attribute9': personal_status.split(' ')[0],
        'Attribute10': guarantors.split(' ')[0],
        'Attribute11': residence,
        'Attribute12': property.split(' ')[0],
        'Attribute13': age,
        'Attribute14': other_installment_plans.split(' ')[0],
        'Attribute15': housing.split(' ')[0],
        'Attribute16': existing_credits_this_bank,
        'Attribute17': job.split(' ')[0],
        'Attribute18': dependents,
        'Attribute19': telephone.split(' ')[0],
        'Attribute20': foreign_worker.split(' ')[0]
    }

    if st.button('Predict'):

        if model_prediction(userdata) == 1:
            prediction = 'Good'
        else:
            prediction = 'Bad'

        show_prediction = st.text(prediction)
        
        pass


if __name__ == "__main__":
    main()