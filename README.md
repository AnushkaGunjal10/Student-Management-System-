📘 Student Management System
A Streamlit-based web application that allows users to manage student records, including adding, updating, deleting students, and performing grade analysis with a bar chart visualization.

📌 Features
✅ Add Student – Enter student details (Name, Age, Grade) and store them in an Excel file.
✅ Update Student – Modify existing student details like Name, Age, and Grade.
✅ Delete Student – Remove a student from the database.
✅ Grade Analysis – Visualize the distribution of student grades using a bar chart.
✅ Data Persistence – Stores student records in an Excel file (students.xlsx).
✅ Styled UI – Custom CSS for an enhanced user interface.

🚀 Tech Stack
Python
Streamlit (for UI)
Pandas (for data handling)
Matplotlib (for graph visualization)
Excel (.xlsx) (for data storage)
📂 Project Structure
bash
Copy
Edit
📁 Student-Management-System
│── 📄 app.py               # Main Python file to run the app
│── 📄 students.xlsx         # Excel file to store student records (Auto-created)
│── 📄 README.md            # Project Documentation
🛠️ Setup & Installation
1️⃣ Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/Student-Management-System.git
cd Student-Management-System
2️⃣ Install Dependencies

bash
Copy
Edit
pip install streamlit pandas openpyxl matplotlib
3️⃣ Run the Application

bash
Copy
Edit
streamlit run app.py
4️⃣ Open in Browser
Once the server starts, the app will open automatically.
If not, go to http://localhost:8501 in your browser.

📊 How to Use
1️⃣ Add Student
Navigate to "Add Student" from the sidebar.
Enter Name, Age, and Grade.
Click "Add Student" to save.
2️⃣ Update Student
Navigate to "Update Student".
Select a Student ID from the dropdown.
Enter new details and click "Update Student".
3️⃣ Delete Student
Navigate to "Delete Student".
Select a Student ID and click "Delete Student".
4️⃣ Grade Analysis
Navigate to "Grade Analysis".
A bar chart will be displayed showing the distribution of grades.
🖼️ Screenshots
📌 Main Dashboard

📌 Grade Analysis Graph

📝 To-Do List
🔹 Add more data visualization (e.g., student performance trends).
🔹 Implement database support (e.g., MySQL instead of Excel).
🔹 Deploy using Streamlit Cloud or Heroku.

🤝 Contributing
Contributions are welcome!

Fork the repo
Create a new branch
Make changes & submit a PR
🛡️ License
This project is open-source and free to use.
