#!/usr/bin/node
let a = process.argv.slice(2);
let secondBiggest = 0;
if (a.length > 1) {
	const integers = a.map(Number);
	integers.sort((a, b) => b - a);
	secondBiggest = integers[1];
}
console.log(secondBiggest);
