import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Inject Custom CSS for styling
st.markdown(
    """
    <style>
    /* Page Background */
    .stApp {
        background-color: #f8f9fa !important;
    }

    /* Sidebar Background */
    section[data-testid="stSidebar"] {
        background-color: #e3e3e3 !important;
    }

    /* Input Fields */
    input, select, textarea {
        background-color: #e8f0fe !important;
        color: black !important;
        border-radius: 5px !important;
        padding: 8px !important;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #4CAF50 !important; /* Green */
        color: white !important;
        font-size: 16px !important;
        padding: 10px 24px !important;
        border-radius: 8px !important;
        border: none !important;
    }

    /* Dataframe Table */
    .stDataFrame {
        background-color: #ffffff !important;
        color: black !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Success Message */
    .stAlert {
        background-color: #d4edda !important;
        color: #155724 !important;
        padding: 10px !important;
        border-radius: 8px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to read students data from Excel
def read_students_from_excel():
    try:
        return pd.read_excel("students.xlsx")
    except FileNotFoundError:
        return pd.DataFrame(columns=["id", "name", "age", "grade"])

# Function to save students data to Excel
def save_students_to_excel(df):
    df.to_excel("students.xlsx", index=False)

# Function to add a student
def add_student_to_excel(name, age, grade):
    df = read_students_from_excel()
    new_student = pd.DataFrame({"id": [len(df) + 1], "name": [name], "age": [age], "grade": [grade]})
    df = pd.concat([df, new_student], ignore_index=True)
    save_students_to_excel(df)

# Streamlit UI
st.title("Student Management System")
operation = st.sidebar.selectbox("Select Operation", ["Add Student", "Update Student", "Delete Student", "Grade Analysis"])

if operation == "Add Student":
    st.header("Add Student")
    with st.form(key="student_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=100)
        grade = st.selectbox("Grade", ["A", "B", "C", "D", "F"])
        submit_button = st.form_submit_button(label="Add Student")
    if submit_button:
        add_student_to_excel(name, age, grade)
        st.success(f"Student {name} added successfully!")

elif operation == "Update Student":
    st.header("Update Student")
    students_df = read_students_from_excel()
    if not students_df.empty:
        student_ids = students_df["id"].tolist()
        student_id_to_update = st.selectbox("Select Student to Update", student_ids)
        with st.form(key="update_form"):
            new_name = st.text_input("New Name")
            new_age = st.number_input("New Age", min_value=1, max_value=100)
            new_grade = st.selectbox("New Grade", ["A", "B", "C", "D", "F"])
            update_button = st.form_submit_button(label="Update Student")
        if update_button:
            students_df.loc[students_df["id"] == student_id_to_update, ["name", "age", "grade"]] = new_name, new_age, new_grade
            save_students_to_excel(students_df)
            st.success(f"Student with ID {student_id_to_update} updated successfully!")
    else:
        st.warning("No students found!")

elif operation == "Delete Student":
    st.header("Delete Student")
    students_df = read_students_from_excel()
    if not students_df.empty:
        student_ids = students_df["id"].tolist()
        student_id_to_delete = st.selectbox("Select Student to Delete", student_ids)
        if st.button("Delete Student"):
            students_df = students_df[students_df["id"] != student_id_to_delete]
            save_students_to_excel(students_df)
            st.success(f"Student with ID {student_id_to_delete} deleted successfully!")
    else:
        st.warning("No students found!")

elif operation == "Grade Analysis":
    st.header("Grade Analysis")
    students_df = read_students_from_excel()
    
    if not students_df.empty:
        # Count occurrences of each grade
        grade_counts = students_df["grade"].value_counts()

        # Create a bar chart
        fig, ax = plt.subplots()
        grade_counts.plot(kind="bar", color=["#4CAF50", "#FF9800", "#F44336", "#2196F3", "#9C27B0"], ax=ax)
        ax.set_xlabel("Grade")
        ax.set_ylabel("Number of Students")
        ax.set_title("Grade Distribution")

        # Display the chart in Streamlit
        st.pyplot(fig)
    else:
        st.warning("No students found!")

# Display Student List
st.header("Student List")
students_df = read_students_from_excel()
if not students_df.empty:
    st.dataframe(students_df)
else:
    st.info("No students available. Please add a student.")
