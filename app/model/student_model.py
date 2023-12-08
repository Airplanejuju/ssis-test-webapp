from flask import request, flash, current_app
from mysql.connector import Error
from .util import gencode_course, gencode_college, generate_college, gencode_college_course, generate_course


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
            query = f"SELECT * FROM tblstudent"
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
            query = f"SELECT * FROM tblstudent WHERE "
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
def submit_form(secure_url=None):
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'id' in form_data:
            id = form_data.get('id', '')
        if 'firstname' in form_data:
            first_name = form_data.get('firstname', '')
        if 'lastname' in form_data:
            last_name = form_data.get('lastname', '')
        if 'gender' in form_data:
            gender = form_data.get('gender', '')
        if 'course' in form_data:
            course = form_data.get('course', '')
            # flash(f'Course: {course}', 'info')
        if 'year' in form_data:
            year = int(form_data.get('year', ''))

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful!', 'success')
        else:
            flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:

                if 'id' in form_data:
                    if not record_exists('tblstudent', 'id', id):
                        # Insert into tblstudent
                        student_query = "INSERT INTO tblstudent (id, firstName, lastName, course, year, gender, photoUrl) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(student_query, (id, first_name, last_name, course, year, gender, secure_url))
                        # Flash a message
                        flash(f'Inserted into tblstudent: {student_query % (id, first_name, last_name, course, year, gender, secure_url)}', 'info')
                    else:
                        flash(f'Student already exists: {id}', 'danger')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error inserting data: {e}', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error inserting data: {e}")
            connection.rollback()
        finally:
            pass

# Function to update a record in the database
def edit_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'studentId' in form_data:
            id = form_data.get('studentId', '')
            firstName = form_data.get('studentFirstname', '')
            lastName = form_data.get('studentLastname', '')
            course = form_data.get('studentCourse', '')
            year = int(form_data.get('studentYear', ''))
            gender = form_data.get('studentGender', '')

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful!', 'success')
        else:
            flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'studentId' in form_data:
                    # Update tblstudent
                    if record_exists('tblcourse','code', course):
                        student_query = "UPDATE tblstudent SET firstName = %s, lastName = %s, course = %s, year = %s, gender = %s WHERE id = %s"
                        cursor.execute(student_query, (firstName, lastName, course, year, gender, id))
                        # Flash a message
                        flash(f'Updated into tblstudent: {student_query % (firstName, lastName, course, year, gender, id)}', 'info')
                    if not record_exists('tblcourse', 'code', course):
                        print(f"Course: {course}")

                        collegeCode = gencode_college_course(course)
                        print(f"Received: {collegeCode}")

                        name =  generate_course(course)
                        print(f"Name Received: {name}")
            
                        if record_exists('tblcollege', 'code', collegeCode):
                            # Insert into tblcourse
                            course_query = "INSERT INTO tblcourse (code, name, college) VALUES (%s, %s, %s)"
                            cursor.execute(course_query, (course, name, collegeCode))
                            # Then update tblstudent
                            student_query = "UPDATE tblstudent SET firstName = %s, lastName = %s, course = %s, year = %s, gender = %s WHERE id = %s"
                            cursor.execute(student_query, (firstName, lastName, course, year, gender, id))
                            # Flash a message
                            flash(f'Updated into tblstudent: {student_query % (firstName, lastName, course, year, gender, id)}', 'info')
                        if not record_exists('tblcollege', 'code', collegeCode):
                            collegeName = generate_college(collegeCode)
                            # Insert into tblcollege
                            college_query = "INSERT INTO tblcollege (code, name) VALUES (%s, %s)"
                            cursor.execute(college_query, (collegeCode, collegeName))
                            # Then insert into tblcourse
                            course_query = "INSERT INTO tblcourse (code, name, college) VALUES (%s, %s, %s)"
                            cursor.execute(course_query, (course, name, collegeCode))
                            # Then update tblstudent
                            student_query = "UPDATE tblstudent SET firstName = %s, lastName = %s, course = %s, year = %s, gender = %s WHERE id = %s"
                            cursor.execute(student_query, (firstName, lastName, course, year, gender, id))
                            # Flash a message
                            flash(f'Updated into tblstudent: {student_query % (firstName, lastName, course, year, gender, id)}', 'info')
            
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
        if 'studentId' in form_data:
            id = form_data.get('studentId', '')

        # Database connection
        connection = get_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful!', 'success')
        else:
            flash('Connection failed!', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'studentId' in form_data:
                    # Delete from tblstudent
                    student_query = "DELETE FROM tblstudent WHERE id = %s"
                    cursor.execute(student_query, (id,))
                    # Flash a message
                    flash(f'Deleted from tblstudent: {student_query % (id,)}', 'info')

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
        # Define columns for tblstudent
        columns = ['id', 'firstName', 'lastName', 'course', 'year', 'gender']
    
        # Perform the search
        result = queryfull_database(columns, keyword)

        # Build and return results dictionary
        results = {'tblstudent': result} if result else {}
    
        # Print and return results
        print(f"Search results for '{keyword}' in table tblstudent: {results}")
        return results
    else:
        # Handle other HTTP methods (GET, etc.) if needed
        return None