from flask import Flask, render_template, redirect, url_for, request, flash
from form import StudentForm
from db_utils import query_database, submit_form
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Set the secret key for CSRF protection
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')


@app.route('/')
def form():
    form = StudentForm()
    return render_template('studentform.html', form=form)

@app.route('/submit_form', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            submit_form()

            # Flash a success message
            flash('Submitted successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Submission failed: {str(e)}', 'danger')

        # Redirect to the form page
        return redirect(url_for('form'))

# Example route to query the database
@app.route('/student')
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
