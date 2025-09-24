// PRACTICE   QUESTION   NUMBER  2  // 

// Takes a number as input and prints an inverted right-angled triangle pattern of *numbers*.  //

function reverseTriangle(n){
    for(let i=n; i>0; i--){
        let row = "";
        for(let j=0; j<i; j++){
           row += j+1;
        }
        console.log(row);   
    }
}
// reverseTriangle(5)

// OUTPUT: 12345
           1234
           123
           12
           1
       




// prints an inverted right-angled triangle pattern of *characters*.  //

function reverseCharTriangle(n){
    for(let i=n; i>0; i--){
        let row = "";
        let char = "A";
        for(let j=0; j<i; j++){
            row += char;
            char = String.fromCharCode(char.charCodeAt(0) + 1);
        }
        console.log(row);   
    }
}
// reverseCharTriangle(4)    
      
// OUTPUT: ABCD
//         ABC
//         AB
//         A