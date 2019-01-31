const handlebars = require('handlebars');

// our data source
const data = {
  company: "Freddy's Fish Farm",
  phone: '619-555-1212',
  owner: {
    firstName: 'Freddy',
    lastName: 'Fishman'
  }
};

// our template
const source = `
<h1>Aquaponics Report for {{company}}</h1>
<p>Owner: {{owner.firstName}} {{owner.lastName}}</p>
<p>Phone: {{phone}}</p>
`;

// Use strict mode so that Handlebars will throw exceptions if we
// attempt to use fields in our template that are not in our data set.
const template = handlebars.compile(source, {strict: true});
const result = template(data);
console.log(result);
