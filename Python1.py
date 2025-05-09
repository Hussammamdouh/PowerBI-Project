import pandas as pd

# Load dataset
df = pd.read_csv('Dataset1.csv') 

# Drop unnecessary columns
df = df.drop(columns=['_id', 'isDeleted', 'image'])

# Handle missing values
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['stock'] = pd.to_numeric(df['stock'], errors='coerce')
df['description'] = df['description'].fillna('No description provided.')

# Fill missing numerical values
df['price'] = df['price'].fillna(df['price'].mean())
df['stock'] = df['stock'].fillna(0)

# Save the cleaned dataset
df.to_csv('clean_dataset1.csv', index=False)

print("✅ clean_dataset1.csv created successfully.")
