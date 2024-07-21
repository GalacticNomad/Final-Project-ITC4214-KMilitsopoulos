
// Ensures the script runs only after the DOM is fully loaded
$(document).ready(function() {
    // Initializes an empty array to store cart items
    let cart = [];

    // Function to update the display of the cart items
    function updateCartDisplay() {
        // Clears the current cart items display
        $('#cart-items').empty();
        // Iterates through each item in the cart array
        // Appends a new list item to the cart-items element with the book's title and author
        cart.forEach(item => {
            $('#cart-items').append('<li>' + item.title + ' by ' + item.author + '</li>');
        });
    }

    // Adds an event listener for the click event on elements with the class 'add-to-cart'
    $('.add-to-cart').click(function() {
        // Retrieves the book ID, title, and author from the data attributes of the clicked element
        const bookId = $(this).data('book-id');
        const bookTitle = $(this).data('book-title');
        const bookAuthor = $(this).data('book-author');

        // Creates an object for the book with the retrieved data
        const book = {
            id: bookId,
            title: bookTitle,
            author: bookAuthor
        };

        // Adds the book object to the cart array
        cart.push(book);
        updateCartDisplay();
    });

    // Adds an event listener for the click event on the element with ID 'simulate-purchase'
    // Displays an alert with the number of books in the cart
    // Clears the cart array
    $('#simulate-purchase').click(function() {
        alert('Purchase simulated! ' + cart.length + ' books bought.');
        cart = [];
        updateCartDisplay();
    });
});
