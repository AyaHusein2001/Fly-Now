const form = document.querySelector('form');

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    const email = formData.get('email');
    const password = formData.get('password');

    try {

        const response = await fetch(`/login-user?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`);
        const result = await response.json();

        if (result.success) {
            localStorage.setItem('loggedin', true);
            localStorage.setItem('user_id', result.user.user_id);
            console.log(result)
            window.location.href = '/';
        } else {
            alert(result.error); 
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
