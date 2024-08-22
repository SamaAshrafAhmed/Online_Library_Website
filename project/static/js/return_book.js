document.addEventListener('DOMContentLoaded', function () {
    function returnBook(element, bookId) {
        const csrftoken = document.getElementById('csrf_token').value;

        fetch('/return_book/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'book_id': bookId })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const row = element.closest('tr');
                    const statusCell = row.querySelectorAll('td')[2];
                    statusCell.textContent = 'Returned';
                    element.remove(); // Remove the return button
                } else {
                    alert('Failed to return the book.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
    }

    // Attach the function to window so it can be called from HTML
    window.returnBook = returnBook;
});
