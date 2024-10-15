const form = document.querySelector('form');
const errorDiv = document.getElementById('error-message');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const userTypeSelect = document.getElementById('user_type');
const employeeNumberDiv = document.getElementById('employee-number-div');
const employeeNumberInput = document.getElementById('employee-number');
const phoneNumberInput = document.getElementById('phone_number');

// Show/hide the employee number field based on user type
userTypeSelect.addEventListener('change', function() {
    if (userTypeSelect.value === '2') {
        employeeNumberDiv.style.display = 'block';
        employeeNumberInput.required = true; // Make it required for admins
    } else {
        employeeNumberDiv.style.display = 'none';
        employeeNumberInput.required = false;
    }
});

// submitting the user info , get the result . 
form.addEventListener('submit', async function(event) {
    event.preventDefault();

    //forcing user to enter a long password for security
    if(passwordInput.value.length<8){
        errorDiv.innerText='password must be more than 8 characters';
        return;
    }
    if(phoneNumberInput.value.length<7||parseInt(phoneNumberInput.value)<0){
        errorDiv.innerText='Enter correct phone number';
        return;
    }
    if(employeeNumberInput){
        if(employeeNumberInput.value<0){

            errorDiv.innerText='Enter correct employee number';
            return;
        }
    }
    
    const formData = new FormData(form);

    // const password = formData.get('password');

    try {
        // const salt = await bcrypt.genSalt(10); 
        // const hashedPassword = await bcrypt.hash(password, salt); 
        

        // formData.set('password', hashedPassword);
        const response = await fetch('/insert-user', {
            method: 'POST', 
            body: formData 
        });
        const result = await response.json();

        if (result.success) {
            
            //storing user information after signing up in the local storage
            localStorage.setItem('loggedin', true);
            localStorage.setItem('user_type', result.user.user_type);
            window.location.href = '/';
        } else {
            //show error message if email used in signing up before .

            errorDiv.innerText=result.error;
            
        }
    } catch (error) {
        
        errorDiv.innerText="Couldn't sign you up , try again later"
        // errorDiv.innerText=error
    }
});
// when user focuses on input , error goes on .
function focusedOnInput(){
    errorDiv.innerText=""

}
emailInput.addEventListener('focus',focusedOnInput);
employeeNumberInput.addEventListener('focus',focusedOnInput);
phoneNumberInput.addEventListener('focus',focusedOnInput);
