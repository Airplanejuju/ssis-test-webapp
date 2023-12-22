from flask import request, flash, current_app
from mysql.connector import Error
from .util import gencode_course, gencode_college, generate_college


def get_connection():
    # Access centralized database connection
    connection = current_app.db_connection
    return connection
    
# Function to query the database
def query_database():

    # Create a connection
    connection = get_connection()

    # Query the database
    if connection:
        try:
            query = f"SELECT * FROM tblcourse"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            #connection.close()
            #print("Connection closed")
            pass
    return None



# Function to search the database
def queryfull_database(columns, keyword):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM tblcourse WHERE "
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
            #connection.close()
            pass

# Function to check if record exists
def record_exists(table, field, value):
    connection = get_connection()
    
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {table} WHERE {field} = %s"
            cursor.execute(query, (value,))
            result = cursor.fetchone()
            return result is not None
    finally:
        #connection.close()
        pass

# Function to insert a record into the database
def submit_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        if 'college' in form_data:
            college = form_data.get('college', '')
            college_code = gencode_college(college)

        if 'course' in form_data:
            course = form_data.get('course', '')
            course_code = gencode_course(course)

        # Database connection
        connection = get_connection()

        # # Check if connection is successful
        # if connection:
        #     flash('Connection successful!', 'success')
        # else:
        #     flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'college' in form_data:
                    if not record_exists('tblcollege', 'code', college_code):
                        # Insert into tblcollege
                        college_query = "INSERT INTO tblcollege (code, name) VALUES (%s, %s)"
                        cursor.execute(college_query, (college_code, college))
                        # Flash a message
                        # flash(f'Inserted into tblcollege: {college_query % (college_code, college)}', 'info')
                    # else:
                    #     flash(f'College already exists: {college_code}', 'danger')

                if 'course' in form_data:
                    if not record_exists('tblcourse', 'code', course_code):
                        # Insert into tblcourse
                        course_query = "INSERT INTO tblcourse (code, name, college) VALUES (%s, %s, %s)"
                        cursor.execute(course_query, (course_code, course, college_code))
                        # Flash a message
                        # flash(f'Inserted into tblcourse: {course_query % (course_code, course, college)}', 'info')
                        # Flash a success message
                        flash('Data inserted successfully!', 'success')
                    else:
                        flash(f'Course already exists: {course_code}', 'danger')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error inserting data: {e}', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error inserting data: {e}")
            connection.rollback()
        finally:
            #connection.close()
            pass

# Function to update a record in the database
def edit_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'courseCode' in form_data:
            code = form_data.get('courseCode', '')
            name = form_data.get('courseName', '')
            college = form_data.get('courseCollege', '')

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        # if connection:
        #     flash('Connection successful!', 'success')
        # else:
        #     flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'courseCode' in form_data:
                    # Update tblcourse
                    if record_exists('tblcollege', 'code', college):
                        course_query = "UPDATE tblcourse SET name = %s, college = %s WHERE code = %s"
                        cursor.execute(course_query, (name, college, code))
                        # Flash a message
                        # flash(f'Updated into tblcourse: {course_query % (name, college, code)}', 'info')
                        flash('Data updated successfully!', 'success')
                    if not record_exists('tblcollege', 'code', college):
                        collegeName = generate_college(college)
                        # Insert into tblcollege
                        college_query = "INSERT INTO tblcollege (code, name) VALUES (%s, %s)"
                        cursor.execute(college_query, (college, collegeName))
                        # Then insert into tblcourse
                        course_query = "UPDATE tblcourse SET name = %s, college = %s WHERE code = %s"
                        cursor.execute(course_query, (name, college, code))
                        # Flash a message
                        # flash(f'Updated into tblcourse: {course_query % (name, college, code)}', 'info')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error updating data: {e}', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error updating data: {e}")
            connection.rollback()
        finally:
            #connection.close()
            pass

# Function to delete a record from the database
def delete_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'courseCode' in form_data:
            code = form_data.get('courseCode', '')

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        # if connection:
        #     flash('Connection successful!', 'success')
        # else:
        #     flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'courseCode' in form_data:
                    # Delete from tblcourse
                    course_query = "DELETE FROM tblcourse WHERE code = %s"
                    cursor.execute(course_query, (code,))
                    # Flash a message
                    # flash(f'Deleted from tblcourse: {course_query % (code,)}', 'info')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error deleting data: {e}', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error deleting data: {e}")
            connection.rollback()
        finally:
            #connection.close()
            pass

# Function to initiate search query and return results
def search_form(keyword):
    if request.method == 'POST':
        # Define columns for tblcourse
        columns = ['code', 'name', 'college']
    
        # Perform the search
        result = queryfull_database(columns, keyword)

        # Build and return results dictionary
        results = {'tblcourse': result} if result else {}
    
        # Print and return results
        print(f"Search results for '{keyword}' in table tblcourse: {results}")
        return results
    else:
        # Handle other HTTP methods (GET, etc.) if needed
        return None