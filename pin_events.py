from functools import partial
from gpiozero import Button, RGBLED, Device
from signal import pause
from sound_manager import SoundManager
from time import sleep
import asyncio


GPIO_PLAY = Button(21)
RGB_LED = RGBLED(17,18,27)

def play_story(sound_manager):
    print("[PLAY EVENT]")
    sound_manager.nextRandomSong()

def stop(sound_manager):
    print("stop")


def volume_down(sound_manager):
    print("softer")


presses = {
    GPIO_PLAY: play_story,
}

holds = {
    GPIO_PLAY: stop,
}
    

async def buttonController(mySoundManager):
    while True:
        for button, event in presses.items():
            print("[BUTTONS] REGISTER")
            button.when_pressed = partial(event, mySoundManager)
            await asyncio.sleep(1)
        await asyncio.sleep(10000)

async def ledController(mySoundManager):
    prevState = True
    while True:
        try: 
            print("[LED] status is %s" % mySoundManager.isStatePlay() )
            if(mySoundManager.isStatePlay() and prevState != True): 
                print("[LED] currently playing led is going to to magic")
                RGB_LED.blink( on_color=(1, 1, 0.2), off_color=(1, 0.2, 1), fade_in_time=4, fade_out_time=4, )
            elif(mySoundManager.isStatePlay() == False and prevState != False): 
                print("[LED] currently not playing led is green")
                RGB_LED.blink( on_color=(1, 1, 0), off_color=(1, 0.1, 0), fade_in_time=1, fade_out_time=2, )
            prevState = mySoundManager.isStatePlay();
            await asyncio.sleep(1)
        except:
            print ("[LED] This ain't good but it will restart it self after 2sec")
            await asyncio.sleep(2)


def main():
    print("[MAIN] creating soundmanager")
    mySoundManager = SoundManager()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        ledController(mySoundManager),
        buttonController(mySoundManager),
    ))
    loop.close()

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
    # LED_RED.off()
    # Device.close()
    print('Destroy')

if __name__ == '__main__':
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
