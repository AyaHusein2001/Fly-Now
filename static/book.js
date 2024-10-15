
const ageInput = document.getElementById("age");
const phoneNumberInput = document.getElementById("phone_number");
const ageError = document.getElementById("ageError");
const phoneError = document.getElementById("phoneError");
ageError.style.display = "none";
phoneError.style.display = "none";

document
  .getElementById("bookingForm")
  .addEventListener("submit", function (event) {
    const ageValue = parseInt(ageInput.value);
    //restrict age between 12 & 99
    if (ageValue < 12 || ageValue > 99) {
      ageError.style.display = "block";
      event.preventDefault();
    } else {
      ageError.style.display = "none";
    }

    const phoneValue = parseInt(phoneNumberInput.value);
    
    if (phoneValue < 0 || phoneNumberInput.value.length <7) {
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