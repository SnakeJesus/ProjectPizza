# Import required modules
import os
import django

# Set up environment variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

# Connect to the database
import mysql.connector

conn = mysql.connector.connect(
    host='your_host',
    user='headChef',
    password='1234',
    database='PizzaDB'
)

# Use the connection to perform a database query
cursor = conn.cursor()
cursor.execute('SELECT * FROM your_table')

# Fetch and print the results
results = cursor.fetchall()
for result in results:
    print(result)

# Close the connection
conn.close()

