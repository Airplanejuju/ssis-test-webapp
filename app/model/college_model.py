from flask import request, flash, current_app
from mysql.connector import Error
from .util import gencode_college

# Function to create a database connection
def get_connection():
    return current_app.config.get('MYSQL_DB')

# Function to query the database
def query_database():
    # Create a connection
    connection = get_connection()

    # Initialize cursor outside the try block
    cursor = None

    # Query the database
    if connection:
        try:
            query = f"SELECT * FROM tblcollege"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print(f"Error executing query: {e}")
            # Close the cursor if an exception occurs
            if cursor:
                cursor.close()
        finally:
            # Do not close the connection here, as it is being managed externally
            pass
    return None


# Function to search the database
def queryfull_database(columns, keyword):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM tblcollege WHERE "
            for column in columns:
                query += f"{column} LIKE '%{keyword}%' OR "
            query = query[:-4]  # Remove the last 'OR'
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(e)
            return None
        finally:
            connection.close()

# Function to check if record exists
def record_exists(field, value):
    connection = get_connection()
    
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM tblcollege WHERE {field} = %s"
            cursor.execute(query, (value,))
            result = cursor.fetchone()
            return result is not None
    finally:
        connection.close()

# Function to insert a record into the database
def submit_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'college' in form_data:
            college = form_data.get('college', '')
            college_code = gencode_college(college)

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful!', 'success')
        else:
            flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'college' in form_data:
                    if not record_exists('tblcollege', 'code', college_code):
                        # Insert into tblcollege
                        college_query = "INSERT INTO tblcollege (code, name) VALUES (%s, %s)"
                        cursor.execute(college_query, (college_code, college))
                        # Flash a message
                        flash(f'Inserted into tblcollege: {college_query % (college_code, college)}', 'info')
                    else:
                        flash(f'College already exists: {college_code}', 'danger')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error inserting data: {e}', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error inserting data: {e}")
            connection.rollback()
        finally:
            connection.close()

# Function to update a record in the database
def edit_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'collegeCode' in form_data:
            code = form_data.get('collegeCode', '')
            name = form_data.get('collegeName', '')

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful!', 'success')
        else:
            flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'collegeCode' in form_data:
                    # Update tblcollege
                    college_query = "UPDATE tblcollege SET name = %s WHERE code = %s"
                    cursor.execute(college_query, (name, code))
                    # Flash a message
                    flash(f'Updated into tblcollege: {college_query % (code, name)}', 'info')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error updating data: {e}', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error updating data: {e}")
            connection.rollback()
        finally:
            connection.close()

# Function to delete a record in the database
def delete_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'collegeCode' in form_data:
            code = form_data.get('collegeCode', '')

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful!', 'success')
        else:
            flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'collegeCode' in form_data:
                    # Delete from tblcollege
                    college_query = "DELETE FROM tblcollege WHERE code = %s"
                    cursor.execute(college_query, (code,))
                    # Flash a message
                    flash(f'Deleted from tblcollege: {college_query % (code,)}', 'info')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error deleting data: {e}', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error deleting data: {e}")
            connection.rollback()
        finally:
            connection.close()

# Function to initiate search query and return results
def search_form(keyword):
    # Define columns for tblcollege
    columns = ['code', 'name']
    
    # Perform the search
    result = queryfull_database(columns, keyword)

    # Build and return results dictionary
    results = {'tblcollege': result} if result else {}
    
    # Print and return results
    print(f"Search results for '{keyword}' in table tblcollege: {results}")
    return results
