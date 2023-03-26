'use strict';

/** ********************
 Make an Event Handler
********************* */

document.querySelector('#popup-alert-button').addEventListener('click', (evt) => alert('you clicked the button'));
/** ***********************
Practice Your Times Tables
************************ */

// add event listener to form, listening for submission
document.querySelector('#multiplying-form').addEventListener('submit', (evt) => {
  // prevent event default (following /nope)
  evt.preventDefault();
  // create empty multiples array
  let multiples = [];
  // get value of mults of dropdown menu
  const mults = document.querySelector('#mults-of').value
  // get value of max field
  const max = Number(document.querySelector('#max').value)
  // populate multiples array
  for (let i = 0; i <= max; i++) {
    if (i % mults === 0){
      multiples.push(i)
    }
  }
  console.log(multiples)
});

/** **************
An Agreeable Form
*************** */

function agree(evt){
  // prevent /oh no don't go here action
  evt.preventDefault();
  //get favorite food
  const food = document.querySelector("#favorite-food-input").value
  document.querySelector("#agreeable-text").innerHTML = `I like ${food}, too.`

}

document.querySelector("#agreeable-form").addEventListener('submit', agree)
/** ****************
Five colored primes
***************** */

const PRIME_COLORS = ['orange', 'midnightblue', 'darkgoldenrod', 'green', 'purple'];

function makePrimes(){
  let primes = [2];
  let lastPrime = Number(document.querySelector('.prime-circle:last-child').innerHTML)
  let n = 3;
  let newPrimes = [];
  while (newPrimes.length < 5){
    for (const num of primes){
      if (n % num === 0){
        break
      } else if (num === primes[primes.length - 1]) {
        primes.push(n)
        if (n > lastPrime) {
          newPrimes.push(n)
        }
      }
    }
    n++;
  }
  for (let i = 0; i < 5; i++){
    document.querySelector("#prime-circle-area").insertAdjacentHTML('beforeend', `<div class="prime-circle" style="background-color: ${PRIME_COLORS[i]}">${newPrimes[i]}</div>`);
  }
}
document.querySelector("#make-prime-circles").addEventListener('click', makePrimes)





/** *********
Got Puppies?
********** */

// NOTE: DO NOT CHANGE THE CODE OF THIS FUNCTION
function showPuppies(results) {
  // get the URL for the puppy photo out of the results object
  const puppyURL = results.url;
  const puppyDiv = document.querySelector('#puppies-go-here');
  // clear anything currently in the div
  puppyDiv.innerHTML = null;
  // add the img element
  puppyDiv.insertAdjacentHTML('beforeend', `<img src=${puppyURL} alt="puppy-image">`);
}

document.querySelector("#puppy-form").addEventListener('submit', (evt)=>{
  evt.preventDefault();

  fetch(`/puppies.json?num-puppies=${document.querySelector('#num-puppies').value}`)
    .then((results)=>results.json())
    .then((data)=>showPuppies(data))

});