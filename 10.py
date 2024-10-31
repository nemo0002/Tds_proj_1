import pandas as pd
import statsmodels.api as sm

# Load the data
users_df = pd.read_csv('users.csv')

# Define the independent variable (X) and dependent variable (Y)
X = users_df['public_repos']
Y = users_df['followers']

# Add a constant to the independent variable (for the intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(Y, X).fit()

# Get the summary of the regression results
summary = model.summary()

# Extract the coefficient for public_repos
additional_followers_per_repo = model.params['public_repos']

print(f"Regression Results:\n{summary}")
print(f"Estimated additional followers per additional public repository: {additional_followers_per_repo:.3f}")
