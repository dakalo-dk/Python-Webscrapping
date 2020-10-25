from playsound import playsound
from multiprocessing import Process

def game(sound):
    playsound(sound)

if __name__ == "__main__":
    p = Process(target = game, args = (r'C:\Users\Dakalo Nemauluma\Music\sound.mp3',))
    p.start()
    input("press ENTER to stop playback")
    p.terminate()