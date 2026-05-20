# 🎓 Hybrid Personalized Learning Recommendation System

A Data Science project that recommends personalized learning courses to college students using a **Hybrid Recommendation System** combining:

- Collaborative Filtering
- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity

The project also includes an interactive **Streamlit Web Application** for real-time course recommendations.

---

# 🚀 Features

✅ Personalized course recommendations  
✅ Hybrid recommendation engine  
✅ User-based collaborative filtering  
✅ Content-based filtering using TF-IDF  
✅ Cold-start handling for new users  
✅ Precision@K evaluation  
✅ Interactive Streamlit UI  
✅ Custom synthetic dataset generation  

---

# 🧠 Recommendation Techniques Used

## 1️⃣ Collaborative Filtering

Recommends courses based on:
- Similar users
- User-item interaction patterns
- User ratings

### Techniques Used
- User-Item Matrix
- Cosine Similarity

---

## 2️⃣ Content-Based Filtering

Recommends courses based on:
- Course tags
- Category
- Difficulty level

### Techniques Used
- TF-IDF Vectorization
- Cosine Similarity

---

## 3️⃣ Hybrid Recommendation System

Combines:
- Collaborative Filtering
- Content-Based Filtering

to improve:
- Personalization
- Recommendation quality
- Cold-start handling

---

# 📊 Dataset

Custom-generated dataset containing:

## courses.csv

| Column | Description |
|---|---|
| course_id | Unique course ID |
| title | Course title |
| category | Course domain |
| difficulty | Beginner / Intermediate / Advanced |
| tags | Course-related skills |

---

## users.csv

| Column | Description |
|---|---|
| user_id | Unique user ID |
| interest | Preferred domain |
| skill_level | User learning level |

---

## ratings.csv

| Column | Description |
|---|---|
| user_id | User ID |
| course_id | Course ID |
| rating | User rating (1–5) |

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

---

# 📈 Evaluation Metrics

The recommendation system is evaluated using:

## Precision@K
Measures how many recommended courses are actually relevant to the user.

## Recall@K
Measures how many relevant courses were successfully discovered by the recommender.

---

# 🧊 Cold Start Problem Handling

For new users with no rating history:
- The system uses user interests and skill level
- Content-based filtering is used initially

This improves recommendation quality for first-time users.

---

# 🌐 Streamlit Web Application

The application allows users to:
- Select interests
- Choose skill level
- Receive personalized course recommendations instantly

---

# 📁 Project Structure

```bash
recommendation_project/
│
├── app/
│   └── app.py
│
├── data/
│   ├── courses.csv
│   ├── users.csv
│   └── ratings.csv
│
├── notebooks/
│   └── recommendation_system.ipynb
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
cd recommendation_project
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Streamlit App

```bash
streamlit run app/app.py
```

---

# 🎯 Future Improvements

- Deep Learning-based Recommendation System
- Matrix Factorization / SVD
- Real-time User Ratings
- User Authentication
- Course Popularity Trends
- Cloud Deployment
- Recommendation Explanation System

---

# 📸 Screenshots



---

# 📌 Resume Project Title

**Hybrid Personalized Learning Recommendation System using Collaborative and Content-Based Filtering**

---

# 👨‍💻 Author

Kinshu  
Data Science Enthusiast
