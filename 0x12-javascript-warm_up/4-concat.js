#!/usr/bin/node
const concat = ' is ';
console.log(typeof process.argv[2] === 'undefined' ? process.argv[2] + concat + process.argv[2] : process.argv[2] + concat + process.argv[3]);
