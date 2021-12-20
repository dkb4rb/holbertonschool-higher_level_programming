#!/usr/bin/node
const { argv } = require('process');
const value = parseInt(argv[2]);
const value2 = parseInt(argv[3]);
if (isNaN(value)) {
  console.log(value);
} else if (isNaN(value2)) {
  console.log(value2);
} else {
  console.log(value + value2);
}
