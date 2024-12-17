# Imports go at the top
import random
from microbit import *
import music, speech

c = []
c.append("Ho Ho Ho")
c.append("Dashing through the snow")
c.append("Hopes and fears of all the years")
c.append("Ding Dong merrily on high")
c.append("Hark the herald angels sing")

s = []
s.append("If music be the food of love, play on.")
s.append("What country friend is this?")
s.append("Some have greatness thrust upon them.")
s.append("To be up late is to be up betimes.")
s.append("Myrmidoms are no bottle ale houses.")
s.append("The rain it raineth every day.")

m = []
# Define the melody as a list of notes and durations
m1 =  ([
    'e:4', 'e:4', 'e:8',
    'e:4', 'e:4', 'e:8',
    'e:4', 'g:4', 'c:4', 'd:4', 'e:8'
])
m2 = (['e4:4', 'e4:4', 'f4:4', 'g4:4', 'g4:4', 'f4:4', 'e4:4', 'd4:4', 'c4:4', 'e4:4', 'e4:4', 'f4:4', 'g4:4', 'g4:4', 'f4:4', 'e4:4', 'd4:4', 'e4:8'] )
m.append(m1)
m.append(m2)

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
        sleep(1000)
        
# Code in a 'while True:' loop repeats forever
while True:  
    heartbeat()
    if accelerometer.was_gesture('shake'):
        on_gesture_shake()
    if pin_logo.is_touched():
        m_play(m)
    if button_a.is_pressed():
        c_scroll(c)
    if button_b.is_pressed():
        c_say(s)
                
        
