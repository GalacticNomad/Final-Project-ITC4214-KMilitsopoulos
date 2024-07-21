$(document).ready(function(){
    $('#search-form').on('submit', function(event){
        event.preventDefault();
        // Retrieves the value of the search input field
        var query = $('#search-input').val();
        $.ajax({
            // Specifies the URL for the AJAX request to the server's search endpoint
            url: '/catalogue/books/search/',
            
            // Sends the search query as data in the AJAX request
            data: {
                'q': query
            },
            dataType: 'json',

            // Defines the callback function to execute if the request is successful
            success: function(data){
                // Clears any existing content in the book list
                $('#book-list').empty();
                if (data.books.length > 0) {
                    data.books.forEach(function(book){

                        // Creates a card element for each book with its details and cover image
                        var bookCard = `
                            <div class="card mb-3">
                                <img class="card-img-top" src="${book.cover_image ? book.cover_image : '/static/images/cover-coming-soon.png'}" alt="${book.title}">
                                <div class="card-body">
                                    <h5 class="card-title">${book.title}</h5>
                                    <p class="card-text">by ${book.author}</p>
                                    <a href="${book.detail_url}" class="btn btn-primary">View Details</a>
                                </div>
                            </div>`;
                        // Appends the book card to the book list
                        $('#book-list').append(bookCard);
                    });
                } else {
                    // If no books are found, displays a message
                    $('#book-list').append('<p>No books found.</p>');
                }
            },
            // Defines the callback function to execute if the request fails
            // Logs the error information to the console
            error: function(xhr, status, error) {
                console.error("An error occurred: " + status + " " + error);
            }
        });
    });
});
