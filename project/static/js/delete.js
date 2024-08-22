document.addEventListener('DOMContentLoaded', function () {
    $('#delete-book-btn').click(function () {
        var bookId = $('#links').data('book-id');
        var csrfToken = $('#links').data('csrf-token');

        $.ajax({
            type: 'POST',
            url: '',
            data: {
                'book_id': bookId,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function () {
                location.assign("/view_books") ;

            },
            error: function (xhr, textStatus, errorThrown) {
                console.error(xhr.statusText);
            }
        });
    });
});
