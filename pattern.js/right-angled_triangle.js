//  PRACTICE   QUESTION   NUMBER  1  // 

// Takes a number as input and prints a right-angled triangle pattern of *numbers* using an array.  // 

function triangle(n){
    for(let i=0; i<n; i++){ // outer loop print line how line it will print 
        let row = "";
        for(let a=0; a<=i; a++){    // inner loop print number and number will come from i
            row += a+1;
        }
        console.log(row);
    }
}
// triangle(5)


// OUTPUT : 1
//          12
//          123
//          1234
//          12345
            




// prints a right-angled triangle pattern of *characters* using an array.  // 

function charTriangle(n){
    // let char = "A";
    for(let i=0; i<n; i++){
        let row = "";
        let char = "A";
        for(let j=0; j<=i; j++){
            row += char;
            char = String.fromCharCode(char.charCodeAt(0) + 1);
        }
        console.log(row);
        // char = String.fromCharCode(char.charCodeAt(0) + 1);
    }
}
// charTriangle(4)

// OUTPUT : A            (when char is in outter loop) OUTPUT : A
//          AB                                                  BB
//          ABC                                                 CCC
//          ABCD                                                DDDD