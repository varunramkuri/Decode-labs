import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def run_recommendation_engine():
    print("--- BOOTING DIGITAL MATCHMAKER ---")
    
    # Simulating the raw_skills.csv database for Job Roles
    # This acts as our "Item" catalog for Content-Based Filtering
    data = {
        "Job_Role": [
            "DevOps Engineer",
            "Data Engineer",
            "Cloud Architect",
            "Frontend Developer",
            "Backend Developer",
            "Machine Learning Engineer"
        ],
        "Required_Skills": [
            "AWS Docker Kubernetes Jenkins Terraform CI/CD Linux Bash",
            "Python SQL AWS ETL Pipelines Hadoop Spark Airflow Data Warehousing",
            "AWS Azure Google Cloud Terraform Infrastructure Serverless Networking Security",
            "JavaScript React HTML CSS Tailwind Figma UI UX",
            "Java Python Node.js SQL PostgreSQL APIs Microservices",
            "Python TensorFlow PyTorch Pandas Scikit-Learn Deep Learning Math"
        ]
    }
    df = pd.DataFrame(data)
    
    # STEP 1: INGESTION 
    # Capturing the user state with a minimum of 3 inputs to bypass the User Cold Start.
    print("\n[Step 1: Gathering User State...")
    user_skills = ["AWS", "Terraform", "Jenkins", "Python", "SQL"]
    user_profile_string = " ".join(user_skills)
    print(f"User Input Vector: {user_skills}")

    # Vector Mapping: Bridging the language barrier using TF-IDF
    # We fit the vectorizer on the existing job roles, then transform both the jobs and the user profile.
    vectorizer = TfidfVectorizer()
    job_vectors = vectorizer.fit_transform(df['Required_Skills'])
    user_vector = vectorizer.transform([user_profile_string])

    # STEP 2: SCORING
    # Calculating the Cosine Similarity between the user vector and all item vectors.
    print("\n[Step 2: Executing Cosine Similarity Mathematics...")
    similarity_scores = cosine_similarity(user_vector, job_vectors)
    
    # Add the calculated scores to our dataframe for easy manipulation
    df['Match_Score'] = similarity_scores[0]

    # STEP 3: SORTING
    # Organizing the scored dataset in descending order.
    print("[Step 3: Ranking vectors by angular alignment...")
    df_sorted = df.sort_values(by='Match_Score', ascending=False)

    # STEP 4: FILTERING
    # Truncating the output to a "Top-N" list to prevent choice overload.
    N = 3
    print(f"\n[Step 4: Generating Top-{N} Recommendations...\n")
    
    top_matches = df_sorted.head(N)
    
    # Output the final commercial-grade results
    print("=== RECOMMENDED CAREER PATHS ===")
    for index, row in top_matches.iterrows():
        # Formatting the score as a percentage for intuitive reading
        match_percentage = row['Match_Score'] * 100
        print(f"-> {row['Job_Role']} (Match: {match_percentage:.1f}%)")
        print(f"   Relevant Skills: {row['Required_Skills']}\n")

if __name__ == "__main__":
    run_recommendation_engine()