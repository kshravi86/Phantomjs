
console.log("Hello World");
function add(a,b){
	return a+b;
	
}
console.log(add(5,4));

var fs = require("fs");
  

  fs.readFile('input.txt', function (err, data) {
  if (err) return console.error(err);
	console.log(data.toString());
  });

	console.log("Program Ended");
	
