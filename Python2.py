import pandas as pd

# Load dataset
df = pd.read_csv('Dataset2.csv')

# Fill missing values in selected columns
columns_to_fill = [
    'CoffeeHouse',
    'CarryAway',
    'RestaurantLessThan20',
    'Restaurant20To50'
]

for col in columns_to_fill:
    df[col] = df[col].fillna('unknown')

# Save the cleaned dataset
df.to_csv('clean_dataset2.csv', index=False)

print("✅ clean_dataset2.csv created successfully.")
