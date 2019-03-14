document.addEventListener('DOMContentLoaded', function(){
    //var io = require('socket.io');
    var socket = io.connect();
    var currentColor = "";
    var canvas = document.getElementById("useless");
    var stream = document.getElementById("stream")
    //var context = canvas.getContext("2d");
    const bgColor = "#899bb5";

    socket.on("update", function(data){
        console.log("drawing image");
        draw(data.image);
    });



    function init(){
    //     canvas.width = 1600;
    //     canvas.height = 900;
    //     context.fillRect(0,0,canvas.width, canvas.height);
    //     context.save();
    }

    function draw(data){
        stream.src = "data:image/png;base64," + data;
        console.log("data:image/png;base64," + data);
        //
        // console.log(data);

        //data = atob(data);
        //context.drawImage(img1,0,0);
    }

    init();

});
