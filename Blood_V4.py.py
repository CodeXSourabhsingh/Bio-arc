import streamlit as st

dict_x = {'O-': ['O-'],
          'O+': ['O+', 'O-'],
          'A-': ['A-', 'O-'],
          'A+': ['A+', 'O+', 'A-', 'O-'],
          'B-': ['B-', 'O-'],
          'B+': ['B+', 'B-', 'O+', 'O-'],
          'AB-': ['AB-','A-','B-','O-'],
          'AB+': ['AB+', 'AB-', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-']
          }
def compatible(donor, recipient):
    return donor in dict_x[recipient]

st.title("Blood Compatibility Checker")
donor = st.selectbox("Donor Blood Type", dict_x.keys())
recipient = st.selectbox("Recipient Blood Type", dict_x.keys())

if st.button("check compatibility"):
    if compatible(donor,recipient):
        st.success(f"{donor} can donate to {recipient}")
    else:
        st.error(f"{donor} cannot donate to {recipient}")\
        