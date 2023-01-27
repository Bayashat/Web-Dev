let arr = [1,2,3,4,5,6,7,8,9,10];

arr.push(6);
arr.pop();

console.log(arr.length);  //   10
console.log(arr.indexOf(3)); // 2

arr.find(function(v)
{
    if(v == 2)
    console.log('hi');
});

let b = arr.slice(2,9); // 提取
console.log(arr); // 1 2 3 4 5 6 7 8 9 10
console.log(b); // 3 4 5 6 7 8 9

arr.splice(2,2); // 从第2位置开始,删除2个元素
console.log(arr); // 1 2 5 6 7 8 9 10

let c = arr.map(function(v)
{
    return v + 5;
});
console.log(c); // [6, 7, 10, 11, 12, 13, 14, 15]

let d = c.filter(function(v)
{
    return v > 9; 
});
console.log(d); // 10, 11, 12, 13, 14, 15

let s = d.reduce(function(sum,v)
{
    return sum + v;
}, 0);
console.log(s); // 75
/*  for loop : 1
for(let i = 0; i < arr.length; i++)
    console.log(arr[i])
*/

/* for loop : 2:
for(let i of arr)
{
    console.log(i)
}
*/

/* for loop : 3:
arr.forEach(function (i)
{
    console.log(i);
});
*/
// while loop 
let i = 0;
while(i < arr.length)
{
    console.log(arr[i]);
    i++;
};