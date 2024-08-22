
document.addEventListener('DOMContentLoaded', function () {
    let booklist = document.getElementById('booklist');

    function toggleHeartColor(heart) {
        heart.classList.toggle('red-heart');
    }
    
    let listItems = document.querySelectorAll('.book')
    console.log(listItems)
    listItems.forEach(
        function (element) {
            element.onclick = function () {
                book_id = element.getAttribute('data-book-id');
                user_id = userid.getAttribute('data-user-id');
                urltem = urltemp.getAttribute('data-url');
                role = userole.getAttribute('data-user-role')

                console.log(role, user_id, book_id)
                if(role == 'reader')
                    url = urltem.replace('0/0', `${user_id}/${book_id}`);
                    
                else if (role == 'admin') {
                    url = urltem.replace('/0/', `/${book_id}/`);
                }
                 
                
                window.location.href = url;
                
              

            };
        });





    let hearts = document.querySelectorAll('.heart');

    hearts.forEach(
        function (element) {
            element.onclick = event => {
                let clickedHeart = event.target;
                toggleHeartColor(clickedHeart);
            }
        });



});

