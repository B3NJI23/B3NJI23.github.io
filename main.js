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

function dropDownBox() {
  var open = document.getElementsByClassName('alert')[0];
  open.style.display = 'block';

  const expanded = document.getElementsByClassName('alert')[0];

  expanded.classList.toggle("alert-expanded");
}

function dropDownBoxClose() {
  var closed = document.getElementsByClassName('alert-expanded')[0];

  closed.style.display = 'none';
}

function calculator() {
  const softPity = 80;
  const hardPity = 90;

  var userPity = document.getElementsByClassName('pity-checker')[0].value;

  if (userPity > 0 && userPity < 90) {
      document.getElementById('result').innerHTML = `Soft pity 5⭐: ${softPity - userPity} wish múlva.\nGarantált 5⭐: ${hardPity - userPity} wish múlva.`;
  }

  else {
      document.getElementById('result').innerHTML = 'Hibás adat! Próbáld újra.';
  }

}

const button = document.getElementsByClassName('primogem-resin-calculator')[0];
button.addEventListener("click");