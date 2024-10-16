const form = document.querySelector("form");
const errorDiv = document.getElementById("error-message");

// Clear previous error messages
errorDiv.innerText = "";
form.addEventListener("submit", function (event) {
  // Check if all required form fields are filled
  let allFieldsValid = true;

  // Iterate over all form elements
  form.querySelectorAll("input[required]").forEach((input) => {
    if (!input.value.trim()) {
      allFieldsValid = false;
      errorDiv.innerText = "Please enter correct values in all fields.";
      event.preventDefault();
      return;
    }
  });

  // Stop form submission if any field is empty
  if (!allFieldsValid) 
  {
    event.preventDefault();
    return;
  }
});

