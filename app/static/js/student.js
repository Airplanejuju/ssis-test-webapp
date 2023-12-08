$(document).on('click', '.photo-btn', function(){
    // Capture data attribute
    var studentPhoto = $(this).data('student-photo');

    // Check if the URL is truthy
    if (studentPhoto != "None") {
        // Update image source
        $('#studentPhotoPreview').attr('src', studentPhoto);

        // Print value to check
        console.log("Photo source:", studentPhoto);

        // Open the modal if needed
        $('#studentPhotoModal').modal('show');
    } else {
        src = "https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg"
        $('#studentPhotoPreview').attr('src', src);
        console.log("Student photo URL is empty or undefined.");
    }
});

$(document).on('click', '.edit-btn', function(){
    // Capture data attributes
    var studentId = $(this).data('student-id');
    var studentFirstname = $(this).data('student-firstname');
    var studentLastname = $(this).data('student-lastname');
    var studentCourse = $(this).data('student-course');
    var studentYear = $(this).data('student-year');
    var studentGender = $(this).data('student-gender');
    var studentPhoto = $(this).data('student-photo');

    // If you want to update a form field
    $('#studentId').val(studentId);
    $('#studentFirstname').val(studentFirstname);
    $('#studentLastname').val(studentLastname);
    $('#studentCourse').val(studentCourse);
    $('#studentYear').val(studentYear);
    $('#studentGender').val(studentGender);
    $('#studentPhoto').val(studentPhoto);

    // Print values to check
    console.log("ID:", studentId);
    console.log("First Name:", studentFirstname);
    console.log("Last Name:", studentLastname);
    console.log("Course:", studentCourse);
    console.log("Year:", studentYear);
    console.log("Gender:", studentGender);
    console.log("Photo:", studentPhoto);

    // Open the modal if needed
    $('#studentEditModal').modal('show');
});

$(document).on('click', '.delete-btn', function() {
    // Capture data attributes
    var studentId = $(this).data('student-id');

    // Confirm deletion with user if needed
    var confirmDelete = confirm(`Are you sure you want to delete ${studentId}?`);

    if (confirmDelete) {
        // Make an AJAX request to delete the item
        $.ajax({
            type: 'POST',
            url: deleteUrl,  
            data: { 'studentId': studentId },
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(response) {
                // Handle success, e.g., remove the corresponding row from the table
                console.log(response);

                // Show a simple alert after successful deletion
               alert(`Item with code ${studentId} deleted successfully!`);

               // Reload the page after a delay
               setTimeout(function(){
                   location.reload();
               }, 200);
            },
            error: function(error) {
                // Handle error
                console.error(error);
            }
        });
    }
});

$(document).ready(function() {
    $(document).on('click', '#searchButton', function() {
        // Get the search query from the input field
        var searchQuery = $('#searchInput').val();

         // Check if the search query is empty
        if (searchQuery === "") {
            // Reload the page if the search query is empty
            location.reload();
            return false;  // Prevent the default form submission
        }

        // Make an AJAX request to the server
        $.ajax({
            type: 'POST',
            url: searchUrl,
            data: { 'search-query': searchQuery },
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(response) {
                // Update the content inside the tbody with the search results
                $('#student_tbody').html(response);
            },
            error: function(error) {
                console.error(error);
            }
        });

        // Prevent the default form submission
        return false;
    });
});

$(document).ready(function(){
    // Set a timeout to fade out the alert after 3 seconds (adjust the duration as needed)
    setTimeout(function(){
        $('.alert').fadeOut('slow');
    }, 3000);
});