import mysql.connector
import dotenv
import os
import time

dotenv.load_dotenv()
connection = mysql.connector.connect(
    host=os.environ.get("MYSQL_HOST"),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    database=os.environ.get("MYSQL_DATABASE") 
)
print(connection)
database_name = os.environ.get("MYSQL_DATABASE")

table_name = "calls"
cursor = connection.cursor()
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    username VARCHAR(30) NOT NULL,
    call_duration INT NOT NULL
)
"""
cursor.execute(create_table_query)
cursor.close()

# Commit changes and close the connection
connection.commit()
connection.close()

print(f"Database '{database_name}' and table '{table_name}' created successfully.")
