#!/usr/bin/node
const SquareN = require('./5-square');

class Square extends SquareN {
  charPrint (c) {
    let line = '';
    if (c !== undefined) {
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
