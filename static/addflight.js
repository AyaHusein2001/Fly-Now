const form = document.querySelector("form");
const errorDiv = document.getElementById("error-message");
const flightNumberInput = document.getElementById("flight-number");
const flightPriceInput = document.getElementById("flight-price");

const departureTimeInput = document.getElementById("departure_time");
const arrivalTimeInput = document.getElementById("arrival_time");


form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = new FormData(form);

  const flightNumber = parseInt(flightNumberInput.value, 10);
  const flightPrice = parseInt(flightPriceInput.value, 10);

  // Validate if the flight number is negative
  if (flightNumber < 0) {
    errorDiv.innerText = "Please enter a valid flight number.";
    return;
  }
  // Validate if the flight price is negative
  if (flightPrice < 0) {
    errorDiv.innerText = "Please enter a valid flight price.";
    return;
  }

 
  errorDiv.innerText = "";

  // Check if all required form fields are filled
  let allFieldsValid = true;

  
  form.querySelectorAll("input[required]").forEach((input) => {
    if (!input.value.trim()) {
      allFieldsValid = false;
      errorDiv.innerText = "Please enter correct values in all fields.";
      return;
    }
  });

 
  if (!allFieldsValid) return;

  // Check if departure time is in the future
  const now = new Date();
  const departureTime = new Date(departureTimeInput.value);
  const arrivalTime = new Date(arrivalTimeInput.value);

  if (departureTime <= now) {
    errorDiv.innerText = "You cannot insert an old flight. Please select a future departure time.";
    return;
  }

  // Check if arrival time is after the departure time
  if (arrivalTime <= departureTime) {
    errorDiv.innerText = "The Flight Departure time cannot be after or the same as its Arrival time.";
    return;
  }

  try {
    const response = await fetch("/addflight", {
      method: "POST",
      body: formData,
    });
    const result = await response.json();

    if (result.success) {
      window.location.href = "/";
    } else {
      errorDiv.innerText = result.error;
      
    }
  } catch (error) {
    errorDiv.innerText = "Couldn't add this flight , try again later";
  }
});
// when user focuses on input , error goes on .
function focusedOnInput() {
  errorDiv.innerText = "";
}
flightNumberInput.addEventListener("focus", focusedOnInput);

/* setting the deprature time , the arrival time initial value with now */
window.onload = function () {
  const now = new Date();

  
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  const hours = String(now.getHours()).padStart(2, "0");
  const minutes = String(now.getMinutes()).padStart(2, "0");
  const formattedDateTime = `${year}-${month}-${day}T${hours}:${minutes}`;

  document.getElementById("departure_time").value = formattedDateTime;
  document.getElementById("arrival_time").value = formattedDateTime;
};
