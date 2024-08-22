
document.addEventListener('DOMContentLoaded', function () {
    var logoutButton = document.getElementById('logout');
    if (logoutButton) {
        logoutButton.addEventListener('click', function () {
            fetchLogout();
        });
    } else {
        console.log("Logout button not found in the document.");
    }
});

function fetchLogout() {
    fetch('/logout', {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'loggedout') {
                window.location.href = "/logout_confirmation";
            } else {
                alert('Logout Failed!');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
