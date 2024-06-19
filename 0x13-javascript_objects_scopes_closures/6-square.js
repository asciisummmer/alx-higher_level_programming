#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let line = '';
    if (c) {
      for (let i = 1; i <= this.width; i++) {
        line += c;
      }
    } else {
      for (let i = 1; i <= this.width; i++) {
        line += 'X';
      }
    }
    for (let i = 1; i <= this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
