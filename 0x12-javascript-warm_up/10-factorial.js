#!/usr/bin/node
const { argv } = require('node:process');

function factorial (number) {
  if (isNaN(number) || number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}

factorial(parseInt(argv[2]));
