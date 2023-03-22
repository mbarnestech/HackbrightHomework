'use strict';

// get the button with color-changer class
const colorChangerButton = document.querySelector('button.color-changer');

// get all elements with color-change class
const colorChangeClass = document.querySelectorAll('.color-change');

// listen for the 'click' event on the color change button
colorChangerButton.addEventListener('click', () => {
    // loop through each element with color-change class
    for (const item of colorChangeClass) {
        // add 'red' class to each element
        item.classList.add('red');
    }
});