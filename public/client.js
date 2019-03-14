document.addEventListener('DOMContentLoaded', function(){
    var socket = io.connect();
    var stream = document.getElementById("stream")

    socket.on("update", function(data){
        console.log("drawing image");
        draw(data.image);
    });

    function draw(data){

        stream.src = "data:image/jpeg;base64," + data;
        console.log("data:image/jpeg;base64," + data);
    }

});
