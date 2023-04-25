#!/usr/bin/node
const request = require('request');
const episode_no = process.argv[2];
let url = 'https://swapi-api.hbtn.io/api/films/';
request(url + episode_no, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
