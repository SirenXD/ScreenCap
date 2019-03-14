import base64
import time

import cv2

from PIL import Image
import ScreenManager
import socketio
from io import BytesIO
import threading

#Threading function to encode and prepare frames
def prepFrame():
    global running
    global manager
    global unencodedFrames
    global currentSend
    global data
    global currentSend

    while running:
        #For FPS counting
        last_time = time.time()

        manager.capture()

        #Serves the image to the local client, mostly
        data = [manager.getCurrentCap(), manager.getAsNP()]

        #Create a blank Image
        jpgImg = Image.new('RGB', (1600, 900))
        #Create a copy of the current screen Cap, which is a PNG, and store it in an empty PIL Img file
        jpgImg.paste(manager.getCap(), (0, 0, 1600, 900))

        #Resize it for data-size purposes
        jpgImg = jpgImg.resize((800, 480), resample=Image.BILINEAR)
        # jpgImg = jpgImg.resize((1280, 720), resample=Image.BILINEAR)

        ##Long process to encode it into Base64
        buffered = BytesIO()
        jpgImg.save(buffered, format="jpeg", optimize=True, quality=95)
        imgstr = base64.b64encode(buffered.getvalue())

        #Effectively serve the Image to the Socket stream
        currentSend = imgstr

        print("fps: {}".format(round(1 / (time.time() - last_time))))

def init():

    #Init some boring stuff
    global manager
    global socket
    global session
    global encThread
    global prepThread
    global data
    global readyToSend
    global running


    running = True
    manager = ScreenManager.ScreenManager()
    data = [None, None]

    prepThread = threading.Thread(target=prepFrame)
    prepThread.start()

    #Don't load anything until we have a screenshot loaded and prepped
    while (data[0] is None) and (data[1] is None):
        time.sleep(.2)

    img = data[1]

    #Load the SocketIO client
    socket = socketio.Client(binary=True)

    #Load the local client
    cv2.imshow("OPENCV/Numpy normal", img)
    #Connect to the Node server
    socket.connect("http://127.0.0.1:7777")

    method()

# Sends the data to the Node Server via SocketIO emit
def send(data):
    socket.emit("newData", {"data":data})




def method():
    while True:

        global data
        global currentSend
        #Send the currently served frame (even if already served)
        #This is probably where I could get a lot of optimization done honestly, this get's called **a lot**
        send(currentSend)

        #Upload the local client. Same as above (optimization).
        cv2.imshow("OPENCV/Numpy normal", data[1])

        #Quit if user presses 'q', properly shuts everything down.
        if cv2.waitKey(25) & 0xFF == ord("q"):
            socket.disconnect()
            cv2.destroyAllWindows()
            global running
            running = False
            global prepThread
            prepThread.join()
            break

if __name__ == "__main__":
    init()
