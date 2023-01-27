//             <1> button cick 
// 我们在 html 文件那里给 button 那儿设置了 onclick = show();
let i = 0;
function show()
{
    console.log(i++);
};

btn.addEventListener('click', show); // 同样的方法

btn.addEventListener('click', function()
{
    alert("Oppsss")
}); // 同样的方法
