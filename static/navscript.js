const logintag = document.getElementById("login-tag");
const signuptag = document.getElementById("signup-tag");
const logouttag = document.getElementById("logout-tag");
const addflighttag = document.getElementById("addflight-tag");
const reservationstag = document.getElementById("reservations-tag");

const bookbuttons = document.querySelectorAll(".submit-button");
const flightnumbers = document.querySelectorAll(".flight-number");
const flightcards = document.querySelectorAll(".flight-card");

if (localStorage.getItem("loggedin")) {

  console.log(localStorage.getItem("loggedin"));
  logintag.classList.remove("visible-tag");
  logintag.classList.add("invisible-tag");
  signuptag.classList.remove("visible-tag");
  signuptag.classList.add("invisible-tag");
  logouttag.classList.remove("invisible-tag");
  logouttag.classList.add("visible-tag");


  for (let index = 0; index < flightcards.length; index++) {
    
    const flightNumber=flightnumbers[index].innerHTML
    
    const bookbuttondiv = document.createElement("div");
    const bookbutton = document.createElement("a");

    bookbuttondiv.className = "submit-button";
    bookbuttondiv.appendChild(bookbutton);
    if(localStorage.getItem('user_type')==1){

      bookbutton.href = `book?flight_number=${flightNumber}&user_id=${localStorage.getItem('user_id')}`;
      bookbutton.textContent = "Book";
    }
    else if(localStorage.getItem('user_type')==2){
      bookbutton.href = `editflight?flight_number=${flightNumber}`;
      bookbutton.textContent = "Edit";
    }

    flightcards[index].appendChild(bookbuttondiv);

  }


}

if(localStorage.getItem("user_type")==2){
    addflighttag.classList.remove("invisible-tag");
    addflighttag.classList.add("visible-tag");
}


if(localStorage.getItem("user_type")==1){
  
  reservationstag.classList.remove("invisible-tag");
  reservationstag.classList.add("visible-tag");
  reservationstag.href=`/reservations?user_id=${localStorage.getItem('user_id')}`
}

function logout() {
  localStorage.removeItem("loggedin");
  localStorage.removeItem("user_type");
  localStorage.removeItem("user_id");

  logintag.classList.remove("invisible-tag");
  logintag.classList.add("visible-tag");
  signuptag.classList.remove("invisible-tag");
  signuptag.classList.add("visible-tag");
  logouttag.classList.remove("visible-tag");
  logouttag.classList.add("invisible-tag");

  addflighttag.classList.remove("visible-tag");
    addflighttag.classList.add("invisible-tag");

  for (let index = 0; index < flightcards.length; index++) {
    
    



    flightcards[index].removeChild(bookbuttons[index]);

  }
  //   bookbuttons.forEach((bookbutton) => {
  //     bookbutton.classList.remove("invisible-tag");
  //     bookbutton.classList.add("visible-tag");
  //   });
}


logouttag.addEventListener("click", logout);
