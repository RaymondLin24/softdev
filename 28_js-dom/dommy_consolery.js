// Team RC :: Raymond Lin, Christopher Louie
// SoftDev pd5
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------

//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;

//assign an anonymous fxn to a var
var f = function(x) 
{
    var j=30;
    return j+x;
};

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};

//insert your implementations here for...
// FIB
let fib = function(n){
    if(n == 0){
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
};

// FAC
let fact = function(n){
    if (n == 1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
};

// GCD
let gcd = function(a, b){
    var gcd;
    for(let i=0; i <= Math.min(a, b); i++){
        if(a%i==0 && b%i==0){
            gcd = i;
        }
    }
    return gcd;
};

addItem("The 6th number of the Fibonacci sequence is " + fib(5));
addItem("Factorial of 5 is " + fact(5));
addItem("The GCD of 48 and 72 is " + gcd(48, 72));

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    // body
    return retVal;
};