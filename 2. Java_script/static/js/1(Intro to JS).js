// 1.What is JS:

console.log('Hello from JS file');

console.log(typeof (2));  // number
console.log(typeof (2.4)); // number
console.log(typeof ('hello')); // string
console.log(typeof ({'id':2 })); // object
console.log(typeof (null)); // object
console.log(typeof (undefined)); // undefined
console.log(typeof (Symbol('a'))); // symbol
console.log(typeof (function(){})); // function
console.log('\n');


// 2. Creation of the variables: can be done with 3 main ways:

var a;  // create a variable with nothing, it will create a global variable 
a = true;
console.log(a);

let b = 3; // let keyword will create a local variable
b = 'hello b';
console.log(b);

const c = 4; // craete a const variable
console.log(c);