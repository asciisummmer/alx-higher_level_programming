#!/usr/bin/node
const myList = require('./100.data.js').list;

myList.map((value, index) => {
  return value * index;
});
