# 🎓 Classroom Grade Simulator

A web-based Streamlit application that allows teachers and students to upload marks, simulate final grades, visualize performance, and export reports.

## 🚀 Features

- 📁 Upload CSV of student marks or enter manually
- 📊 Visualize grade distribution with histograms and boxplots
- 📈 View summary statistics (mean, median, etc.)
- 🧮 Simulate final grades based on scoring criteria
- 📝 Download detailed student performance report as CSV

## 📷 Screenshots

<p align="center">
  <img src="screenshots/main_page.png" width="600"/>
  <img src="screenshots/visualization.png" width="600"/>
  <img src="screenshots/statistics.png" width="600"/>
</p>

## 🧠 How It Works

1. Upload your dataset in CSV format with columns like `Name`, `Assignment1`, `Midterm`, `FinalExam`, etc.
2. The app calculates total scores and assigns grades based on:
   - A+: 90–100
   - A : 80–89
   - B : 70–79
   - C : 60–69
   - D : 50–59
   - F : <50
3. You can edit scores manually, and results update live.

## 📦 Installation

```bash
git clone https://github.com/bhanup23/classroom-grade-simulator.git
cd classroom-grade-simulator
pip install -r requirements.txt
streamlit run app.py
