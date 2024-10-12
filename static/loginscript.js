const form = document.querySelector('form');
const errorDiv = document.getElementById('error-message');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
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
            localStorage.setItem('loggedin', true);
            localStorage.setItem('user_id', result.user.user_id);
            localStorage.setItem('user_type', result.user.user_type);
            window.location.href = '/';
        } else {
            errorDiv.innerText='Invalid Email or Password';
        }
    } catch (error) {
        errorDiv.innerText="Couldn't log you in , try again later";
    }
});

function focusedOnInput(){
    errorDiv.innerText="";

};
emailInput.addEventListener('focus',focusedOnInput);
passwordInput.addEventListener('focus',focusedOnInput);