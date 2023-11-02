from flask import Blueprint, flash
from flask import render_template, request, redirect
from app.model.student_model import submit_form
from app.wtform.form import StudentForm

main_bp = Blueprint(
    "main_bp",
    __name__,
)

@main_bp.route('/')
def home():
    form = StudentForm()
    return render_template('home.html', form=form)

@main_bp.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            submit_form()

            # Flash a success message
            flash('Submitted successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Submission failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)