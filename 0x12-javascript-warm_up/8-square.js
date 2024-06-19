#!/usr/bin/node
const { argv } = require('node:process');

if (isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  const squareSize = parseInt(argv[2]);
  let square = '';
  for (let i = 0; i < squareSize; i++) {
    square += 'X';
  }
  for (let i = 0; i < squareSize; i++) {
    console.log(square);
  }
}
