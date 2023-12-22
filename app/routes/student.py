from flask import Blueprint, flash
from app.model.student_model import query_database, submit_form, edit_form, delete_form, search_form
from app.model.course_model import query_database as query_course
from app.wtform.form import StudentForm
from flask import render_template, request, redirect
import re

from cloudinary.uploader import upload, destroy
from app.model.util import public_id

student_bp = Blueprint(
    "student_bp",
    __name__,
)

@student_bp.route('/')
def student():
    data = query_database()

    # Print the data for debugging purposes
    print("Data from query:", data)

    form = StudentForm()
    courses = query_course() #get courses available in course table
    return render_template('table/student.html', data=data, form=form, courses=courses)

@student_bp.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        id = request.form['id']
        photo = request.files['photo']
        #Check if ID correct format
        if not re.match(r'\d{4}-\d{4}', id):
            flash("Incorrect format.", 'danger')
            return redirect(request.referrer)
        try:
            if photo:
                upload_result = upload(photo, folder="ssis", resource_type='image')
                secure_url = upload_result['secure_url']
            else:
                secure_url = None
            # Call the insert function in student_model
            submit_form(secure_url)

            # Flash a success message
            # flash('Added successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Add failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

from flask import make_response

@student_bp.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        currentPhoto = request.form.get('currentStudentPhotoUrl')
        newPhoto = request.files['studentPhoto']
        
        print("Current Photo: ",currentPhoto)
        print("New Photo :",newPhoto)
        try:
            # Upload new photo to cloudinary
            if newPhoto:
                upload_result = upload(newPhoto, folder="ssis", resource_type='image')
                secure_url = upload_result['secure_url']

                # flash(f"Uploaded new photo: {secure_url}", 'info')
                # Delete old photo from cloudinary
                if currentPhoto:
                    try:
                        # Extract public ID from the photo URL
                        public_id_val = public_id(currentPhoto)

                        # Delete the photo using its public ID
                        result = destroy("ssis/" + public_id_val)

                        # Check the deletion result
                        # if result.get("result") == "ok":
                        #     # Flash a success message
                        #     # flash('Updated successfully!', 'success')
                        # else:
                        #     # Flash an error message
                        #     flash(f"Error deleting old photo: {result.get('result')}", 'danger')
                    except Exception as e:
                        flash(f"Error deleting old photo: {str(e)}", 'danger')

                    # Call the update function in student_model
                    edit_form(secure_url)
                else:
                    # Call the update function in student_model
                    edit_form(secure_url)
                    # Flash a success message
                    # flash('Updated successfully!', 'success')
            else:
                secure_url = None

                # Call the update function in student_model
                edit_form(secure_url)
                # Flash a success message
                # flash('Updated successfully! No new photo.', 'success')

        except Exception as e:
            # Flash an error message
            flash(f'Update failed: {str(e)}', 'danger')
    
    # return jsonify({'success': False, 'error': 'Invalid request. Missing required data.'})
    return redirect(request.referrer)

@student_bp.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        # Retrieve photo url
        photo = request.form.get('photoUrl')
        print("Photo: ",photo)
        try:
            # Delete old photo from cloudinary
            if photo:
                try:
                    # Extract public ID from the photo URL
                    public_id_val = public_id(photo)

                    # Delete the photo using its public ID
                    result = destroy("ssis/" + public_id_val)

                    # Check the deletion result
                    # if result.get("result") == "ok":
                    #     # Flash a success message
                    #     flash('Updated successfully!', 'success')
                    # else:
                    #     # Flash an error message
                    #     flash(f"Error deleting old photo: {result.get('result')}", 'danger')
                except Exception as e:
                    flash(f"Error deleting old photo: {str(e)}", 'danger')

                # Call the delete function in student_model
                delete_form()
            else:
                # Call the delete function in student_model
                delete_form()
                # Flash a success message
                # flash('Deleted successfully!', 'success')
        except Exception as e:
            # Flash an error message
            flash(f'Delete failed: {str(e)}', 'danger')
    
    return redirect(request.referrer)

@student_bp.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search-query', '').lower()

    print(f"Received search query: {search_query} for table tblstudent")

    # Perform search logic based on the query
    search_results = search_form(search_query)

    #print(search_results)
    print(f"Final search results: {search_results}")
    
    return render_template('form/search/student-fs.html', results=search_results, form=StudentForm())