//  JSON : Java Script Object Notation
let a = 
{
    id: '123',
    num: [1, 2, 'hello'],
    b: true
}

let s = JSON.stringify(a);
console.log(s) // {"id":"123","num":[1,2,"hello"],"b":true}

let b = JSON.parse(s);

console.log(typeof (s)); // string
console.log(b); // {id: '123', num: Array(3), b: true}

a = undefined;

let p = a && a['id'];
console.log(p);
