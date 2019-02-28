var express = require('express') ;
var socket = require('socket.io') ;

// app setup
var app = express() ;

var server = app.listen(3000,'0.0.0.0', function(){
  console.log("Listening to port 4000") ;
})

// Static files
app.use(express.static('public')) ;

// Socket setup
var io = socket(server) ;


var tcpp = require('tcp-ping');
 
tcpp.probe('192.168.43.202', 3000, function(err, available) {
    console.log(available);
});
 
function pingClients(){
	tcpp.ping({ address: '192.168.43.202', port:3000,  attempts:100 }, function(err, data) {
	    console.log(data);
	    console.log( data.avg) ;
	});
}
// setInterval(pingClients, 5000);
// pingClients();

io.on('connection', function(socket){
	console.log("helo");
	// console.log(socket.getPort());
	var clientIp = socket.request.connection.remoteAddress;
	var clientPort = socket.request.connection
	var socketId = socket.id ;
	 console.log("Client and local host Ips: " + clientIp) ;
	 pingClients();
});
// Socket newSock = socket.accept();

// https://stackoverflow.com/questions/3653065/get-local-ip-address-in-node-js