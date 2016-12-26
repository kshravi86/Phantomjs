var http = require("http");

  http.createServer(function (request, response) {

 
	  
	
  response.writeHead(200, {'Content-Type': 'text/plain'});

  
	  
	
  response.end('Hello World\n');
  }).listen(8081);

  
	  
  
  console.log('Server running at http://127.0.0.1:8081/');
  
  var f=require("fs");
  
  f.readFile('input.txt',function(err,data){
	  
	  if(err){
		console.log(  err.stack);
		return;
		  
	  }
	  console.log(data.toString);
  } );
