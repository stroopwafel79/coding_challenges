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
const petsData = $.get(url, createHTML);
// Create helper function by useing handlebars .registerHelper method
// argument 1 is what we want the helper to be named
// argument 2 is the anonymous function being created
// whatever function returns is value used in the template
Handlebars.registerHelper("calculateAge", (birthYear) => {
  const age = new Date().getFullYear() - birthYear;

  if (age > 0) {
    return age + " years old";
  } else {
    return "Less than a year old";
  }

});

function createHTML(petsData) {
  // get the string of text inside the template
  const rawTemplate = $("#petsTemplate").html();
  console.log(`rawTemplate ${rawTemplate}`);
  // const rawTemplate = document.getElementById("petsTemplate").innerHTML;

  // turns compiledTemplate into a usable function
  const compiledTemplate = Handlebars.compile(rawTemplate, { strict: true });
  console.log(`compiledTemplate ${compiledTemplate}`);
  // pass our data to the template function so it can create HTML
  const ourGeneratedHTML = compiledTemplate(petsData);
  console.log(`ourGeneratedHTML: ${ourGeneratedHTML}`);
  $("#pets-container").html(ourGeneratedHTML);
  // const petsContainer = document.getElementById("pets-container");
  // const jqpetsContainer = $("#pets-container");
  // petsContainer.innerHTML = ourGeneratedHTML;
}