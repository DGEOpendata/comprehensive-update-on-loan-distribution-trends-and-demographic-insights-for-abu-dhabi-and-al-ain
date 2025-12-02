python
import pandas as pd
from datetime import datetime

# Load the original dataset
original_data = pd.read_csv('Loan_Distribution_2007.csv')

# Function to update dataset with new data
def update_dataset(existing_data, new_data):
    # Concatenate the existing and new data
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    # Sort the data by approval year
    updated_data.sort_values(by='approval_year', inplace=True)
    return updated_data

# Simulate new data
new_data = pd.DataFrame({
    'loan_amount': [150000, 250000],
    'project_location': ['Abu Dhabi', 'Al Ain'],
    'approval_year': [2023, 2023],
    'sector': ['Technology', 'Healthcare'],
    'subsector': ['Software Development', 'Biotech'],
    'education_level': ['Bachelor', 'Masters'],
    'employment_status': ['Employed', 'Self-employed'],
    'gender': ['Male', 'Female'],
    'year_of_birth': [1990, 1985]
})

# Update the dataset
updated_data = update_dataset(original_data, new_data)

# Save the updated dataset
updated_data.to_csv('Updated_Loan_Distribution.csv', index=False)
print("Dataset updated successfully.")
