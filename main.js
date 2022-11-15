/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  document.getElementById("sidenavBtn").style.display = "none";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.body.style.backgroundColor = "white";
  document.getElementById("sidenavBtn").style.display = "block";
}

function validate() {
  var username = document.getElementById("userName").value;
  var password = document.getElementById("passWord").value;

  if (username == "B3NJI" && password == "dev") {
    window.open("https://b3nji23.github.io/about-me.html", _self);
  } else {
    alert("Login Failed!");
  }
}
