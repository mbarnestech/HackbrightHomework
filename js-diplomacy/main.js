'use strict';

// get the button with color-changer class
const colorChangerButton = document.querySelector('button.color-changer');

// get all elements with color-change class
const colorChangeClass = document.querySelectorAll('.color-change');

colorChangerButton.addEventListener('click', () => {
    for (const item of colorChangeClass) {
        item.classList.add('red');
    }
});