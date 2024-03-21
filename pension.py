import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import datetime as datetime

# calculate of Member

def calculate_age(date_of_birth):
    today = datetime.today()
    years = today.year - date_of_birth.year
    months = today.month - date_of_birth.month
    if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day):
        years -= 1
        months = 12 + months
    if today.day < date_of_birth.day:
        months -= 1
    if months < 0:
        months += 12
    return years, months

st.title("Pension Benefit Calculator")

# Enter Claimant Information.
st.write("### Enter Claimant's Bio Information")
col1, col2 = st.columns(2)
ss_number = col1.text_input("Social Security Number" ,"")
surname = col1.text_input("Surname" ,"")
firstname = col1.text_input("Firstname" ,"")
emp_name = col1.text_input("Name of Employer" ,"")
pension_option = ["PNDC 247", "ACT 766"]
pension_option_select = col1.selectbox("Select Pension Type",pension_option)
date_of_birth = col2.date_input("Select a date")
if date_of_birth:
    years, months = calculate_age(date_of_birth)
    st.write(f"Age is {years} years and {months} months")
number_of_months = col2.number_input("Number of Months", min_value=1, value=12)
best_first = col2.number_input("First Best Annual Salary", min_value=2400, value=500000)
best_second = col2.number_input("Second Best Annual Salary", min_value=2400, value=500000)
best_third = col2.number_input("Third Best Annual Salary", min_value=2400, value=500000)


