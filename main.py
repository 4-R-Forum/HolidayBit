# Imports go at the top
import random
from microbit import *
import music, speech


c = []
c.append("Ho Ho Ho")
c.append("Dashing through the snow")
#c.append("Hopes and fears of all the years")
#c.append("Ding Dong merrily on high")
#c.append("Hark the herald angels sing")

s = []
s.append("If music be the food of love, play on.")
s.append("What country friend is this?")
s.append("Some have greatness thrust upon them.")
#s.append("To be up late is to be up betimes.")
#s.append("Myrmidoms are no bottle ale houses.")
#s.append("The rain it raineth every day.")


m = []
# Define the melody as a list of notes and durations
m1 =  ([
    'e:4', 'e:4', 'e:8',  'e:4', 'e:4', 'e:8',
    'e:4', 'g:4', 'c:4', 'd:4', 'e:8',
    'f:4' ,'f:4' ,'f:8' ,'f:2' , 'f:2' ,'f:4' ,'f:8' ,'f:2' ,'f:2' ,
    'e:4' ,'d:4' ,'d:4' ,'e:4' ,'d:4' ,'a:8' 
])

m2 = ([
    'd4:4',
    'g4:4', 'g4:2', 'a4:2', 'g4:2', 'f#4:2', 
    'e4:4', 'e4:4', 'e4:4',
    'a4:4', 'a4:2', 'b4:2', 'a4:2', 'g4:2',
    'f#4:4', 'f#4:4', 'f#4:4',
    'b4:4', 'b4:2', 'c5:2', 'b4:2', 'a4:2',
    'g4:4', 'e4:4', 'd4:2', 'd4:2',
    'e4:4', 'a4:4', 'f#4:4',
    'g4:8'
    ])

m3 = ([
    'g4:6','f4:2','e4:4','d4:4',
    'c4:4','d4:4','e4:4','c4:4',
    'd4:2','e4:2','f4:2','d4:2','e4:6','d4:2',
    'c4:4','b3:4','c4:8'
     ])

m4 = ([
    'a#3:4','a#3:4',
    'a3:8','d4:4','d4:4','d4:8','d4:4','d4:4',
    'e4:4','f4:4','g4:4','e4:4','f4:10','g4:4',
    'a#4:8','b4:4','g4:4','f4:4','d4:4','e4:8',
    'd4:12'
])
m5 = ([
    'f4:4',
    'f4:2','f4:2','f4:4','d5:4','c5:4','a4:6','f4:4',
    'f4:2','f4:2','f4:4','d5:4',
    'c5:8','c5:2','b4:2',
    'a4:2','g4:2','f4:4','a4:2','a4:2',
    'd4:2','d4:2','c4:4','f4:2','g4:2',
    'a4:2','bb4:2','a4:4','g4:4',
    'f4:8',
])
m6 = ([
    'a4:8','b4:2','a4:2','g4:2','f#4:2',
    'g4:8','a4:2','g4:2','f#4:2','e4:2',
    'f#4:8','g4:2','f#4:2','e4:2','d4:2',
    'e4:6','a3:2','a3:8',
    'd4:4','e4:4','f#4:4','g4:4',
    'f#4:8','e4:4','r4:4',
    'a4:8','b4:2','a4:2','g4:2','f#4:2',
    'g4:8','a4:2','g4:2','f#4:2','e4:2',
    'f#4:8','g4:2','f#4:2','e4:2','d4:2',
    'e4:6','a3:2','a3:8',
    'd4:4','e4:4','f#4:4','g4:4',
    'f#4:8','e4:8',
    'd4:16'
])
m.append(m1)
m.append(m2)
m.append(m3)
m.append(m4)
m.append(m5)
m.append(m6)
def heartbeat():
    display.show(Image.HEART_SMALL)
    sleep(400)
    display.show(Image.HEART)
    sleep(400)

def on_gesture_shake():
    #display.show(random.randint(0,10))
    c_scroll(s)

def c_scroll(a):
    for x in range(len(a)):
        display.show(a[x])
        sleep(30)

def c_say(a):
    for x in range(len(a)):
        speech.say(a[x])
        sleep(300)

def m_play(a):
    music.set_tempo(bpm=200)
    for x in range(len(a)):
        music.play(a[x])
        
# Code in a 'while True:' loop repeats forever
while True:
    heartbeat()
    if accelerometer.was_gesture('shake'):
        m_play(m)
    if pin_logo.is_touched():
        n = random.randint(0,5)
        m_play(m[n])
    if button_a.is_pressed():
        c_scroll(c)
    if button_b.is_pressed():
        c_say(s)
    
