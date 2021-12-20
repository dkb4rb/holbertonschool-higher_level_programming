#!/usr/bin/node
const { argv } = require('process');

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let count = parseInt(argv[2]);
  while (count > 0) {
    console.log('C is fun');
    count--;
  }
}
