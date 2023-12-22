from flask import Blueprint, flash
from flask import render_template, request, redirect
from app.model.student_model import submit_form, query_database
from app.wtform.form import StudentForm

from app.model.course_model import query_database as query_course

main_bp = Blueprint(
    "main_bp",
    __name__,
)

@main_bp.route('/')
def home():
    # form = StudentForm()
    # return render_template('home.html', form=form)
    data = query_database()

    # Print the data for debugging purposes
    print("Data from query:", data)

    form = StudentForm()
    courses = query_course() #get courses available in course table
    return render_template('table/student.html', data=data, form=form, courses=courses)

# @main_bp.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         try:
#             submit_form()

#             # Flash a success message
#             flash('Submitted successfully!', 'success')
#         except Exception as e:
#             # Flash an error message
#             flash(f'Submission failed: {str(e)}', 'danger')
    
#     return redirect(request.referrer)