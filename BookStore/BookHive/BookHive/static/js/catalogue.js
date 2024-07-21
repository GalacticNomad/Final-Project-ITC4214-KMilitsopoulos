$(document).ready(function() {
    console.log("Catalogue jQuery is ready!");

    // Example: Adding a new book (assuming you have a form for adding books)
    $('#addBookForm').on('submit', function(event) {
        event.preventDefault();
        
        // Perform form validation or other manipulations
        let title = $('#id_title').val();
        let author = $('#id_author').val();

        if (title && author) {
            // Proceed with form submission or AJAX call to add the book
            console.log('Adding book:', title, author);
            // You can add an AJAX call here to submit the form data
        } else {
            alert('Please fill in both the title and author fields.');
        }
    });
});
