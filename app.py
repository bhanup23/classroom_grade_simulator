import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cache data generation to avoid recomputation
@st.cache_data
def generate_grades(num_students, dist_type, mean=70, std=10, low=50, high=90):
    if dist_type == "Normal":
        grades = np.random.normal(mean, std, num_students)
    else:  # Uniform
        grades = np.random.uniform(low, high, num_students)
    grades = np.clip(grades, 0, 100)
    return pd.DataFrame({
        "Student": [f"Student {i+1}" for i in range(num_students)],
        "Grade": grades.round(2)
    })

# Cache plot generation to avoid recomputation
@st.cache_data
def plot_histogram(grades):
    fig, ax = plt.subplots()
    sns.histplot(grades, bins=10, kde=False, ax=ax, color='skyblue')  # Disable kde for speed
    ax.set_title("Grade Distribution Histogram")
    return fig

@st.cache_data
def plot_boxplot(grades):
    fig, ax = plt.subplots()
    sns.boxplot(x=grades, ax=ax, color='orange')
    ax.set_title("Grade Boxplot")
    return fig

# Set page config
st.set_page_config(page_title="Classroom Grade Simulator", layout="wide")
st.title("🎓 Classroom Grade Simulator")

# Sidebar options
st.sidebar.header("📥 Input Options")
input_method = st.sidebar.radio("Select Input Method:", ["Upload CSV", "Manual Entry", "Simulate Grades"])

# Input methods
df = None
if input_method == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload Grade CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
elif input_method == "Manual Entry":
    num_students = st.sidebar.slider("Number of Students", 5, 50, 10)
    grades = []
    for i in range(num_students):
        grade = st.sidebar.slider(f"Student {i+1} Grade", 0, 100, 75, key=f"grade_{i}")
        grades.append(grade)
    df = pd.DataFrame({"Student": [f"Student {i+1}" for i in range(num_students)], "Grade": grades})
elif input_method == "Simulate Grades":
    num_students = st.sidebar.slider("Number of Students", 10, 100, 30)  # Reduced max for performance
    dist_type = st.sidebar.selectbox("Distribution Type", ["Normal", "Uniform"])
    if dist_type == "Normal":
        mean = st.sidebar.slider("Mean", 40, 100, 70)
        std = st.sidebar.slider("Standard Deviation", 1, 20, 10)  # Reduced max std
        df = generate_grades(num_students, dist_type, mean=mean, std=std)
    else:
        low = st.sidebar.slider("Min Grade", 0, 100, 50)
        high = st.sidebar.slider("Max Grade", 50, 100, 90)
        df = generate_grades(num_students, dist_type, low=low, high=high)

# Main section
if df is not None:
    st.subheader("📊 Grade Data")
    # Display only first 10 rows to reduce rendering time
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("📈 Grade Distribution")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Histogram")
        fig_hist = plot_histogram(df['Grade'])
        st.pyplot(fig_hist)

    with col2:
        st.write("Boxplot")
        fig_box = plot_boxplot(df['Grade'])
        st.pyplot(fig_box)

    st.subheader("📐 Statistics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Mean", f"{df['Grade'].mean():.2f}")
    col2.metric("Median", f"{df['Grade'].median():.2f}")
    col3.metric("Std Dev", f"{df['Grade'].std():.2f}")
    col4.metric("Pass % (>=40)", f"{(df['Grade'] >= 40).mean() * 100:.2f}%")

    st.subheader("🎯 Grade Simulation")
    st.markdown("Enter a hypothetical final score to simulate final grade:")
    sim_score = st.slider("Simulated Final Score", 0, 100, 80)
    st.write(f"If your final score is **{sim_score}**, your grade could be:")
    if sim_score >= 90:
        st.success("Grade: A")
    elif sim_score >= 75:
        st.info("Grade: B")
    elif sim_score >= 60:
        st.warning("Grade: C")
    elif sim_score >= 40:
        st.error("Grade: D")
    else:
        st.error("Grade: F")

    # Download section
    st.subheader("⬇️ Download Report")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name='classroom_grades.csv',
        mime='text/csv'
    )
else:
    st.warning("👈 Please upload or generate grade data to begin.")
