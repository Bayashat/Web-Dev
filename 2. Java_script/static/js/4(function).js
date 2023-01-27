//              < 1 > Funtion decloration
function greeting()
{
    console.log('hi');
};
greeting();

//              < 2 > function expression
let greeting2 = function()
{
    console.log('hello2');
};
greeting2();

//              < 3 > Arrow function
// (1):
// standart form :
function square1(v)
{
    return v * v;
};

let square = (a) => a * a;
console.log(square(4)); // 16

// (2):
let sum = (a,b) => a+b;
console.log(3,4); // 7

// (3):
let mult = (a,b) => {
    let c = a * b;
    return c;
}

//                 < 4 > As property of an object
let student = 
{
    id : '20BD030499',
    s_name : 'Bayashat',
    show: function()
    {
        // console.log(this.id + " => " + this.s_name); // 20B030499 => Bayashat
        console.log(`${this.id} => ${this.s_name}`); // 20B030499 => Bayashat
    }
}
student.show();