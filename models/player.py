import requests
import glob, os
import json
import time

class Player:
    """
    Create an instance of player to
    control the music.
    """
    PLAY_URL = "http://localhost:8080/play?name="
    RESUME_URL = "http://localhost:8080/unpause"
    PAUSE_URL = "http://localhost:8080/pause"
    STATUS_URL = "http://localhost:8080/status"
    STOP_URL = "http://localhost:8080/stop"
    DOWNLOAD_URL = "http://localhost:8080/play?url="
    SONG_URL = "https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs/"
    HEADERS = {"Authorization": "mws96s3um14n8gqu0vmm4rapx3uhoz6l"}

    def __init__(self):
        self.song_queue = []
        self.playing = False

    def play(self, song):
        """
        Plays the song indicated, you should
        search for the song first

        :param song: name of song
        """
        payload = {}
        headers = {
          'Authorization': 'mws96s3um14n8gqu0vmm4rapx3uhoz6l'
        }
        url = self.SONG_URL + str(song.id)
        try:
            response = requests.request("GET", url, headers=headers, data = payload).json()
            get_url = response["playUrl"]
            r = requests.post(self.DOWNLOAD_URL + get_url)
            print(r)
            self.playing = True
        except:
            raise Exception("Error playing song.")

    def resume(self):
        """
        resumes the current song
        """
        requests.post(self.RESUME_URL)
        self.playing = True

    def pause(self):
        """
        pauses the current song
        """
        requests.post(self.PAUSE_URL)
        self.playing = False

    def skip(self):
        """
        goes to next song in queue
        """
        self.pause()
        self.song_queue.pop(0)
        if len(self.song_queue):
            self.play(self.song_queue[0])

    def add_song(self, song):
        """
        add song to end of queue
        """
        if isinstance(song, Song):
            self.song_queue.append(song)
        else:
            raise Excpetion("Argument must be type Song")

    def remove_song(self, song):
        """
        remove song from queue
        """
        if song in self.song_queue:
            self.song_queue.remove(song)

    def get_status(self):
        """
        gets the status of the player
        """
        return requests.get(STATUS_URL)


