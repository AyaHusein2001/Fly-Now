const form = document.querySelector('form');
const errorDiv = document.getElementById('error-message');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
// submitting the login form info , get the result . 

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    
    try {
        const response = await fetch('/login-user', {
            method: 'POST', 
            body: formData 
        });
        const result = await response.json();

        if (result.success) {
            //storing user information after logging in, in the local storage

            localStorage.setItem('loggedin', true);
            localStorage.setItem('user_type', result.user.user_type);
            window.location.href = '/';
        } else {
            //show error message if email or password is incorrect .
            errorDiv.innerText='Invalid Email or Password';
        }
    } catch (error) {
        errorDiv.innerText="Couldn't log you in , try again later";
    }
});
// when user focuses on input , error goes on .
function focusedOnInput(){
    errorDiv.innerText="";

};
emailInput.addEventListener('focus',focusedOnInput);
passwordInput.addEventListener('focus',focusedOnInput);