import csv
from datetime import datetime

# List to store users from Austin
users_in_austin = []

# Read the CSV file
try:
    with open('users.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Process each row
        for row in reader:
            location = row['location'].strip().lower()
            
            # Check if the user is from Austin
            if 'austin' in location:
                try:
                    created_at = datetime.strptime(row['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                    users_in_austin.append({
                        'login': row['login'],
                        'created_at': created_at
                    })
                except ValueError as e:
                    print(f"Error parsing date for {row['login']}: {e}")
except FileNotFoundError:
    print("The file 'users.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Sort users based on created_at in ascending order
sorted_users = sorted(users_in_austin, key=lambda x: x['created_at'])

# Extract the top 5 earliest user logins
top_5_earliest_logins = [user['login'] for user in sorted_users[:5]]

# Print the result as a comma-separated list
if top_5_earliest_logins:
    print(','.join(top_5_earliest_logins))
else:
    print("No users found from Austin.")
