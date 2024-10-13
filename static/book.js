const ageInput = document.getElementById("age");
ageError.style.display = "none";

document.getElementById("bookingForm").addEventListener("submit", function (event) {
    const ageError = document.getElementById("ageError");
    const ageValue = parseInt(ageInput.value);
    //restrict age between 12 & 99
    if (ageValue < 12 || ageValue > 99) {
      ageError.style.display = "block";
      event.preventDefault();
    } else {
      ageError.style.display = "none";
    }
  });

// when user focuses on input , error goes on .
function focusedOnInput(){
    ageError.style.display = "none";

};
ageInput.addEventListener("focus",focusedOnInput);
