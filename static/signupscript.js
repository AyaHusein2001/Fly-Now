const form = document.querySelector('form')

function submitted() {
    localStorage.setItem('loggedin',true)
}
form.addEventListener('submit',submitted)