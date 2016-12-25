console.log('Hello');
var that = {
  printf: function(){
    console.log("This keyword");
    console.log(this === that);
  }
};
that.printf();
var person = {
  firstname:"Sharathchandra",
  corpID:"A570530",
  age:"23"
};
function addNumbers(a,b) {
  return a+b;
};
console.log(person);
console.log(addNumbers(2,5));
var print = function() {
  console.log("NodeJS is server end JS!");
};
print();
setTimeout(print,5000);
<!-- Mutliple Request -->
function placeAnOrder(addNumber){
  console.log("Customer Order:", addNumber);
  cookAndDelivery (function (){
    console.log("Delivery:",addNumber);

  });
}

function cookAndDelivery(callback){
  setTimeout(callback,5000);
}
placeAnOrder(1);
placeAnOrder(2);
placeAnOrder(3);
placeAnOrder(4);
placeAnOrder(5);
placeAnOrder(6);
<!-- Mutliple Request -->
<!-- Module Request -->
var movies = require('./module');
<!-- movies.movie(); -->
<!-- Module Request -->
<!-- movies.printWIP(); -->
console.log(movies.favMovie);
<!-- Shared Module Request -->
require('./SharedMod1');
require('./SharedMod2');
