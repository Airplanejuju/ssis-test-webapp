from flask import Blueprint, flash
from app.model.student_model import query_database, submit_form, edit_form, delete_form, search_form
from app.wtform.form import StudentForm
from flask import render_template, request, redirect

student_bp = Blueprint(
    "student_bp",
    __name__,
)

@student_bp.route('/student')
def student():
    data = query_database()

    # Print the data for debugging purposes
    print("Data from query:", data)

    form = StudentForm()
    return render_template('table/student.html', data=data, form=form)

@student_bp.route('/student/add', methods=['POST'])
def add():
    if request.method == 'POST':
        try:
            # Call the insert function in student_model
            submit_form()

            # Flash a success message
            flash('Added successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Add failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

@student_bp.route('/student/update', methods=['POST'])
def update():
    if request.method == 'POST':
        try:
            # Call the update function in student_model
            edit_form()

            # Flash a success message
            flash('Updated successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Update failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

@student_bp.route('/student/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        try:
            # Call the delete function in student_model
            delete_form()

            # Flash a success message
            flash('Deleted successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Delete failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

@student_bp.route('/student/search', methods=['POST'])
def search():
    search_query = request.form.get('search-query', '').lower()

    print(f"Received search query: {search_query} for table tblstudent")

    # Perform search logic based on the query
    search_results = search_form(search_query)

    #print(search_results)
    print(f"Final search results: {search_results}")
    
    return render_template('form/search/student-fs.html', results=search_results, form=StudentForm())