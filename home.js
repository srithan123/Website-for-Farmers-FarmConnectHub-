var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";
}

/*code for login button pop*/

var modal = document.getElementById('main-block');

var btn = document.getElementById("loginButton");

btn.onclick = function() {
  modal.style.display = "block";
}

function closeModal() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target === modal) {
      modal.style.display = "none";
  }
}

/*code ends for login pop up*/

/*code for login check*/
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if ((username === "Srithan")  && (password === "Srithan")) {
        alert("You have successfully logged in.");
        location.reload();
        window.open("home.html", "_self");
    } else {
        loginErrorMsg.style.opacity = 1;
    }

    if ((username === "Vishnu") && (password === "Vishnu")) {
        alert("You have succesfully logged in.");
        location.reload();
        window.open("home.html", "_self");
    } else {
        loginErrorMsg.style.opacity = 1;
    }

    if ((username === "Nivas") && (password === "Nivas")) {
        alert("You have succesfully logged in.");
        location.reload();
        window.open("home.html", "_self");
    } else {
        loginErrorMsg.style.opacity = 1;
    }

    if ((username === "Prasad") && (password === "Prasad")) {
        alert("You have succesfully logged in.");
        location.reload();
        window.open("home.html", "_self");
    } else {
        loginErrorMsg.style.opacity = 1;
    }

    if ((username === "Dikshit") && (password === "Dikshit")) {
        alert("You have succesfully logged in.");
        location.reload();
        window.open("home.html", "_self");
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
/*code ended for login check*/

/*code for image sizing*/