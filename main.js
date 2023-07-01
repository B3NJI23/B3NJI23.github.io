let loggedIn = localStorage.getItem('loggedIn') || 'false';

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
function randomChoice(array) {
  const randomIndex = Math.floor(Math.random() * array.length);
  return array[randomIndex];
}

function generateHash() {
  let symbolsAndLetters = [];
  var hash = ''

  // Add symbols and letters
  for (let i = 33; i <= 126; i++) {
    symbolsAndLetters.push(String.fromCharCode(i))
  }

  for (let j of symbolsAndLetters) {
    hash += randomChoice(symbolsAndLetters)
    if (hash.length == 16) {
      break
    }
  }

  return hash
}

function validate() {
  var user1 = {}
  var user2 = {}

  const usernameHash = generateHash()
  const passwordHash = generateHash()

  const usernameHash2 = generateHash()
  const passwordHash2 = generateHash()

  const usernameInput = document.getElementById('username')
  const passwordInput = document.getElementById('password')

  const inputtedUsername = usernameInput.value
  const inputtedPassword = passwordInput.value

  user1['username'] = 'B3NJI'
  user1['password'] = 'admin.dev'
  user2['username'] = 'szeretlek'
  user2['password'] = 'szeretlek'

  if (inputtedUsername === user1['username'] && inputtedPassword === user1['password'] || inputtedUsername == user2['username'] && inputtedPassword == user2[passwordHash2]) {
    localStorage.setItem('loggedIn', 'true');
    alert('Successful login!');
    window.open('main.html', '_self');
  } else {
    alert('Wrong credentials!');
    usernameInput.value = '';
    passwordInput.value = '';
  }
}

function Redirect() {
  const loggedIn = localStorage.getItem('loggedIn');
  const currentPage = window.location.pathname;

  if (loggedIn !== 'true' && currentPage !== '/index.html') {
    window.location.href = 'index.html';
  }
}

function logOut() {
  alert('Logged out.')
  window.open('index.html', '_self')
  localStorage.setItem('loggedIn', 'false');
}