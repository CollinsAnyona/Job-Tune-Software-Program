import sqlite3
from prettytable import PrettyTable

user_name = input("Welcome. Please enter your full names: ")
names = user_name.split()

if len(names) < 2:
    print("You have entered only one name, kindly input at least two names")
    user_name = input("Please enter your full names again: ")

print(" ")
print("Thank you for choosing us. May you continue with the signing in")

# Function to create the table if it doesn't exist
def create_table():
    connection = sqlite3.connect("credentials.db")
    cursor = connection.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_names TEXT,
            skill TEXT,
            graduation_year INTEGER,
            work_experience INTEGER
        )
    """)

    connection.commit()
    connection.close()

# Create the table if it doesn't exist
create_table()

# Function to insert data into the table
def insert_credentials(full_names, skill, graduation_year, work_experience):
    with sqlite3.connect("credentials.db") as connection:
        cursor = connection.cursor()

        # Insert data into the table
        cursor.execute("""
            INSERT INTO credentials (full_names, skill, graduation_year, work_experience)
            VALUES (?, ?, ?, ?)
        """, (full_names, skill, graduation_year, work_experience))

# Get user input for each field
full_names = user_name
skill = input("Enter your skill: ")
print(" ")
graduation_year = input("Enter your graduation year: ")
print(" ")
work_experience = input("Enter your work experience: ")
print(" ")
print("Thank you. Your profile has been created")

# Display the entered credentials using PrettyTable
credentials_table = PrettyTable()
credentials_table.field_names = ["Full Names", "Skill", "Graduation Year", "Work Experience"]
credentials_table.add_row([full_names, skill, graduation_year, work_experience])

print("Credentials entered:")
print(credentials_table)

# Add the user input to the table
insert_credentials(full_names, skill, graduation_year, work_experience)

print("Credentials stored in the database.")


# def match_skills(user_skills, job_skills):
#     """
#     Calculate the similarity score between user skills and job skills.

#     Parameters:
#     - user_skills: List of strings representing user skills.
#     - job_skills: List of strings representing job skills.

#     Returns:
#     - Similarity score (float) between 0 and 1.
#     """
#     common_skills = set(user_skills) & set(job_skills)
#     total_skills = len(set(user_skills) | set(job_skills))

#     similarity_score = len(common_skills) / total_skills if total_skills > 0 else 0
#     return similarity_score

# def find_matching_jobs(user_skills, job_data):
#     """
#     Find and rank job vacancies based on user skills.

#     Parameters:
#     - user_skills: List of strings representing user skills.
#     - job_data: List of dictionaries representing job vacancies, each containing an 'id' and 'skills' field.

#     Returns:
#     - List of tuples (job_id, similarity_score) sorted by descending similarity score.
#     """
#     job_matches = []

#     for job in job_data:
#         job_id = job['id']
#         job_skills = job['skills']

#         similarity_score = match_skills(user_skills, job_skills)
#         job_matches.append((job_id, similarity_score))

#     # Sort job matches by similarity score in descending order
#     sorted_matches = sorted(job_matches, key=lambda x: x[1], reverse=True)
#     return sorted_matches

# # Example data
# user_skills = ["Python", "Data Analysis", "Machine Learning"]
# job_data = [
#     {"id": 1, "skills": ["Python", "Data Analysis", "Statistics"]},
#     {"id": 2, "skills": ["Java", "Web Development", "Database Management"]},
#     {"id": 3, "skills": ["Python", "Machine Learning", "Deep Learning"]},
# ]

# # Find matching jobs
# matching_jobs = find_matching_jobs(user_skills, job_data)

# # Display the results
# print("Matching Jobs:")
# for job_id, similarity_score in matching_jobs:
#     print(f"Job ID: {job_id}, Similarity Score: {similarity_score}")
