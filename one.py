import pandas as pd

data = {
    "Age": [30, 45, 25, 50],
    "Education Level": ["Graduate", "High School", "Graduate", "Post-Graduate"],
    "Occupation": ["Salaried", "Self-Employed", "Student", "Business"],
    "Household Size": [4, 5, 3, 6],
    "Income": [50000, 40000, 15000, 60000],
    "Location": ["Urban", "Rural", "Urban", "Semi-Urban"],
    "MPCE": [12000, 8000, 5000, 15000]
}

df = pd.DataFrame(data)
df.to_csv("D:/pydev/mpce_data.csv", index=False)
print("CSV file created successfully!")


