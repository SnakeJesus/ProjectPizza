# Import required modules
import os
import django

# Set up environment variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

# Connect to the database
import mysql.connector
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'PizzaDB',
        'USER': 'HeadChef',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
conn = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
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

#create a table on the database
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")