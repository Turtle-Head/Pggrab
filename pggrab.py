# Written by: James Fehr
# Date: 2023-08-02
# Purpose: To connect to a PostgreSQL database and extract data from it
# Database connection parameters
import os
import csv
import psycopg2

# Database connection parameters
# Modify these to match your database
db_params = {
    "host": "your_host",
    "database": "your_database",
    "user": "your_user",
    "password": "your_password"
}

# Get user input for CSV file name
csv_filename = input("Enter CSV file name (without .csv extension): ")

# Establish a connection
connection = psycopg2.connect(**db_params)

# Create a cursor
cursor = connection.cursor()

# Execute a SQL query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch the data
data = cursor.fetchall()

# Close the cursor and the connection
cursor.close()
connection.close()

# Determine the path for the Downloads folder
downloads_folder = os.path.expanduser("~") + "/Downloads/"

# Create the CSV file path
csv_file_path = os.path.join(downloads_folder, csv_filename + ".csv")

# Write data to CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow([desc[0] for desc in cursor.description])
    # Write data rows
    csv_writer.writerows(data)

print(f"CSV file '{csv_filename}.csv' has been saved in the Downloads folder.")
