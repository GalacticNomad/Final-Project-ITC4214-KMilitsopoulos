document.addEventListener('DOMContentLoaded', (event) => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');

    // Check if dark mode was previously enabled for persistence
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
    }

    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');

        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
        } else {
            localStorage.removeItem('darkMode');
        }
    });
});
