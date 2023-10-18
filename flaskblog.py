from flask import Flask, render_template
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Database Configuration
db_config = {
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'user': os.environ['DB_USERNAME'],
    'password': os.environ['DB_PASSWORD'],
    'database': os.environ['DB_NAME'],
}

# Function to create a database connection
def create_connection():
    connection = connect(**db_config)
    return connection

# Function to query the database
def query_database(tablename):

    # Create a connection
    connection = create_connection()

    # Query the database
    if connection:
        try:
            query = f"SELECT * FROM {tablename}"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            connection.close()
    return None

# Example route to query the database
@app.route('/')
def student():
    data = query_database('tblstudent')
    return render_template('db/student.html', data=data)

@app.route('/course')
def course():
    data = query_database('tblcourse')
    return render_template('db/course.html', data=data)

@app.route('/college')
def college():
    data = query_database('tblcollege')
    return render_template('db/college.html', data=data)


# Other Flask configurations and routes go here

if __name__ == '__main__':
    app.run()
