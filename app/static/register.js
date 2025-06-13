document.getElementById("")

fetch("127.0.0.1:5000/register")
    .then(response => console.log(response))
    .catch(error => console.error(`Error: ${error}`))
    