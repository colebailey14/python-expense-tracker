import streamlit as st
import pandas as pd
import os

# CSV file to store expenses
CSV_FILE = "expenses.csv"

# Load existing expenses or create new DataFrame
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=["Name", "Amount", "Category"])

st.title("Python Expense Tracker 💰")

# Form to add new expense
with st.form("add_expense_form"):
    name = st.text_input("Expense Name")
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Other"])
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_row = {"Name": name, "Amount": amount, "Category": category}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        st.success(f"Expense '{name}' added successfully!")

# Display all expenses
st.subheader("All Expenses")
st.dataframe(df)

# Display total
total = df["Amount"].sum() if not df.empty else 0
st.write(f"**Total Expenses:** ${total:.2f}")
