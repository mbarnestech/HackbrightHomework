'use strict';

// array of melons
let melonsToAdd = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba', 'Sharlyn', 
                    'Xigua', 'Ogen', 'Christmas', 'Christmas', 'Christmas', 
                    'Christmas', 'Watermelon', 'Sharlyn', 'Xigua','Cantaloupe', 
                    'Christmas', 'Watermelon', 'Christmas','Sharlyn', 'Christmas', 
                    'Cantaloupe', 'Casaba', 'Cantaloupe','Santa Claus', 'Horned Melon', 
                    'Watermelon', 'Ogen','Horned Melon', 'Cantaloupe', 'Xigua', 
                    'Horned Melon', 'Sharlyn','Horned Melon', 'Sharlyn', 'Cantaloupe', 
                    'Christmas','Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 
                    'Xigua','Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
                    'Watermelon', 'Santa Claus', 'Casaba'];

// function to count the number of times each melon is in the list
function countMelons(melonsToAdd){

    let melonCounts = {};

    for (const melon of melonsToAdd){
        if (melonCounts.hasOwnProperty(melon)){
            melonCounts[melon] ++;
        } else {
            melonCounts[melon] = 1;
        }
    }
    return melonCounts;
}

console.log(countMelons(melonsToAdd));