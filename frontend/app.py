import streamlit as st
import pandas as pd

# This must be the first Streamlit command
st.set_page_config(page_title="SHL Test Recommender", layout="centered")

# Load CSV
@st.cache_data
def load_data():
    return pd.read_csv("shl_assessments.csv")

df = load_data()

# Streamlit UI
st.title("SHL Test Recommender")
st.write("Welcome! Select options from the sidebar to get started.")

# Sidebar filter
job_role = st.sidebar.selectbox(
    "Select Job Role",
    ["Software Engineer", "Data Analyst", "Product Manager"]
)

# Filter logic (adjust keywords as needed)
role_keywords = {
    "Software Engineer": ["Cognitive", "Programming"],
    "Data Analyst": ["Cognitive", "Data", "Numerical"],
    "Product Manager": ["Cognitive", "Verbal"]
}
keywords = role_keywords[job_role]
filtered_df = df[df['Test Type'].apply(lambda x: any(k in x for k in keywords))]

# Show results
st.subheader("Recommended SHL Tests")

if filtered_df.empty:
    st.warning("No matching tests found.")
else:
    for _, row in filtered_df.iterrows():
        st.markdown(f"### [{row['Name']}]({row['URL']})")
        st.markdown(f"- **Remote Support:** {row['Remote Support']}")
        st.markdown(f"- **Adaptive:** {row['Adaptive']}")
        st.markdown(f"- **Duration:** {row['Duration']}")
        st.markdown(f"- **Test Type:** {row['Test Type']}")
        st.markdown("---")
