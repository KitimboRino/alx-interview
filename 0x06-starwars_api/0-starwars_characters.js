#!/usr/bin/node
/* prints all characters of Star Wars movie passed as command-line argument */

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const getCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, res, body) => {
      if (err) return reject(err);
      resolve(JSON.parse(body).name);
    });
  });
};

request(url, async (err, res, body) => {
  if (err) {
    console.error(`Error fetching movie data: ${err}`);
    return;
  }

  try {
    const charactersArray = JSON.parse(body).characters;
    for (const character of charactersArray) {
      const name = await getCharacterName(character);
      console.log(name);
    }
  } catch (err) {
    console.error(`Error processing character data: ${err}`);
  }
});
