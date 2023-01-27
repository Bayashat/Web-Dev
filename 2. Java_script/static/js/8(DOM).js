//      DOM : Document Object Model

/*          1. Document:

In console: you can write 'windows.document' see all the documents.
and 'document.head' or 'document.body' can see you HTML file's heady and body part
*/
/*
//          2. Accessing DOM Nodes
let a = document.body;
console.log(a);

//          3. Use DOM lookup method : changing style

let b = document.getElementsByTagName('h1');
console.log(b);  // [h1]

let c = document.getElementById('btn');
console.log(c); // 

let d = document.getElementsByClassName('box');
console.log(d); // 

// let e = document.querySelector('html body .box');
let e = document.querySelector('.box');
console.log(e); // 
e.innerHTML = "Hello message"; 
e.style.color = 'red';
e.style.fontSize = '25px';
e.style.fontWeight = 'bold';

let btn = document.querySelector('#btn');
btn.style.background = 'yellow';
btn.style.fontSize = '25px';
btn.style.border = 'solid 5px green';
btn.style.borderRadius = '20px';
btn.style.padding = '10px 40px';
console.log(btn.getAttribute('data-id')) // 123
btn.setAttribute('data-id', 999); 


//             4. Creating new element
let text = document.createElement('h3');
text.innerHTML = "new created h3 from JS";

let container = document.querySelector('.container');
container.appendChild(text);

//              5. More DOM operations
// 1.window.location.href 会给你当前页面的url地址,  可将其改变: window.location.href = "google.com" 来转到别的页面



// 2. alert('wow!')
alert('WOW! its so nice')  // 弹出一个新小窗口 提示 : WOW! its so nice

// 3. confirm('OK?') 
confirm('OK?')  // 弹出一个新小窗口 提示 : Ok?  要我们选择 Ok cancel

// 4. prompt('Message')
prompt('Enter your name: ') // 弹出一个输入框
let n = prompt('Enter your name: ');
console.log(n);
*/

//          < 6 > DOM's Coordinate System
// 网页上的每个东西都有它的坐标
console.log(btn.offsetTop); // 107 - 是指从上方到btn的距离
console.log(btn.offsetLeft); // 8 - 是指从左方到btn的距离
console.log(btn.offsetHeight); // 22 是btn的高度
console.log(btn.offsetWidth); // 50 是btn的宽度

