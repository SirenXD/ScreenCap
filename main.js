var express = require('express');
var app = express();
var http = require("http");
var server = http.createServer(app);
var io = require("socket.io")(server, {'origins' : "*:*"});
var fs = require("fs");

const port = process.env.PORT || 5000;
// const port = 7777;

server.listen(port);


app.use(express.static(__dirname + "/public"));

io.on("connection", function(socket){
    // app.post('/', function(req, res){
    //     console.log("REEEE");
    //     let body = '';
    //     req.on('data', chunk => {
    //         body += chunk.toString();
    // });
    //
    //     req.on('end', () => {
    //         console.log(body);
    //         socket.broadcast.emit("update", {image: body});
    //         res.set('Content-type', "text/plain");
    //         res.send("You sent data to the server!");
    //     });
    // });
    socket.on('newData', function(msg){
        let buff = new Buffer(msg.data);
        let utfData = buff.toString('utf8');
        socket.broadcast.emit("update", {image: utfData});
    });
});
