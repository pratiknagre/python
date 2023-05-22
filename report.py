import pandas as pd

# Prepare the data
data = {
    'Name': ['John', 'Jane', 'Mike'],
    'Age': [30, 25, 35],
    'City': ['New York', 'London', 'Paris']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Generate the report
report_file = 'report.xlsx'
sheet_name = 'Report'

with pd.ExcelWriter(report_file) as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Report generated and saved as '{report_file}'.")
