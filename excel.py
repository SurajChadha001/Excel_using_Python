import pandas as pd
data = {
    'Name': ['John','Anna','Peter','Joe'],
    'Age': [28,35,42,29],
    'City': ['New York','Paris','London','Stockholm']
}
df=pd.DataFrame(data)

file_path = 'example.xlsx'

df.to_excel(file_path, index=False)

print("Excel file has been created successfully")