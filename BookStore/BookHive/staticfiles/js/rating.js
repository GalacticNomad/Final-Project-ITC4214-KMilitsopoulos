// Function to retrieve the value the cookie
//Users can perform actions without noticing the underlying security measures protecting their interactions.
function getCookie(name) {
    
    // I Initialize the variable to hold the cookie value

    let cookieValue = null;

    //https://www.w3schools.com/howto/howto_css_star_rating.asp
    // I check if there are any cookies set
    // then split the cookies string into individual cookies
    // Loop through each cookie
    // Check if the cookie name matches the desired name
    // Decode and assign the cookie value
    if (document.cookie && document.cookie !== '') {

        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$(document).ready(function() {
    // Initialize the rating value to 0
    let ratingValue = 0;


    // Add a click event listener to each star in the rating element
    // Get the rating value from the data attribute of the clicked star
    // Set the hidden input field with the rating value
    // Remove the 'checked' class from all stars to reset the display
    // Add the 'checked' class to the clicked star and all previous stars
    $('.rating .fa-star').on('click', function() {
        ratingValue = $(this).data('value');
        $('#rating-value').val(ratingValue);
        $('.rating .fa-star').removeClass('checked');
        $(this).prevAll().addBack().addClass('checked');
    });

    $('#rating-form').on('submit', function(event) {
        // Prevent the default form submission
        event.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: "POST",
            headers: { 'X-CSRFToken': csrftoken },
            data: $(this).serialize(),
            success: function(data) {
                // Check if the response indicates success
                if (data.success) {
                    // Update the current rating display with the new rating
                    $('#current-rating').html('<h3>Current Rating: ' + data.rating + '</h3>');
                }
            }
        });
    });
});