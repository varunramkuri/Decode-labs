# Tech Career Recommendation System

## About the Project

I built this project to explore how recommendation systems work and how they can be applied to career guidance. The idea is simple: a user provides their technical skills, and the program suggests technology roles that best match those skills.

Instead of using historical user data, the system compares a user's skills with the skills required for different job roles and ranks them based on similarity.

## Objective

The main objective of this project was to understand:

- Content-based recommendation systems
- Text vectorization using TF-IDF
- Similarity measurement using Cosine Similarity
- Data processing with Pandas
- Basic machine learning workflows

## Tools and Libraries

- Python
- Pandas
- Scikit-Learn

## How It Works

### 1. Create a Job Dataset

The project contains a small dataset of technology roles and their associated skills.

Some of the roles included are:

- DevOps Engineer
- Data Engineer
- Cloud Architect
- Frontend Developer
- Backend Developer
- Machine Learning Engineer

### 2. Build a User Profile

The user's skills are collected and combined into a single text string.

Example:

AWS, Terraform, Jenkins, Python, SQL

### 3. Convert Skills into Numerical Data

TF-IDF Vectorization is used to transform both the user profile and job skill descriptions into numerical vectors that can be compared mathematically.

### 4. Calculate Similarity

Cosine Similarity is used to determine how closely the user's skills match each job role.

### 5. Rank Recommendations

All job roles are ranked based on their similarity score, and the top matches are displayed to the user.

## Sample Output

Recommended Career Paths:

- DevOps Engineer
- Cloud Architect
- Data Engineer

The exact ranking depends on the skills provided by the user.

## What I Learned

While working on this project, I gained practical experience with:

- Recommendation system concepts
- Feature extraction using TF-IDF
- Similarity-based ranking
- Working with structured datasets
- Using Scikit-Learn for machine learning tasks

## Future Improvements

Some features I would like to add in future versions:

- User input from the command line
- Larger job-role database
- Resume parsing
- Skill gap analysis
- Learning path recommendations
- Web-based interface

## How to Run

Install the required libraries:

pip install pandas scikit-learn

Run the program:

python tech_recommender.py

## Project Structure

tech_recommender.py
README.md

## Note

This project was created as a learning exercise to better understand recommendation systems and text-based similarity techniques in machine learning.
