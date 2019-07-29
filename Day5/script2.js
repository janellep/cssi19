//f(x)is a function that take
// a single parameter and return
// multiplied by 3 then adding 7
function f(x)
{
    return 3 * x * 7;
}

// display the result pf calling the
// function f()with 
//argument 2
console.log(f(2));
console.log(f(12));
console.log(f(7));

function g(x)
{
    return 5*x* 5;
}

console.log(g(2));
console.log(g(12));
console.log(g(7));

function h(x)
{
        return 5 * x ** 2 - 4 * x + 2;
}

console.log(h(2));
console.log(h(12));
console.log(h(7));

function i(x,y){
    return x*x * y*y;
    //return x**2 -y**2;
}

console.log("/n");
console.log(i(3,4));
console.log(i(4,3));
console.log(i(5,2));


function k(r){
    return 2 * Math.PI * r;
}

console.log("/n");
console.log(k(1));
console.log(k(1.5));

function l(a,b,c){
    vard = b**2 - 4 * a * c;

    if(d >= 0){
    var srd=Math.sqrt(d);
    return(-1 * b + srd)/(2*a);
    }
    else {
    return NaN;
    }
}

console.log(l(1,4,4));
console.log(l(1,1,-1));