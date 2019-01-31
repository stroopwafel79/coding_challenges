/////////////// Logical operators
if (x > 10 && x < 30) {
	console.log('Between 10 and 30');
} else if (x > 31 || x < 11) {
	console.log('Not between 10 and 30');
} else if (!(x < 0)) {
	console.log('Number is positive');
}


//////////////// while loop
let i = 0;
while (i < 5) {
	console.log(i);
	i++;
}


//////////////// function declarations
function multiply(x, y) {
	return x * y;
}
// OR
const multiply = function(x, y) {
	return x * y;
}
// OR
const multiply = (x, y) => {
	return x * y;
}

multiply(3, 2); // return 6


// with default value
function add(x, y=0) {
	return x + y;
}

add(3); // return 3 b/c y defaults to 0
add(3, 2); // return 5

////////////////// String formating use backticks
const name = 'Kristi';
const message = `Hello ${name}!`;

const msg = `
	This is a multiline
	comment that uses
	backticks.
`;


/////////////////// Lists/arrays
const states = ['CA', 'MA', 'FL'];
states.push('NY');

states[2]; // 'FL'
states.slice(2); // ['FL', 'NY'];
states.slice(2, 3); // ['FL']

states.includes('FL'); // true
states.includes('OR'); // false

//////////////////// Loop over lists/arrays
for (let state of states) {
	console.log(state);
}
// CA
// MA
// FL
// NY

// looping using forEach
states.forEach(function (state) {
	console.log(state);
});

// Loop over indicies of lists/arrays
for (let i = 0; i < states.length; i++) {
	console.log(`I love ${states[i]}!`);
}
// I love CA!
// I love MA!
// I love FL!
// I love NY!

// Behaves like ennumerate
states.forEach((state, i) => {
	console.log(`${i}, ${state}`);
});
// 0, CA
// 1, MA
// 2, FL
// 3, NY

//////////////////// MAPS are JavaScript's dictionaries
// MAPS are a list of lists, but behave like a dictionary
const capitals = new Map([
	['CA', 'Sacramento'],
	['MA', 'Boston'],
	['FL', 'Jacksonville'],
]);

capitals.set('NY', 'New York');
capitals.get('CA'); // Sacramento
caplitals.has('MA'); // true
capitals.keys(); // MapIterator {"CA", "MA", "FL", "NY"}
capitals.values(); // MapIterator {"Sacramento", "Boston", "Jacksonville", "New York"}
capitals.entries(); // MapIterator {"CA" => "Sacramento", "MA" => "Boston", "FL" => "Jacksonville", "NY" => "New York"}
capitals.size; // 4

if (capitals.has('CA')) {
	console.log('California'); 
}

// Loop over key, values of a Map
for (let [key, value] of capitals) {
	console.log(`${value} is the capital of ${key}`);
}
// OR
for (let [capital, state] of capitals) {
	console.log(`${capital} is the capital of ${state}`);
}

// Sets
const colors = new Set();
// OR
const myColors = new Set(
	['red', 'green', 'blue']
);

myColors.add('purple');
myColors.has('red'); // true

for (let color of myColors){
	console.log(color);
}


/////////////////// Create objects 
// Can create objects without a class
const cat = {
	name: 'Anna',
	color: 'tabby',
	age: 5
};

cat.disposition = 'Sweet';
cat.hasOwnProperty('name'); // true
Object.keys(cat); // (4) ["name", "color", "age", "disposition"]
Object.values(cat); // (4) ["Tater", "black", 14, "Sweet"]
Object.entries(cat); // (4) [Array(2), Array(2), Array(2), Array(2)]

//////////////////// More than none
undefined - No assigned value. Functions, by default, return Undefined
null - Explicitly having no value. More similar to None in Python
NaN - Not-a-Number. Gets returned when mathematical operations fail.
// Will result in false :
null, undefined, NaN, Empty string, 0, false


////////////////////// The DOM
// YOU MUST FIRST GET THE ELEMENT
document.querySelector("#id");
document.getElementById("id");
document.querySelectorAll(".class"); // array of elements by class name
document.querySelectorAll("p"); // array of elements by tag
const id = document.querySelector("#id");
console.dir(id);