pip install pandas
import pandas as pd
df = pd.read_csv("data.csv")
print(df)
df = pd.read_excel("data.xlsx")
print(df)
df = pd.read_json("data.json")
print(df)
filtered = df[df["Age"] > 25]
print(filtered)
filtered = df[df["Salary"] >= 40000]
print(filtered)
filtered = df[(df["Age"] > 25) & (df["Salary"] > 40000)]
print(filtered)
filtered = df[(df["Age"] < 25) | (df["Salary"] > 45000)]
print(filtered)
