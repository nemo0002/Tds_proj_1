import pandas as pd

# Load the data
users_df = pd.read_csv('users.csv')

# Calculate the correlation between followers and public repositories
correlation = users_df['followers'].corr(users_df['public_repos'])

print(f"The correlation between the number of followers and the number of public repositories is: {correlation:.3f}")
