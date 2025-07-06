🎓 Classroom Grade Simulator
A web-based Streamlit application that allows teachers and students to upload, simulate, or manually enter student grades, visualize performance, and export reports.
🚀 Features

📁 Upload a CSV with student grades (columns: Student, Grade)
✍️ Manually enter grades for a custom number of students
🎲 Simulate grades using normal or uniform distributions
📊 Visualize grade distribution with histograms and boxplots
📈 View summary statistics (mean, median, standard deviation, pass percentage)
🧮 Simulate final grades based on a hypothetical score
📝 Download a detailed student performance report as CSV

📷 Screenshots



Note: Screenshots are placeholders. Replace with actual images of the app.
🧠 How It Works

Choose an Input Method:
Upload CSV: Upload a CSV file with columns Student (e.g., "Student 1") and Grade (numeric, 0–100).
Manual Entry: Enter grades for a specified number of students using sliders.
Simulate Grades: Generate random grades for a specified number of students using normal (mean, std dev) or uniform (min, max) distributions.


The app calculates and displays:
A table of grades (up to 10 rows for performance).
Visualizations (histogram and boxplot).
Statistics (mean, median, standard deviation, pass percentage ≥40).


Simulate a final grade based on a hypothetical score with the following criteria:
A: ≥90
B: ≥75
C: ≥60
D: ≥40
F: <40


Download the grade data as a CSV report.

📋 Prerequisites

Python 3.8 or higher
A modern web browser (e.g., Chrome, Firefox)
Dependencies listed in requirements.txt

📦 Installation

Clone the repository:
git clone https://github.com/bhanup23/classroom_grade_simulator.git
cd classroom_grade_simulator


(Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Run the Streamlit app:
streamlit run app.py


Open your browser at http://localhost:8501.


📝 Sample CSV Format
Student,Grade
Student 1,85.5
Student 2,92.0
Student 3,78.3

🛠️ Troubleshooting

Slow Performance: For large datasets (>1000 rows), the app may slow down. Limit the number of students or use a smaller CSV.
Missing Dependencies: Ensure all libraries are installed (streamlit, pandas, numpy, matplotlib, seaborn). Run pip install -r requirements.txt.
Port Conflict: If localhost:8501 is in use, specify a different port: streamlit run app.py --server.port 8502.
CSV Errors: Ensure the uploaded CSV has Student and Grade columns with valid numeric grades (0–100).

