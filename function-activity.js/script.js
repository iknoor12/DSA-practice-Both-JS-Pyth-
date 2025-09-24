const prompt = require('prompt-sync')();

// Multiplication Table Function
// ➤ Write a function that takes a single positive integer n and prints its multiplication table from 1 to 10.

// let n = prompt("Enter a single positive number: ");

// function multiplication(n) {
//     for(let i=1; i<=10; i++) {
//         let val = n * i;
//         console.log(n, "x", i, "=", val);
//     }
// }
// multiplication(n);





// Function Expression – Max of Two
// ➤ Write a function expression that takes two numbers as input and returns the greater number. 

// let n1 = prompt("Enter first positive number: ");
// let n2 = prompt("Enter second positive number: ");

// function maximum(n1, n2) {
//     if(n1 > n2){
//         console.log("Maximum number is", n1);
//     } else {
//         console.log("Maximum number is", n2); 
//     }
// }
// maximum(n1, n2);




// Function Expression – Capitalize Words
// ➤ Create a function expression that takes a string and returns a new string where the first letter of each word is capitalized.


// let str = prompt("Enter your word: ");

// function captilize(str) {
//     str = str.charAt(0).toUpperCase()+ str.slice(1);           /*It returns a substring starting from index 1 to the end of the string.So it removes the first character and gives you the rest.*/
//     console.log(str);   
// }
// captilize(str);




// Anonymous Function – Squared Numbers
// ➤ Create an anonymous function assigned to a variable that takes an array of numbers and returns a new array containing the squares of those numbers.

let arr = prompt("Enter some numbers: ");
let array = arr.split(" ").map(Number);

let newArray = array.map(i => i ** 2);
console.log(newArray);

// function squared(array) {
//     array.forEach(i => {
//         i **= 2;
        
//     }); 

// }
// squared(array);