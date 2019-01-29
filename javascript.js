// Given a DNA strand, return its compliment
function getDNACompliment(dna) {
	dna = dna.toUpperCase();
	let dnaCompliment = '';
	for (let i = 0; i < dna.length; i++) {
		if (dna[i] === 'A') {
			dnaCompliment += 'T'
		} else if (dna[i] === 'T') {
			dnaCompliment += 'A'
		} else if (dna[i] === 'C') {
			dnaCompliment += 'G'
		} else {
			dnaCompliment += 'C'
		}
	}
	return dnaCompliment
};