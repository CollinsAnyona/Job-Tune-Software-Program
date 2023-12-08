import json
import sqlite3
from prettytable import PrettyTable
from companies_data import companies

def check_profile():
    existing_profile = input("Are you a new user? (yes/no): ").lower()

    if existing_profile == "yes":
        create_profile()
    elif existing_profile == "no":
        continue_profile()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        check_profile()

def continue_profile():
    print("Welcome back! Let's continue with your profile.")

def create_profile():
    print("Let's create a new profile for you")
    print(" ")
    # Get name of the user and reject if the name is only one
    user_name = input("Please enter your full names: ")
    names = user_name.split()

    if len(names) < 2:
        print("You have entered only one name, kindly input at least two names")
        user_name = input("Please enter your full names again: ")

    print(" ")
    print(f"Thank you {user_name} for choosing us. May you continue with the signing in")

    # Display available industries and prompt the user to choose
    def display_industries():
        industries_list = [
            {"id": 1, "name": "Agricultural Industry"},
            {"id": 17, "name": "Technology Industry"},
            {"id": 16, "name": "Automobile and Accessories"},
            {"id": 4, "name": "Financial Industry"},
            {"id": 15, "name": "Commercial and Professional Services"},
            {"id": 13, "name": "E-commerce and Retail Industry"},
            {"id": 10, "name": "Energy and Environment Resources"},
            {"id": 9, "name": "Travel and Leisure Industry"},
            {"id": 8, "name": "Construction and Real Estate"},
            {"id": 7, "name": "Health and Beauty"},
            {"id": 6, "name": "Hotels, Lodges, and Tourism Industry"},
            {"id": 5, "name": "Services Industry"},
            {"id": 4, "name": "Home and Office Furniture"},
            {"id": 3, "name": "Foodstuff and Beverages"},
            {"id": 2, "name": "Electricals and Electronics"},
        ]

        print("The following are the available Industries:")
        print(" ")
        for industry in industries_list:
            print(f"ID: {industry['id']}, Name: {industry['name']}")

        while True:
            try:
                user_industry_id = int(input("Enter the ID of the industry you are interested in: "))
                if any(industry['id'] == user_industry_id for industry in industries_list):
                    break
                else:
                    print("Invalid ID. Please enter a valid ID from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric ID.")

        return user_industry_id
    user_industry_id = display_industries()

# Get name of the user and reject if the name is only one
user_name = input("Welcome. Please enter your full names: ")
names = user_name.split()

if len(names) < 2:
    print("You have entered only one name, kindly input at least two names")
    user_name = input("Please enter your full names again: ")

print(" ")
print(f"Thank you {user_name} for choosing us. May you continue with the signing in")

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
user_career = input("Enter your career/professional background: ")
print(" ")
user_skills_input = input("Enter your skills separated by commas (enter at least one skill): ")
print(" ")
while True:
    try:
        graduation_year = int(input("Enter your graduation year: "))
        break  # Break the loop if the input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter a valid number for graduation year.")

print(" ")

while True:
    try:
        work_experience = int(input("Enter your work experience: "))
        break  # Break the loop if the input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter a valid number for work experience.")

print(" ")
print("Thank you. Your profile has been created")

# Display the entered credentials using PrettyTable
credentials_table = PrettyTable()
credentials_table.field_names = ["Full Names", "Skill", "Graduation Year", "Work Experience"]
credentials_table.add_row([full_names, user_career, graduation_year, work_experience])

print("These are the credentials entered:")
print(credentials_table)

# Add the user input to the table
insert_credentials(full_names, user_career, graduation_year, work_experience)

print("Credentials stored in the database.")

# Read data from the JSON file
with open('companies.json', 'r') as json_file:
    companies = json.load(json_file)

def match_skills(user_skills, job_skills):
    """
    Calculate the similarity score between user skills and job skills.

    Parameters:
    - user_skills: List of strings representing user skills.
    - job_skills: List of strings representing job skills.

    Returns:
    - Similarity score (float) between 0 and 1.
    """
    common_skills = set(user_skills) & set(job_skills)
    total_skills = len(set(user_skills) | set(job_skills))

    similarity_score = len(common_skills) / total_skills if total_skills > 0 else 0
    return similarity_score

def find_matching_jobs(user_skills, job_data, company_data):
    """
    Find and rank job vacancies based on user skills.

    Parameters:
    - user_skills: List of strings representing user skills.
    - job_data: List of dictionaries representing job vacancies, each containing an 'id' and 'skills' field.

    Returns:
    - List of tuples (job_id, similarity_score) sorted by descending similarity score.
    """
    job_matches = []

    for job in job_data:
        job_id = job['id']
        job_skills = [skill.lower() for skill in job['skills']]
        company_name = next((company['name'] for company in company_data if company['id'] == job_id), f"Unknown Company {job_id}")

        similarity_score = match_skills(user_skills, job_skills)
        job_matches.append((company_name, job_id, similarity_score))

    # Sort job matches by similarity score in descending order
    sorted_matches = sorted(job_matches, key=lambda x: x[2], reverse=True)
    return sorted_matches

# Split the input into a list of skills
user_skills = [skill.strip().lower() for skill in user_skills_input.split(",")]
with open("industries_data.json", "r") as f:
    industries_skills = json.load(f)

job_data = industries_skills
company_data = companies

# Find matching jobs
matching_jobs = find_matching_jobs(user_skills, job_data, company_data)

# Display the results
print("Matching Jobs:")
found_match = False

for company_name, job_id, similarity_score in matching_jobs:
    if similarity_score > 0.1:  # Adjust the threshold as needed
        print(f"Congratulations! {company_name}  company of Job ID {job_id} is a strong match for your skills with a similarity score of {similarity_score:.2f}")
        found_match = True
        break
    elif similarity_score > 0.01:
        print(f"{company_name}  company of Job ID {job_id} seems to be a good match for your skills with a similarity score of {similarity_score:.2f}")
        found_match = True
        break
if not found_match:
        print("Your skills do not match any of the available vacancies. You may leave your email for upcoming opportunities")
