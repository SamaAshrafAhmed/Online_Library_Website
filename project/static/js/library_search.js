// library_search.js

document.addEventListener('DOMContentLoaded', function () {
    $("#searchForm").submit(function (event) {
        event.preventDefault();

        var searchBy = $('input[name="search_by"]:checked').val();
        var searchTerm = $("#searchInput").val();

        $.ajax({
            url: "library_search",
            data: {
                search_by: searchBy,
                s: searchTerm,
            },
            success: function (data) {
                $("#booklist").html("");
                $.each(data.books, function (index, book) {

                    console.log("data: ", data)
                    console.log("book: ", book)


                    var bookItem = `
            <div class="book" style = "margin: 10px;" data-book-id= "${book.id}" onclick="openBook(this)">
              <div class="book_info">
              <img src="${book.cover_photo}" alt="${book.title} cover">
              <h2>${book.title}</h3>
              <p>Author: ${book.author}</p>
              <p>Category: ${book.category}</p>
              <p class="heart">❤</p>
              </div>
            </div>
          `;
                    $("#booklist").append(bookItem);
                });
            },
        });
    });

    function openBook(element) {
        book_id = element.getAttribute('data-book-id');
        user_id = userid.getAttribute('data-user-id');
        urltem = urltemp.getAttribute('data-url');
        role = userole.getAttribute('data-user-role')

        console.log(role, user_id, book_id)
        if (role == 'reader')
            url = urltem.replace('0/0', `${user_id}/${book_id}`);

        else if (role == 'admin') {
            url = urltem.replace('/0/', `/${book_id}/`);
        }

        console.log("url: ", url);

        window.location.href = url;
    }
});

function openBook(element) {
    book_id = element.getAttribute('data-book-id');
    user_id = userid.getAttribute('data-user-id');
    urltem = urltemp.getAttribute('data-url');
    role = userole.getAttribute('data-user-role')

    console.log(role, user_id, book_id)
    if (role == 'reader')
        url = urltem.replace('0/0', `${user_id}/${book_id}`);

    else if (role == 'admin') {
        url = urltem.replace('/0/', `/${book_id}/`);
    }

    console.log("url: ", url);

    window.location.href = url;
}