let userName = document.getElementById('name');
let mail = document.getElementById('mail');
let submit = document.getElementById('submit');
let message = document.getElementById('message');
console.log(message);

function mailFormatCheck() {
    if (mail.value.includes('@gmail.com') || mail.value.includes('@yahoo.com')) {
        return true;
    }
    else {
        return false;
    }
}

submit.onclick = function (e) {
    e.preventDefault();
    if (mailFormatCheck() && userName.value != '' && message.value != '') {
        let subject = 'Contact';
        window.open(`mailto:semsemsama2004@gmail.com?subject=` + encodeURIComponent(subject) + '&body=' + encodeURIComponent(message.value));
    }
}