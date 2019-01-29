// Logical operators
if (x > 10 && x < 30) {
	console.log('Between 10 and 30');
} else if (x > 31 || x < 11) {
	console.log('Not between 10 and 30');
} else if (!(x < 0)) {
	console.log('Number is positive');
}


// while loop
let i = 0;
while (i < 5) {
	console.log(i);
	i++;
}


// function declarations
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

