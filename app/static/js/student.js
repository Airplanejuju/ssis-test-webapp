$(document).on('click', '.edit-btn', function(){
    // Capture data attributes
    var studentId = $(this).data('student-id');
    var studentFirstname = $(this).data('student-firstname');
    var studentLastname = $(this).data('student-lastname');
    var studentCourse = $(this).data('student-course');
    var studentYear = $(this).data('student-year');
    var studentGender = $(this).data('student-gender');

    // If you want to update a form field
    $('#studentId').val(studentId);
    $('#studentFirstname').val(studentFirstname);
    $('#studentLastname').val(studentLastname);
    $('#studentCourse').val(studentCourse);
    $('#studentYear').val(studentYear);
    $('#studentGender').val(studentGender);

    // Print values to check
    console.log("ID:", studentId);
    console.log("First Name:", studentFirstname);
    console.log("Last Name:", studentLastname);
    console.log("Course:", studentCourse);
    console.log("Year:", studentYear);
    console.log("Gender:", studentGender);

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
            url: '{{ url_for("student_bp.delete") }}',  
            data: { 'studentId': studentId },
            success: function(response) {
                // Handle success, e.g., remove the corresponding row from the table
                console.log(response);

                location.reload();
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

        // Get the table ID from the data attribute
        var tableId = $(this).data('table-id');

        // Make an AJAX request to the server
        $.ajax({
            type: 'POST',
            url: '{{ url_for("student_bp.search") }}',
            data: { 'search-query': searchQuery, 'table-id': tableId },
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