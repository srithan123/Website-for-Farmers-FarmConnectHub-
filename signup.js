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