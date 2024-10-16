const ageInput = document.getElementById("age");
const phoneNumberInput = document.getElementById("phone_number");
const ageError = document.getElementById("ageError");
const phoneError = document.getElementById("phoneError");
const form = document.getElementById("bookingForm");
const errorDiv = document.getElementById("error-message");

ageError.style.display = "none";
phoneError.style.display = "none";

form.addEventListener("submit", function (event) {
  // Clear previous error messages
  errorDiv.innerText = "";

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
  if (!allFieldsValid) {
    event.preventDefault();
    return;
  }

  const ageValue = parseInt(ageInput.value);
  //restrict age between 12 & 99
  if (ageValue < 12 || ageValue > 99) {
    ageError.style.display = "block";
    event.preventDefault();
  } else {
    ageError.style.display = "none";
  }

  const phoneValue = parseInt(phoneNumberInput.value);

  if (phoneValue < 0 || phoneNumberInput.value.length < 7) {
    phoneError.style.display = "block";
    event.preventDefault();
  } else {
    phoneError.style.display = "none";
  }
});

// when user focuses on input , error goes on .
function focusedOnInput() {
  ageError.style.display = "none";
}
// when user focuses on input , error goes on .
function focusedOnPhoneInput() {
  phoneError.style.display = "none";
}
ageInput.addEventListener("focus", focusedOnInput);
phoneNumberInput.addEventListener("focus", focusedOnPhoneInput);
