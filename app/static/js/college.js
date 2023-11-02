$(document).on('click', '.edit-btn', function() {
    // Capture data attributes
    var collegeCode = $(this).data('college-code');
    var collegeName = $(this).data('college-name');

    // If you want to update a form field, for example, an input with an ID 'collegeCodeInput'
    $('#collegeCodeInput').val(collegeCode);
    $('#collegeName').val(collegeName);

    // Open the modal if needed
    $('#collegeEditModal').modal('show');
});

$(document).on('click', '.delete-btn', function() {
    // Capture data attributes
    var collegeCode = $(this).data('college-code');

    // Confirm deletion with user if needed
    var confirmDelete = confirm(`Are you sure you want to delete ${collegeCode}?`);

    if (confirmDelete) {
        // Make an AJAX request to delete the item
        $.ajax({
            type: 'POST',
            url: '{{ url_for("college_bp.delete") }}',  
            data: { 'collegeCode': collegeCode },
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
$(document).on('click', '.search-btn', function() {
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
        url: '{{ url_for("college_bp.search") }}',
        data: { 'search-query': searchQuery, 'table-id': tableId },
        success: function(response) {
            // Update the content inside the tbody with the search results
            $('#college_tbody').html(response);
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