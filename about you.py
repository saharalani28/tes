import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
     with lock:
         for char in text:
             sys.stdout.write(char)
             sys.stdout.flush()
             time.sleep(delay)
         print()
             
             
def sing_lyric(Lyric, delay, speed):
      time.sleep(delay)
      animate_text(Lyric, speed)
      
  
def sing_song():
     lyric = [
         ("Do you think I have forgotten?", 0.1 ),
         ("Do you think I have forgotten?", 0.1 ),
         ("Do you think I have forgotten?", 0.1 ),
         ("About you?", 0.2),
         ("There was something bout you that now i cant, remember", 0.1),
         ("its the same damn thng that made my heart surrender", 0.1),
         ("And i miss you on the train, i miss you in the morning", 0.1),
         ("I never know what to think about ", 0.1),
         ("I think about youuuuuuwwwwwwwwww", 0.1)
         
     ]   
     delays = [0.3, 0.5, 10.0, 15.0, 20.3,25.0, 27.0, 30.2, 35.0]
     
     Threads =[]
     for i in range(len(lyric)):
         lyric, speed = lyric[i]
         t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
         Threads.append(t)
         t.start()
     for Thread in Threads:
        Thread.join()
                 
if __name__ == "_main_" :
     sing_song()    

           
             
            