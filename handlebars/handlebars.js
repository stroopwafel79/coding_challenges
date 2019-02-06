// AJAX request
// TODO make request with jQuery

// create new AJAX request object
//const ourRequest = new XMLHttpRequest();

// using the AJAX req object, make the AJAX call
// ourRequest.open('GET', url);
// upon loading, check if response is ok
// ourRequest.onload = function() {
//   if (ourRequest.status >= 200 && ourRequest.status < 400) {

//     var data = JSON.parse(ourRequest.responseText);
//     createHTML(data);
//   } else {
//     console.log("We connected to the server, but it returned an error.");
//   }
// };

// ourRequest.onerror = function() {
//   console.log("Connection error");
// };

// ourRequest.send();
// End AJAX request

// Now make AJAX request using JQuery - MUUUUUCH Easier
const url = 'https://learnwebcode.github.io/json-example/pets-data.json'
const ourRequest = $.get(url, createHTML);



Handlebars.registerHelper("calculateAge", function(birthYear) {
  var age = new Date().getFullYear() - birthYear;

  if (age > 0) {
    return age + " years old";
  } else {
    return "Less than a year old";
  }

});

function createHTML(petsData) {
  var rawTemplate = document.getElementById("petsTemplate").innerHTML;
  var compiledTemplate = Handlebars.compile(rawTemplate);
  var ourGeneratedHTML = compiledTemplate(petsData);

  var petsContainer = document.getElementById("pets-container");
  petsContainer.innerHTML = ourGeneratedHTML;
}