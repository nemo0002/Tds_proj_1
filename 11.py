import pandas as pd

# Load the data
repositories_df = pd.read_csv('repositories.csv')


# Calculate the correlation directly
correlation = repositories_df['has_projects'].astype(int).corr(repositories_df['has_wiki'].astype(int))

print(f"The correlation between having projects enabled and having a wiki enabled is: {correlation:.3f}")
