#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let l = 0; l < this.height; l++) {
      let r = '';
      for (let b = 0; b < this.width; b++) {
        r += 'X';
      }
      console.log(r);
    }
  }
}
module.exports = Rectangle;
