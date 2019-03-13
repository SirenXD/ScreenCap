document.addEventListener('DOMContentLoaded', function(){
    //var io = require('socket.io');
    var socket = io.connect();
    var currentColor = "";
    var image = document.getElementById("stream");
    const bgColor = "#899bb5";

    socket.on("update", function(data){
        console.log("drawing image");
        draw(data);
    });



    function init(){
        image.width = 1600;
        image.height = 900;
    }

    function draw(data){
        image.src = "data:image/png;base64," + data["image"];
        console.log("data:image/png;base64," + data["image"]);
    }

    init();

});
