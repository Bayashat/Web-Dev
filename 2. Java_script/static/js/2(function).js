
/*
var s_name = "Aikumys";

function hi()
{
    console.log("Hello " + s_name )
};

hi()   // Hello Aikumys
*/
var s_name = 
{
    name : 'Aikumys',
    age : 20,
    gpa : 3.4
};

function hi()
{
    if(s_name['gpa'] >= 3.5)
    {
        console.log("GPA is greater than 3.5")    
    }
    else
    {
        console.log("GPA is less than 3.5")
    }
};

hi() // GPA is less than 3.5