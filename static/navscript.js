const loginTag = document.getElementById("login-tag");
const signupTag = document.getElementById("signup-tag");
const logoutTag = document.getElementById("logout-tag");
const addFlightTag = document.getElementById("addflight-tag");
const reservationsTag = document.getElementById("reservations-tag");

const cardsButtons = document.querySelectorAll(".submit-button");
const flightNumbers = document.querySelectorAll(".flight-number");
const flightCards = document.querySelectorAll(".flight-card");

if (localStorage.getItem("loggedin")) {
  // if user is logged in , hide login , sign up button , show logout button

  loginTag.classList.remove("visible-tag");
  loginTag.classList.add("invisible-tag");
  signupTag.classList.remove("visible-tag");
  signupTag.classList.add("invisible-tag");
  logoutTag.classList.remove("invisible-tag");
  logoutTag.classList.add("visible-tag");

  for (let index = 0; index < flightCards.length; index++) {
    const flightNumber = flightNumbers[index].innerHTML;
    const cardButtonDiv = document.createElement("div");
    const cardButton = document.createElement("a");
    cardButtonDiv.className = "submit-button";
    cardButtonDiv.appendChild(cardButton);

    /*
    if user is logged in , and he is a customer , allow him to book flights by
    showing the book button , allow him to see his reservations by adding a tag to the reservations page .
    if he is an admin , allow him to edit flight details by showing edit button ,
    allow him to add flights by adding a tag to the add flight page .
    */
    if (localStorage.getItem("user_type") == 1) {
      cardButton.href = `book?flight_number=${flightNumber}&user_id=${localStorage.getItem("user_id")}`;
      cardButton.textContent = "Book";

      reservationsTag.classList.remove("invisible-tag");
      reservationsTag.classList.add("visible-tag");
      reservationsTag.href = `/reservations?user_id=${localStorage.getItem("user_id")}`;

    } else if (localStorage.getItem("user_type") == 2) {
      cardButton.href = `editflight?flight_number=${flightNumber}`;
      cardButton.textContent = "Edit";

      addFlightTag.classList.remove("invisible-tag");
      addFlightTag.classList.add("visible-tag");
    }

    flightCards[index].appendChild(cardButtonDiv);
  }
}

/*
when user logs out , remove his details from the local storage ,
also remove the tags that allows him to add flight , or see his reaservations . he also no longer allowed to
book or edit flights .
*/

function logout() {

  localStorage.removeItem("loggedin");
  localStorage.removeItem("user_type");
  localStorage.removeItem("user_id");

  loginTag.classList.remove("invisible-tag");
  loginTag.classList.add("visible-tag");
  signupTag.classList.remove("invisible-tag");
  signupTag.classList.add("visible-tag");
  logoutTag.classList.remove("visible-tag");
  logoutTag.classList.add("invisible-tag");

  addFlightTag.classList.remove("visible-tag");
  addFlightTag.classList.add("invisible-tag");

  for (let index = 0; index < flightCards.length; index++) {
    flightCards[index].removeChild(cardsButtons[index]);
  }
}

logoutTag.addEventListener("click", logout);
