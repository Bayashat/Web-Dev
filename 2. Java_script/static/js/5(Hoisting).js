// (1) with variables
/*
console.log(a) // error
let a = 2;
*/

console.log(b); // not error, just undefined;
var b = 2;


// (2) with functions:
console.log(sum(2, 4));

function sum(a, b) 
{
    return a + b;
}

//                      ** Callback**
let i = 0;
function show() 
{
  console.log(i++);
}

// setTimeout(show, 4000); // 过了4000毫秒后才会输出一个,且只输出一个就结束了
// setInterval(show, 1000); // 每过1000毫秒,输出一个数

// (1)
function f1(){
    setTimeout(function(){
      console.log('f1 function');
    }, 2000);
  }
  
  function f2(){
    console.log('f2 function');
  }
  
  f1();
  f2();
  // 会先输出 f2function, 然后才是 f1function : 因为f1function会迟2秒才输出

// (2) 而如若我们需要先输出f1，且在其保持有setTimeout的情况下,那:
function f1(callback){
  setTimeout(function(){
    console.log('f1 function');
    callback();
  }, 2000);
}

function f2(){
  console.log('f2 function');
}

f1(f2); // 将f2以参数的形式传给了f1(callback), 而callback会等f1自己输出完后再输出
// f2();

