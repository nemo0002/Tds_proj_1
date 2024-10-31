import pandas as pd

# Load the data
users_df = pd.read_csv('users.csv')
repositories_df = pd.read_csv('repositories.csv')

# Convert created_at to datetime and filter users who joined after 2020
users_df['created_at'] = pd.to_datetime(users_df['created_at'])
recent_users = users_df[users_df['created_at'] > '2020-01-01']

# Get the logins of recent users
recent_user_logins = recent_users['login'].tolist()

# Filter repositories by these users
recent_repositories = repositories_df[repositories_df['login'].isin(recent_user_logins)]

# Count occurrences of each programming language
language_counts = recent_repositories['language'].value_counts()

# Get the second most popular programming language
second_most_popular_language = language_counts.nlargest(2).index[1]
second_most_popular_count = language_counts.nlargest(2).values[1]

print(f"The second most popular programming language among users who joined after 2020 is: {second_most_popular_language} with {second_most_popular_count} repositories.")