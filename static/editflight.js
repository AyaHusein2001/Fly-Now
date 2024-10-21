const form = document.querySelector("form");
const errorDiv = document.getElementById("error-message");
const flightPriceInput = document.getElementById("flight-price");

// Clear previous error messages
errorDiv.innerText = "";
form.addEventListener("submit", function (event) {
  // Check if all required form fields are filled
  let allFieldsValid = true;
  // Validate if the flight price is negative
  if (flightPrice < 0) {
    errorDiv.innerText = "Please enter a valid flight price.";
    event.preventDefault();
    return;
  }

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

