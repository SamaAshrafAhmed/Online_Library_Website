document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('logoutBtn2').addEventListener('click', function () {
        fetchLogout();
    });
});

function fetchLogout() {
    fetch( "logout", {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'loggedout') {
                window.location.href = "logout_confirmation";
            } else {
                alert('Logout Failed!');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
