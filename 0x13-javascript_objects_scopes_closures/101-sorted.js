#!/usr/bin/node
const dict1 = require('./101-data.js').dict;
const dict2 = {};
for (const key in dict1) {
  const value = dict1[key];
  if (value in dict2) {
    dict2[value].push(key);
  } else {
    dict2[value] = [key];
  }
}
console.log(dict2);
