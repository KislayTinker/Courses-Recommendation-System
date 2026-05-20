import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
courses_path = BASE_DIR / "data" / "courses.csv"
courses_df = pd.read_csv(courses_path)

# Create combined features
courses_df["combined_features"] = (
    courses_df["category"] + " "
    + courses_df["difficulty"] + " "
    + courses_df["tags"]
)

# TF-IDF Vectorization
tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(
    courses_df["combined_features"]
)

# Course similarity matrix
course_similarity = cosine_similarity(tfidf_matrix)

course_similarity_df = pd.DataFrame(
    course_similarity,
    index=courses_df.index,
    columns=courses_df.index
)

# Streamlit UI
st.title("🎓 Personalized Learning Recommendation System")

st.write("Get personalized course recommendations based on your interests and skill level.")

# User inputs
interest = st.selectbox(
    "Select Your Interest",
    courses_df["category"].unique()
)

skill_level = st.selectbox(
    "Select Your Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# Recommendation function
def recommend_for_new_user(interest, skill_level, top_n=5):

    filtered_courses = courses_df[
        (courses_df["category"] == interest) &
        (courses_df["difficulty"] == skill_level)
    ]

    return filtered_courses.sample(top_n)

# Button
if st.button("Recommend Courses"):

    recommendations = recommend_for_new_user(
        interest,
        skill_level
    )

    st.subheader("Recommended Courses")

    st.dataframe(
        recommendations[
            ["title", "category", "difficulty", "tags"]
        ]
    )