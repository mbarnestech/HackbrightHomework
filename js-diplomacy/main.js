'use strict';

// FIRST TASK: COLOR CHANGE BUTTON

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

// SECOND TASK: "When someone submits the form, prevent its default behavior 
    // (it should not redirect to a new page). Instead, validate the input in 
    // the text input with ID “number-input”. If it is not a number or greater 
    // than or equal to 10, change the text of the element with ID “formFeedback” 
    // to say ‘Please enter a smaller number’. Otherwise, change the text of that 
    // element to say “You are good to go!.”"

