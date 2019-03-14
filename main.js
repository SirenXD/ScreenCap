var express = require('express');
var app = express();
var http = require("http");
var server = http.createServer(app);
var io = require("socket.io")(server, {'origins' : "*:*"});

// const port = process.env.PORT || 5000;
const port = 7777;

server.listen(port);


app.use(express.static(__dirname + "/public"));

io.on("connection", function(socket){
    socket.on('newData', function(msg){
        socket.broadcast.emit("update", {image: msg.data.toString("utf8")});
    });
});
