const form = document.querySelector("form");
const errorDiv = document.getElementById("error-message");
const flightPriceInput = document.getElementById("flight-price");

const departureTimeInput = document.getElementById("departure_time");
const arrivalTimeInput = document.getElementById("arrival_time");

// Clear previous error messages
errorDiv.innerText = "";

form.addEventListener("submit", function (event) {
  // Validate if the flight price is negative
  const flightPrice=flightPriceInput.value;
  if (flightPrice < 0) {
    errorDiv.innerText = "Please enter a valid flight price.";
    
    event.preventDefault();
    return;
  }
  
    // Check if departure time is in the future
    const now = new Date();
    const departureTime = new Date(departureTimeInput.value);
    const arrivalTime = new Date(arrivalTimeInput.value);
  
    if (departureTime <= now) {
      errorDiv.innerText = "You cannot insert an old flight. Please select a future departure time.";
      event.preventDefault();
      return;
    }
  
    // Check if arrival time is after the departure time
    if (arrivalTime <= departureTime) {
      errorDiv.innerText = "The Flight Departure time cannot be after or the same as its Arrival time.";
      event.preventDefault();
      return;
    }
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

