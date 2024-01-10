#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let l = 0; l < this.height; l++) {
      let r = '';
      for (let b = 0; b < this.width; b++) {
        r += c;
      }
      console.log(r);
    }
  }
}
module.exports = Square;
