// PART 1: SHOW A FORTUNE

function showFortune() {
  fetch('/fortune')
    .then((fortunePromise)=>fortunePromise.text())
    .then((fortuneText)=>{
      document.querySelector('#fortune-text').innerHTML = fortuneText;
    })
}

document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER

function showWeather(evt) {
  evt.preventDefault();
  const zipcode = document.querySelector('#zipcode-field').value;
  const url = `/weather?zipcode=${zipcode}`;

  fetch(url)
    .then((response)=>response.json())
    .then((weatherInfo)=>{
      document.querySelector('#weather-info').innerHTML = weatherInfo.forecast;
    })
}

document.querySelector('#weather-form').addEventListener('submit', showWeather);
