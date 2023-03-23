function submitProfile(evt) {
  evt.preventDefault();

  // const gardenValue = ()
  const data = {
    name: document.querySelector('#name-field').value,
    age: document.querySelector('#age-field').value,
    occupation: document.querySelector('#occupation-field').value,
    salary: document.querySelector('[name="salary"]').value,
    educationLevel: document.querySelector('[name="education"]').value,
    state: document.querySelector('#state-field').value,
    // get boolean for city type checkboxes
    cityType: {rural: document.querySelector('[value="rural"]').checked,
      suburban: document.querySelector('[value="suburban"]').checked,
      urban: document.querySelector('[value="urban"]').checked},
    garden: { yes: document.querySelector('[value="yes"]').checked, no: 
      document.querySelector('[value="no"]').checked},
    tv: document.querySelector('[name="tv"]').value,
  };

  fetch('/api/profile', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {'content-type': 'application/json'},
  })
    .then((response)=>response.json())
    .then((jsonData)=>{
        document
          .querySelector('#profiles')
          .insertAdjacentHTML(
            "beforeend", `<p> ${jsonData.name} is a ${jsonData.occupation} and is ${jsonData.age}. </p` );
    });

}

document.querySelector('#profile-form').addEventListener('submit', submitProfile);
