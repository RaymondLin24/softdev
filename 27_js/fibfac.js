//Team Prize Picks :: Raymond Lin, Jackie Zeng
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:
let fact = function(n){
    if (n==1){
      return 1;
    }
    else {
      return
    }
  }
  //<your team's fact(n) implementation>
  
  //TEST CALLS
  // (writing here can facilitate EZer copy/pasting into dev console now and later...)
  console.log(fact(1)); // "...should be 1"
  console.log(fact(2)); // "...should be 2"
  console.log(fact(3)); // "...should be 6"
  console.log(fact(4)); // "...should be 24"
  console.log(fact(5)); // "...should be 120"
  
  //-----------------------------------------------------------------
  
  
  //fib:
  
  //<your team's fib(n) implementation>
  let fib = function(n){
    if (n ==0){
      return 0;
    }
      else if (n==1){
          return 1;}
      else {
      return (fib(n-1)+fib(n-2));
    }
  }
  //TEST CALLS
  // (writing here can facilitate EZer copy/pasting into dev console now and later...)
  console.log(fib(0)); // "...should be 0"
  console.log(fib(1)); // "...should be 1"
  console.log(fib(2)); // "...should be 1"
  console.log(fib(3)); // "...should be 2"
  console.log(fib(4)); // "...should be 3"
  console.log(fib(5)); // "...should be 5"
  //=================================================================