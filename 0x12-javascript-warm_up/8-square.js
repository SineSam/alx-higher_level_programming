#!/usr/bin/node
const i = process.argv[2];
if (isNaN(i)) {
  console.log('Missing size')
} else {
  for (let x = 0; x < i; x++) {
	  console.log('X'.repeat(i));
  }
}
  
