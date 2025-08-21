import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Student Budget Planner", layout="wide")

st.title("📊 Student Budget Planner")
st.write("Plan, track, and manage your monthly allowance efficiently!")

# -----------------------------
# Data Storage
# -----------------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Category", "Amount", "Type"])

# -----------------------------
# Input Section
# -----------------------------
st.header("➕ Add Income / Expense")

col1, col2, col3 = st.columns(3)

with col1:
    category = st.text_input("Category (e.g., Food, Rent, Travel)")
with col2:
    amount = st.number_input("Amount (₹)", min_value=0, step=100)
with col3:
    type_choice = st.selectbox("Type", ["Income", "Expense"])

if st.button("Add Entry"):
    if category and amount > 0:
        new_entry = {"Category": category, "Amount": amount, "Type": type_choice}
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_entry])], ignore_index=True)
        st.success(f"Added {type_choice}: {category} ₹{amount}")
    else:
        st.warning("Please enter a valid category and amount.")

# -----------------------------
# Budget Summary
# -----------------------------
st.header("📌 Monthly Summary")

if not st.session_state.data.empty:
    income = st.session_state.data[st.session_state.data["Type"] == "Income"]["Amount"].sum()
    expenses = st.session_state.data[st.session_state.data["Type"] == "Expense"]["Amount"].sum()
    savings = income - expenses

    st.metric("Total Income", f"₹{income}")
    st.metric("Total Expenses", f"₹{expenses}")
    st.metric("Savings", f"₹{savings}")

    if savings < 0:
        st.error("⚠️ You are over budget! Please review your expenses.")

    # -----------------------------
    # Category Analysis
    # -----------------------------
    st.subheader("📊 Category-wise Analysis")
    expense_data = st.session_state.data[st.session_state.data["Type"] == "Expense"]

    if not expense_data.empty:
        fig1, ax1 = plt.subplots()
        ax1.pie(expense_data["Amount"], labels=expense_data["Category"], autopct="%1.1f%%")
        st.pyplot(fig1)

        st.bar_chart(expense_data.set_index("Category")["Amount"])

    # -----------------------------
    # Financial Goal
    # -----------------------------
    st.subheader("🎯 Financial Goal")
    goal = st.number_input("Set a savings goal (₹)", min_value=0, step=500)
    if goal > 0:
        if savings >= goal:
            st.success(f"🎉 Congratulations! You reached your savings goal of ₹{goal}.")
        else:
            st.warning(f"💡 You need ₹{goal - savings} more to reach your goal.")

    # -----------------------------
    # Export Report
    # -----------------------------
    st.subheader("📤 Export Monthly Report")
    csv = st.session_state.data.to_csv(index=False).encode("utf-8")
    st.download_button("Download Report (CSV)", data=csv, file_name="monthly_budget.csv", mime="text/csv")

else:
    st.info("No records yet. Add your income and expenses above ⬆️")
