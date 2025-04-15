import pandas as pd
import numpy as np

print("✅ Libraries imported successfully!\n")

print("📥 Reading dataset...")
df = pd.read_csv("students.csv")

#Data Functions
print("\n🔎 First 5 records:")
print(df.head())

print("Shape(R,C):", df.shape)   

print("Columns:", df.columns)   

print("Statistics:")
print(df.describe())  


#Extract Example: Get math scores as NumPy array
math_scores = np.array(df['math score'])
print("Average Math Score:", np.mean(math_scores))

# Cleaning example
# 1. Check for missing values
print("\n🔍 Checking for missing values:")
print(df.isnull().sum())

# 2. Drop rows with any missing values
df_clean = df.dropna()
print(f"\n🧼 Rows after dropping missing values: {df_clean.shape[0]}")

# 3. Remove duplicates
df_clean = df_clean.drop_duplicates()
print(f"🧽 Rows after dropping duplicates: {df_clean.shape[0]}")

#Transformation
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Filter: students with average score > 75
top_students = df[df['average_score'] > 75]

print(top_students.head())