from flask import Flask, render_template, redirect, url_for, request, flash
from form import StudentForm, CourseForm, CollegeForm
from db_utils import query_database, submit_form, edit_form, delete_form, search_form
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Set the secret key for CSRF protection
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')


@app.route('/')
def form():
    form = StudentForm()
    return render_template('home.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            submit_form()

            # Flash a success message
            flash('Submitted successfully! <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Submission failed: {str(e)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')
    
    return redirect(request.referrer)

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        try:
            # Call the update function in db_utils
            edit_form()

            # Flash a success message
            flash('Updated successfully! <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Update failed: {str(e)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')
    
    return redirect(request.referrer)

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        try:
            # Call the delete function in db_utils
            delete_form()

            # Flash a success message
            flash('Deleted successfully! <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Delete failed: {str(e)} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>', 'danger')
    
    return redirect(request.referrer)

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search-query', '').lower()
    
    print(f"Received search query: {search_query}")

    # If the search query is empty, return the full data
    if not search_query:
        return render_template('search_results.html', results=None)

    # Perform search logic based on the query
    search_results = search_form(search_query)

    #print(search_results)
    print(f"Final search results: {search_results}")
    return render_template('search_results.html', results=search_results)

# Example route to query the database
@app.route('/student')
def student():
    data = query_database('tblstudent')
    form = StudentForm()
    return render_template('db/student.html', data=data, form=form)

@app.route('/course')
def course():
    data = query_database('tblcourse')
    form = CourseForm()
    return render_template('db/course.html', data=data, form=form)

@app.route('/college')
def college():
    data = query_database('tblcollege')
    form = CollegeForm()
    return render_template('db/college.html', data=data, form=form)


# Other Flask configurations and routes go here
if __name__ == '__main__':
    app.run()
