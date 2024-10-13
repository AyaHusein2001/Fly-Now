const form = document.querySelector("form");
const errorDiv = document.getElementById("error-message");
const flightNumberInput = document.getElementById("flight-number");

// submit the flight details , get the result , show error message , if flight number is repeated . 
form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = new FormData(form);

  try {
    const response = await fetch("/insert-flight", {
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
  
  // Format the date and time in local time zone
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const formattedDateTime = `${year}-${month}-${day}T${hours}:${minutes}`;

  document.getElementById('departure_time').value = formattedDateTime;
  document.getElementById('arrival_time').value = formattedDateTime;
};