const fs = require('fs');
const handlebars = require('handlebars');

const inFile = './handlebars.hbs';
const outFile = './report1.html';

// load JSON directly using the node.js require function
const data = require('./handlebars.json');

// retrieve our template from the file
const source = fs.readFileSync(inFile, 'utf8');
// compile the template in strict mode
const template = handlebars.compile(source, { strict: true });

const result = template(data);

console.log(result);

// write the results to an HTML file rather than the console
fs.writeFileSync(outFile, result);
console.log(`File written to ${outFile}`);
