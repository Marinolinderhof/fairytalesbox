from persisten_client import PersistentMPDClient
from time import sleep

class SoundManager(object):
    def __init__(self):
        # Persistent MDP client it's wrapper for all actions
        self.client = PersistentMPDClient(host="localhost", port=6600)
        
        # player
        self.client.repeat(0)
        self.client.random(1)
        self.client.single(1)
        self.client.consume(0)
        #playlist
        self.loadPlaylist('queue1')

    def loadPlaylist(self, playlist):
        print('[LOAD PLAYLIST] clear')
        self.client.clear()
        print('[LOAD PLAYLIST] loading')
        self.client.load('queue1')
        print('[LOAD PLAYLIST] shuffle')
        self.client.shuffle()

    def status(self):
        return self.client.status()

    def isStatePlay(self):
        try: 
            return self.client.status()['state'] == 'play'
        except:
            print ("[IS STATE PLAY] This ain't good but it won't hurt")

    def nextRandomSong(self):
        print('[NEXT RANDOM SONG]')

        if self.isStatePlay():
            print('[NEXT RANDOM SONG] state is play execute next()')
            self.client.repeat(1)
            self.client.next()
            sleep(1);
            self.client.repeat(0)
            return
        print('[NEXT RANDOM SONG] state is NOT play execute play()')
        self.client.play()
        sleep(1);

    def __del__(self):
        self.client.disconnect()
        # self.loop.close()
