const logintag = document.getElementById('login-tag')
const signuptag = document.getElementById('signup-tag')
const logouttag = document.getElementById('logout-tag')
if (localStorage.getItem("loggedin")) {
    console.log(localStorage.getItem("loggedin"))
    logintag.className = 'invisible-tag'
    signuptag.className = 'invisible-tag'
    logouttag.className = 'visible-tag'
}
function logout() {
    localStorage.removeItem('loggedin',false)
    logintag.className = 'visible-tag'
    signuptag.className = 'visible-tag'
    logouttag.className = 'invisible-tag'
}
logouttag.addEventListener('click',logout)