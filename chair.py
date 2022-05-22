# from gpio import gpio as GPIO

# import the music seperately
# load song into songs
songs = {}
counter = 0

def play_music():
    print("play music")
    global counter
    counter = counter + 1
    # PLAYMUSIC(songs[counter])


def stop_music():
    print("stop music")
    global counter
    counter = counter - 1
    # STOPMUSIC(songs[counter])


# GPIO.setup(25, GPIO.IN)    # set GPIO25 as input (button)  

# GPIO.add_event_detect(25, GPIO.RISING, callback=play_music)
# GPIO.add_event_detect(25, GPIO.FALLING, callback=stop_music)

