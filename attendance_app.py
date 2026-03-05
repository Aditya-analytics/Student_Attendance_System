import streamlit as st
import pandas as pd
import os
from datetime import date

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Smart Attendance", page_icon="🎓", layout="wide")

st.title("🎓 Smart Student Attendance System")

# -------------------------------
# Ensure CSV files exist
# -------------------------------
if not os.path.exists("students.csv"):
    open("students.csv", "w").close()

if not os.path.exists("attendance.csv"):
    open("attendance.csv", "w").close()

# -------------------------------
# Sidebar Menu
# -------------------------------
menu = st.sidebar.selectbox(
    "📌 Menu",
    [
        "➕ Add Students",
        "👨‍🎓 View Students",
        "📷 Mark Attendance",
        "📊 View Attendance",
        "🚪 Exit"
    ]
)

# ===================================
# ➕ ADD STUDENTS
# ===================================

if menu == "➕ Add Students":

    st.header("➕ Add Student")

    with st.container():

        col1, col2 = st.columns(2)

        with col1:
            roll_no = st.text_input("🆔 Student Roll Number")

        with col2:
            name = st.text_input("👤 Student Name")

        department = st.text_input("🏫 Department")

        if st.button("Add Student"):

            file = open("students.csv", "a")
            file.write(roll_no + "," + name + "," + department + "\n")
            file.close()

            st.success("✅ Student Added Successfully!")

# ===================================
# 👨‍🎓 VIEW STUDENTS
# ===================================

elif menu == "👨‍🎓 View Students":

    st.header("👨‍🎓 Student List")

    try:
        df = pd.read_csv("students.csv", names=["Roll No","Name","Department"])

        search = st.text_input("🔍 Search Student")

        if search:
            df = df[df["Name"].str.contains(search, case=False)]

        st.dataframe(df, use_container_width=True)

    except:
        st.warning("⚠ No Students Found")

# ===================================
# 📷 MARK ATTENDANCE
# ===================================

elif menu == "📷 Mark Attendance":

    st.header("📷 Mark Attendance")

    try:
        df = pd.read_csv("students.csv", names=["Roll No","Name","Department"])

        roll_no = st.selectbox("Select Roll Number", df["Roll No"])

        status = st.radio(
            "Attendance Status",
            ["Present","Absent"]
        )

        if st.button("Start Attendance"):

            file = open("attendance.csv","a")
            file.write(str(roll_no) + "," + status + "," + str(date.today()) + "\n")
            file.close()

            st.success("✅ Attendance Marked Successfully")

    except:
        st.warning("⚠ Add Students First")

# ===================================
# 📊 VIEW ATTENDANCE
# ===================================

elif menu == "📊 View Attendance":

    st.header("📊 Attendance Records")

    try:
        df = pd.read_csv("attendance.csv", names=["Roll No","Status","Date"])

        filter_date = st.date_input("📅 Filter by Date")

        if filter_date:
            df = df[df["Date"] == str(filter_date)]

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download Attendance CSV",
            csv,
            "attendance.csv",
            "text/csv"
        )

    except:
        st.warning("⚠ No Attendance Records")

# ===================================
# 🚪 EXIT
# ===================================

elif menu == "🚪 Exit":

    st.header("🚪 Exit")

    st.success("💜 Thank you for using the Smart Attendance System!")