#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - 1) > 0) {
    const tmp = list[len];
    list[len] = list[i];
    list[i] = tmp;
    i++;
    len--;
  }
  return list;
};
