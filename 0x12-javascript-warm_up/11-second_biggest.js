#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < argv.length; i++) {
    arr.push(parseInt(argv[i]));
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
