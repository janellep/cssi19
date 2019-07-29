console.log('1');
console.log('2');
console.log('3');
console.log('4');
console.log('5');
console.log('6');
console.log('7');
console.log('8');
console.log('9');
console.log('10');

//prompt
let result= prompt(" enter your name ");
console.log("hello, ", result);

let num = prompt(" enter a number");
num = Number(num);
if(isNaN(num))
{
        num = 10;
}
console.log (num);

//prompt
 response=prompt("enter grade");
grade= Number(response);
if(!isNaN(response)&&response>=70){
    console.log("you passeed");
}
else{
    console.log("you failed");
}