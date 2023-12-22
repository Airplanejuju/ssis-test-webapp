from flask import Blueprint, flash
from app.model.college_model import query_database, submit_form, edit_form, delete_form, search_form
from app.wtform.form import CollegeForm
from flask import render_template, request, redirect#, jsonify, url_for
#from flask import current_app as app

college_bp = Blueprint(
    "college_bp",
    __name__,
)

@college_bp.route('/')
def college():
    data = query_database()

    # Print the data for debugging purposes
    print("Data from query:", data)

    form = CollegeForm()
    return render_template('table/college.html', data=data, form=form)

@college_bp.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        try:
            # Call the insert function in college_model
            submit_form()

            # Flash a success message
            # flash('Added successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Add failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

@college_bp.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        try:
            # Call the update function in college_model
            edit_form()

            # Flash a success message
            # flash('Updated successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Update failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

@college_bp.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        try:
            # Call the delete function in college_model
            delete_form()

            # Flash a success message
            # flash('Deleted successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Delete failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

@college_bp.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search-query', '').lower()

    print(f"Received search query: {search_query} for table tblcollege")

    # Perform search logic based on the query
    search_results = search_form(search_query)

    #print(search_results)
    print(f"Final search results: {search_results}")
    
    return render_template('form/search/college-fs.html', results=search_results, form=CollegeForm())