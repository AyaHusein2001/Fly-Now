const form = document.querySelector("form");
const errorDiv = document.getElementById("error-message");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const userTypeSelect = document.getElementById("user_type");
const employeeNumberDiv = document.getElementById("employee-number-div");
const employeeNumberInput = document.getElementById("employee-number");
const phoneNumberInput = document.getElementById("phone_number");

// Show/hide the employee number field based on user type
userTypeSelect.addEventListener("change", function () {
  if (userTypeSelect.value === "2") {
    employeeNumberDiv.style.display = "flex";
    employeeNumberInput.required = true; // Make it required for admins
  } else {
    employeeNumberDiv.style.display = "none";
    employeeNumberInput.required = false;
  }
});


form.addEventListener("submit", async function (event) {
  event.preventDefault();

  //forcing user to enter a long password for security
  if (passwordInput.value.trim().length < 8) {
    errorDiv.innerText = "Password must be more than 8 characters not including spaces";
    return;
  }
  if (
    phoneNumberInput.value.length < 7 ||
    parseInt(phoneNumberInput.value) < 0 || phoneNumberInput.value.length > 15
  ) {
    errorDiv.innerText = "Enter correct phone number";
    return;
  }
  if (employeeNumberInput) {
    if (employeeNumberInput.value < 0) {
      errorDiv.innerText = "Enter correct employee number";
      return;
    }
  }

  const formData = new FormData(form);
  
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

  // const password = formData.get('password');

  try {
    // const salt = await bcrypt.genSalt(10);
    // const hashedPassword = await bcrypt.hash(password, salt);

    // formData.set('password', hashedPassword);
    const response = await fetch("/signup", {
      method: "POST",
      body: formData,
    });
    const result = await response.json();

    if (result.success) {
      //storing user information after signing up in the local storage
      localStorage.setItem("loggedin", true);
      localStorage.setItem("user_type", result.user.user_type);
      window.location.href = "/";
    } else {

      errorDiv.innerText = result.error;
    }
  } catch (error) {
    errorDiv.innerText = "Couldn't sign you up , try again later";
  }
});
function focusedOnInput() {
  errorDiv.innerText = "";
}
emailInput.addEventListener("focus", focusedOnInput);
employeeNumberInput.addEventListener("focus", focusedOnInput);
phoneNumberInput.addEventListener("focus", focusedOnInput);
