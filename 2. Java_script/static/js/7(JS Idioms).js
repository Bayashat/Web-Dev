//          < 1 > Assign a default value
/* port = port  || 80
a = 30;
b = a || 'hi'; // 若a存在,则给b a的值,否则给 'hi'

console.log(b); // 30

a = undefined;
b = a || 'hello';
console.log(b); // hello
*/

//           < 2 >   
let a = 
{
  id: '123',
  num: [1, 2, 'hello'],
  b: true
}
// a = undefined;

let p = a && a['id'];
console.log(p); //if a = undefined => error  if not => 123
// so we can write as :
if(a != undefined)
{
    let p = a['id'];
}
console.log(p);

