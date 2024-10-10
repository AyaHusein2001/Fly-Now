const form = document.querySelector('form');

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
            console.log(result);
            window.location.href = '/';
        } else {
            alert(result.error); 
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
