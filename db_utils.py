from flask import request, flash
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

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

# Function to generate a code based on the selected college
def gencode_college(college):
    # Define mappings of preset codes for colleges and courses
    college_codes = {
        'College of Engineering': 'COE',
        'College of Arts and Social Sciences': 'CASS',
        'College of Economics and Business Administration': 'CEBA',
        'College of Education': 'CED',
        'College of Health Sciences': 'CHS',
        'College of Science and Mathematics': 'CSM',
        'College of Computer Studies': 'CCS'
    }

    return college_codes.get(college, 'COL')  # Default to 'COL' if not found

# Function to generate college based on the code
def generate_college(college):
    college_codes = {
        'COE': 'College of Engineering',
        'CASS': 'College of Arts and Social Sciences',
        'CEBA': 'College of Economics and Business Administration',
        'CED': 'College of Education',
        'CHS': 'College of Health Sciences',
        'CSM': 'College of Science and Mathematics',
        'CCS': 'College of Computer Studies'
    }

    return college_codes.get(college, 'COL')  # Default to 'COL' if not found

# Function to generate a code based on the selected course
def gencode_course(course):
    course_codes = {
        # College of Engineering
        'Bachelor of Science in Metallurgical Engineering' : 'BSMetE',
        'Bachelor of Science in Computer Engineering' : 'BSCpE',
        'Bachelor of Science in Electronics and Communication Engineering': 'BSECE',
        'Bachelor of Science in Mechanical Engineering' : 'BSME',
        'Bachelor of Science in Chemical Engineering': 'BSChE',
        'Bachelor of Science in Civil Engineering' : 'BSCE',
        'Bachelor of Science in Industrial Automation and Mechatronics' : 'BSIAM',
        'Bachelor of Science in Ceramics Engineering' : 'BSCerE',
        'Bachelor of Science in Mining Engineering' : 'BSMiningE',
        'Bachelor of Science in Electrical Engineering' : 'BSEE',
        'Bachelor of Science in Environmental Engineering' : 'BSEnvE',
        # College of Arts and Social Sciences
        'Bachelor of Arts in English Language Studies' : 'BAELS',
        'Bachelor of Arts in Literary and Culture Studies' : 'BALCS',
        'Bachelor of Arts in Filipino' : 'BAF',
        'Bachelor of Arts in History' : 'BAH',
        'Bachelor of Arts in Panitikan' : 'BAP',
        'Bachelor of Arts in Political Science' : 'BAPS',
        'Bachelor of Arts in Psychology' : 'BAPsy',
        'Bachelor of Arts in Sociology' : 'BASoc',
        'Bachelor of Science in Philosophy': 'BSPhil',
        'Bachelor of Science in Psychology': 'BSPsy',
        # College of Economics and Business Administration
        'Bachelor of Science in Accountancy': 'BSA',
        'Bachelor of Science in Economics': 'BSE',
        'Bachelor of Science in Business Administration major in Business Economics': 'BSBA-BE',
        'Bachelor of Science in Business Administration major in Marketing Management': 'BSBA-MM',
        'Bachelor of Science in Entrepreneurship': 'BSEnt',
        'Bachelor of Science in Hospitality Management': 'BSHM',
        # College of Education
        'Bachelor of Elementary Education – Language Education': 'BEEd-LE',
        'Bachelor of Elementary Education – Science and Mathematics': 'BEEd-SM',
        'Bachelor of Secondary Education – Biology': 'BSE-Bio',
        'Bachelor of Secondary Education – Chemistry': 'BSE-Chem',
        'Bachelor of Secondary Education – Physics': 'BSE-Physics',
        'Bachelor of Secondary Education – Mathematics': 'BSE-Math',
        'Bachelor of Physical Education': 'BPE',
        'Bachelor of Technology and Livelihood Education major in Home Economics': 'BTLE-HE',
        'Bachelor of Technology and Livelihood Education major in Industrial Arts': 'BTLE-IA',
        'Bachelor of Technical-Vocational Teacher Education major in Drafting Technology': 'BTVTE-DraftTech',
        # College of Health Sciences
        'Bachelor of Science in Nursing': 'BSN',
        # College of Science and Mathematics
        'Bachelor of Science in Physics': 'BSP',
        'Bachelor of Science in Chemistry': 'BSChem',
        'Bachelor of Science in Biology': 'BSBio',
        'Bachelor of Science in Statistics': 'BSStat',
        'Bachelor of Science in Mathematics': 'BSMath',
        # College of Computer Studies
        'Bachelor of Science in Computer Science': 'BSCS',
        'Bachelor of Science in Computer Application': 'BSCA',
        'Bachelor of Science in Information Technology': 'BSIT',
        'Bachelor of Science in Information System': 'BSIS'
    }
    
    return course_codes.get(course, 'COURSE')  # Default to 'COURSE' if not found

# Function to generate course based on code
def generate_course(course):
    course_codes = {
        # College of Engineering
        'BSMetE' : 'Bachelor of Science in Metallurgical Engineering',
        'BSCpE' : 'Bachelor of Science in Computer Engineering',
        'BSECE': 'Bachelor of Science in Electronics and Communication Engineering',
        'BSME' : 'Bachelor of Science in Mechanical Engineering',
        'BSChE': 'Bachelor of Science in Chemical Engineering',
        'BSCE' : 'Bachelor of Science in Civil Engineering',
        'BSIAM' : 'Bachelor of Science in Industrial Automation and Mechatronics',
        'BSCerE' : 'Bachelor of Science in Ceramics Engineering',
        'BSMiningE' : 'Bachelor of Science in Mining Engineering',
        'BSEE' : 'Bachelor of Science in Electrical Engineering',
        'BSEnvE' : 'Bachelor of Science in Environmental Engineering',
        # College of Arts and Social Sciences
        'BAELS' : 'Bachelor of Arts in English Language Studies',
        'BALCS' : 'Bachelor of Arts in Literary and Culture Studies',
        'BAF' : 'Bachelor of Arts in Filipino',
        'BAH' : 'Bachelor of Arts in History',
        'BAP' : 'Bachelor of Arts in Panitikan',
        'BAPS' : 'Bachelor of Arts in Political Science',
        'BAPsy' : 'Bachelor of Arts in Psychology',
        'BASoc' : 'Bachelor of Arts in Sociology',
        'BSPhil': 'Bachelor of Science in Philosophy',
        'BSPsy': 'Bachelor of Science in Psychology',
        # College of Economics and Business Administration
        'BSA': 'Bachelor of Science in Accountancy',
        'BSE': 'Bachelor of Science in Economics',
        'BSBA-BE': 'Bachelor of Science in Business Administration major in Business Economics',
        'BSBA-MM': 'Bachelor of Science in Business Administration major in Marketing Management',
        'BSEnt': 'Bachelor of Science in Entrepreneurship',
        'BSHM': 'Bachelor of Science in Hospitality Management',
        # College of Education
        'BEEd-LE': 'Bachelor of Elementary Education – Language Education',
        'BEEd-SM': 'Bachelor of Elementary Education – Science and Mathematics',
        'BSE-Bio': 'Bachelor of Secondary Education – Biology',
        'BSE-Chem': 'Bachelor of Secondary Education – Chemistry',
        'BSE-Physics': 'Bachelor of Secondary Education – Physics',
        'BSE-Math': 'Bachelor of Secondary Education – Mathematics',
        'BPE': 'Bachelor of Physical Education',
        'BTLE-HE': 'Bachelor of Technology and Livelihood Education major in Home Economics',
        'BTLE-IA': 'Bachelor of Technology and Livelihood Education major in Industrial Arts',
        'BTVTE-DraftTech': 'Bachelor of Technical-Vocational Teacher Education major in Drafting Technology',
        # College of Health Sciences
        'BSN': 'Bachelor of Science in Nursing',
        # College of Science and Mathematics
        'BSP': 'Bachelor of Science in Physics',
        'BSChem': 'Bachelor of Science in Chemistry',
        'BSBio': 'Bachelor of Science in Biology',
        'BSStat': 'Bachelor of Science in Statistics',
        'BSMath': 'Bachelor of Science in Mathematics',
        # College of Computer Studies
        'BSCS': 'Bachelor of Science in Computer Science',
        'BSCA': 'Bachelor of Science in Computer Application',
        'BSIT': 'Bachelor of Science in Information Technology',
        'BSIS': 'Bachelor of Science in Information System'
    }

# Function to generate college code based on the course code
def gencode_college_course(course):
    college_codes = {
        # College of Engineering
        'BSMetE' : 'COE',
        'BSCpE' : 'COE',
        'BSECE': 'COE',
        'BSME' : 'COE',
        'BSChE': 'COE',
        'BSCE' : 'COE',
        'BSIAM' : 'COE',
        'BSCerE' : 'COE',
        'BSMiningE' : 'COE',
        'BSEE' : 'COE',
        'BSEnvE' : 'COE',
        # College of Arts and Social Sciences
        'BAELS' : 'CASS',
        'BALCS' : 'CASS',
        'BAF' : 'CASS',
        'BAH' : 'CASS',
        'BAP' : 'CASS',
        'BAPS' : 'CASS',
        'BAPsy' : 'CASS',
        'BASoc' : 'CASS',
        'BSPhil': 'CASS',
        'BSPsy': 'CASS',
        # College of Economics and Business Administration
        'BSA': 'CEBA',
        'BSE': 'CEBA',
        'BSBA-BE': 'CEBA',
        'BSBA-MM': 'CEBA',
        'BSEnt': 'CEBA',
        'BSHM': 'CEBA',
        # College of Education
        'BEEd-LE': 'CED',
        'BEEd-SM': 'CED',
        'BSE-Bio': 'CED',
        'BSE-Chem': 'CED',
        'BSE-Physics': 'CED',
        'BSE-Math': 'CED',
        'BPE': 'CED',
        'BTLE-HE': 'CED',
        'BTLE-IA': 'CED',
        'BTVTE-DraftTech': 'CED',
        # College of Health Sciences
        'BSN': 'CHS',
        # College of Science and Mathematics
        'BSP': 'CSM',
        'BSChem': 'CSM',
        'BSBio': 'CSM',
        'BSStat': 'CSM',
        'BSMath': 'CSM',
        # College of Computer Studies
        'BSCS': 'CCS',
        'BSCA': 'CCS',
        'BSIT': 'CCS',
        'BSIS': 'CCS'
    }


def record_exists(table, field, value):
    connection = create_connection()
    
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {table} WHERE {field} = %s"
            cursor.execute(query, (value,))
            result = cursor.fetchone()
            return result is not None
    finally:
        connection.close()

def submit_form():
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
        if 'college' in form_data:
            college = form_data.get('college', '')
            college_code = gencode_college(college)
        if 'course' in form_data:
            course = form_data.get('course', '')
            course_code = gencode_course(course)
        if 'year' in form_data:
            year = int(form_data.get('year', ''))

        # Database connection
        connection = create_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful! <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'success')
        else:
            flash('Connection failed!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

        try:
            with connection.cursor() as cursor:
                
                if 'college' in form_data:
                    if not record_exists('tblcollege', 'code', college_code):
                        # Insert into tblcollege
                        college_query = "INSERT INTO tblcollege (code, name) VALUES (%s, %s)"
                        cursor.execute(college_query, (college_code, college))
                        # Flash a message
                        flash(f'Inserted into tblcollege: {college_query % (college_code, college)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')
                    else:
                        flash(f'College already exists: {college_code} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

                if 'course' in form_data:
                    if not record_exists('tblcourse', 'code', course_code):
                        # Insert into tblcourse
                        course_query = "INSERT INTO tblcourse (code, name, college) VALUES (%s, %s, %s)"
                        cursor.execute(course_query, (course_code, course, college_code))
                        # Flash a message
                        flash(f'Inserted into tblcourse: {course_query % (course_code, course, college)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')
                    else:
                        flash(f'Course already exists: {course_code} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

                if 'id' in form_data:
                    if not record_exists('tblstudent', 'id', id):
                        # Insert into tblstudent
                        student_query = "INSERT INTO tblstudent (id, firstName, lastName, course, year, gender) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(student_query, (id, first_name, last_name, course_code, year, gender))
                        # Flash a message
                        flash(f'Inserted into tblstudent: {student_query % (id, first_name, last_name, course_code, year, gender)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')
                    else:
                        flash(f'Student already exists: {id} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error inserting data: {e} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error inserting data: {e}")
            connection.rollback()
        finally:
            connection.close()

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
        if 'courseCode' in form_data:
            code = form_data.get('courseCode', '')
            name = form_data.get('courseName', '')
            college = form_data.get('courseCollege', '')
        if 'studentId' in form_data:
            id = form_data.get('studentId', '')
            firstName = form_data.get('studentFirstname', '')
            lastName = form_data.get('studentLastname', '')
            course = form_data.get('studentCourse', '')
            year = int(form_data.get('studentYear', ''))
            gender = form_data.get('studentGender', '')

        # Database connection
        connection = create_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful! <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'success')
        else:
            flash('Connection failed!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'collegeCode' in form_data:
                    # Update tblcollege
                    college_query = "UPDATE tblcollege SET name = %s WHERE code = %s"
                    cursor.execute(college_query, (name, code))
                    # Flash a message
                    flash(f'Updated into tblcollege: {college_query % (code, name)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')

                if 'courseCode' in form_data:
                    # Update tblcourse
                    if record_exists('tblcollege', 'code', college):
                        course_query = "UPDATE tblcourse SET name = %s, college = %s WHERE code = %s"
                        cursor.execute(course_query, (name, college, code))
                        # Flash a message
                        flash(f'Updated into tblcourse: {course_query % (name, college, code)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')
                    if not record_exists('tblcollege', 'code', college):
                        collegeName = generate_college(college)
                        # Insert into tblcollege
                        college_query = "INSERT INTO tblcollege (code, name) VALUES (%s, %s)"
                        cursor.execute(college_query, (college, collegeName))
                        # Then insert into tblcourse
                        course_query = "UPDATE tblcourse SET name = %s, college = %s WHERE code = %s"
                        cursor.execute(course_query, (name, college, code))
                        # Flash a message
                        flash(f'Updated into tblcourse: {course_query % (name, college, code)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')

                if 'studentId' in form_data:
                    # Update tblstudent
                    if record_exists('tblcourse','code', course):
                        student_query = "UPDATE tblstudent SET firstName = %s, lastName = %s, course = %s, year = %s, gender = %s WHERE id = %s"
                        cursor.execute(student_query, (firstName, lastName, course, year, gender, id))
                        # Flash a message
                        flash(f'Updated into tblstudent: {student_query % (firstName, lastName, course, year, gender, id)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')
                    if not record_exists('tblcourse', 'code', course):
                        collegeCode = gencode_college_course(course)
                        if record_exists('tblcollege', 'code', collegeCode):
                            # Insert into tblcourse
                            course_query = "INSERT INTO tblcourse (code, name, college) VALUES (%s, %s, %s)"
                            cursor.execute(course_query, (course, name, collegeCode))
                            # Then update tblstudent
                            student_query = "UPDATE tblstudent SET firstName = %s, lastName = %s, course = %s, year = %s, gender = %s WHERE id = %s"
                            cursor.execute(student_query, (firstName, lastName, course, year, gender, id))
                            # Flash a message
                            flash(f'Updated into tblstudent: {student_query % (firstName, lastName, course, year, gender, id)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')
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
                            flash(f'Updated into tblstudent: {student_query % (firstName, lastName, course, year, gender, id)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')
            
            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error updating data: {e} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error updating data: {e}")
            connection.rollback()
        finally:
            connection.close()

def delete_form():
    if request.method == 'POST':
        # Extract form data dynamically
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Accessing specific fields
        if 'collegeCode' in form_data:
            code = form_data.get('collegeCode', '')
        if 'courseCode' in form_data:
            code = form_data.get('courseCode', '')
        if 'studentId' in form_data:
            id = form_data.get('studentId', '')

        # Database connection
        connection = create_connection()

        # Check if connection is successful
        if connection:
            flash('Connection successful! <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'success')
        else:
            flash('Connection failed!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

        try:
            with connection.cursor() as cursor:
                if 'collegeCode' in form_data:
                    # Delete from tblcollege
                    college_query = "DELETE FROM tblcollege WHERE code = %s"
                    cursor.execute(college_query, (code,))
                    # Flash a message
                    flash(f'Deleted from tblcollege: {college_query % (code,)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')

                if 'courseCode' in form_data:
                    # Delete from tblcourse
                    course_query = "DELETE FROM tblcourse WHERE code = %s"
                    cursor.execute(course_query, (code,))
                    # Flash a message
                    flash(f'Deleted from tblcourse: {course_query % (code,)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')

                if 'studentId' in form_data:
                    # Delete from tblstudent
                    student_query = "DELETE FROM tblstudent WHERE id = %s"
                    cursor.execute(student_query, (id,))
                    # Flash a message
                    flash(f'Deleted from tblstudent: {student_query % (id,)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'info')

            # Commit the changes
            connection.commit()

        except Exception as e:
            # Flash an error message
            flash(f'Error deleting data: {e} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')

            # Handle the exception (rollback, log, etc.)
            print(f"Error deleting data: {e}")
            connection.rollback()
        finally:
            connection.close()

# Function to query the database
def queryfull_database(tablename, columns, keyword):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM {tablename} WHERE "
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

# Function to search for a keyword in the specified tables and columns
def search_form(keyword, table_id):
     # Define your tables and columns based on the received table ID
    tables = {
        'tblcourse': ['code', 'name', 'college'],
        'tblcollege': ['code', 'name'],
        'tblstudent': ['id', 'firstName', 'lastName', 'course', 'year', 'gender']
    }
    results=  {}
    if table_id in tables:
        columns = tables[table_id]
        result = queryfull_database(table_id, columns, keyword)
        if result:
            results[table_id] = result

    print(f"Search results for '{keyword}' in table {table_id}: {results}")
    return results
