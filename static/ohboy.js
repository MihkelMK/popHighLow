function request(name) {
  let data = { nimi: name };

  return fetch('/game', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }).then((response) => response.json());
}

const updatePeople = (nimi) => {
  request(nimi).then((a) => {
    document.getElementsByClassName('skoor')[0].textContent =
      'Skoor: ' + a['score'];
    if ('võit' in a) {
      document.location.href = '/win';
    }

    let givenName = a['given'][0];
    let guessName = a['guess'][0];
    let givenNr = a['given'][1][0];
    let guessNr = a['guess'][1][0];

    document.getElementById('givenNr').textContent = givenNr;
    document.getElementById('guessNr').textContent = guessNr;
    document.getElementById('givenName').textContent = givenName;
    document.getElementById('guessName').textContent = guessName;
    document.getElementsByClassName(
      'given'
    )[0].style.cssText += `background-image: linear-gradient(rgba(0, 0, 0, 0.527),rgba(0, 0, 0, 0.5)), url(${a['given'][1][1]});`;
    document.getElementsByClassName(
      'guess'
    )[0].style.cssText += `background-image: linear-gradient(rgba(0, 0, 0, 0.527),rgba(0, 0, 0, 0.5)), url(${a['guess'][1][1]});`;
  });
};

const checkGuess = (guess) => {
  let givenNr = Number(document.getElementById('givenNr').textContent);
  let guessNr = Number(document.getElementById('guessNr').textContent);
  let guessName = document.getElementById('guessName').textContent;

  if (guess == 'rohkem' && givenNr <= guessNr) {
    updatePeople(guessName);
  } else if (guess == 'vähem' && givenNr >= guessNr) {
    updatePeople(guessName);
  } else {
    document.location.href = '/lose';
  }
};

updatePeople('start');
