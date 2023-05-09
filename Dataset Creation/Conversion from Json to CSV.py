import pandas as pd

# Create the list of CSV file names to be read
csv_files = ["part1.csv", "part2.csv", "part3.csv"]

final_csv = pd.DataFrame()

# Loop through each file in the csv_files list
for file in csv_files:
    
    # Read the CSV file and store it in a temporary DataFrame named df_temp
    df_temp = pd.read_csv(file, index_col=0)
    
    # Append the temporary DataFrame to the final_csv DataFrame
    final_csv = final_csv.append(df_temp, ignore_index=True)
    
    
# Drop any duplicate rows from the final_csv DataFrame
df = final_csv.drop_duplicates()

# Export the resulting DataFrame to a new CSV file named "urls.csv"

df.to_csv("urls.csv", index=False, index_label="urls")

