const form = document.querySelector('form');
const errorDiv = document.getElementById('error-message');
const emailInput = document.getElementById('email');
// submitting the user info , get the result . 

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    
    try {
        const response = await fetch('/insert-user', {
            method: 'POST', 
            body: formData 
        });
        const result = await response.json();

        if (result.success) {
            
            //storing user information after signing up in the local storage
            localStorage.setItem('loggedin', true);
            localStorage.setItem('user_id', result.user.user_id);
            localStorage.setItem('user_type', result.user.user_type);
            window.location.href = '/';
        } else {
            //show error message if email used in signing up before .

            errorDiv.innerText=result.error;
            
        }
    } catch (error) {
        errorDiv.innerText="Couldn't sign you up , try again later"
    }
});
// when user focuses on input , error goes on .
function focusedOnInput(){
    errorDiv.innerText=""

}
emailInput.addEventListener('focus',focusedOnInput);
