"""
m = int(input(""))
n = int(input(""))

if m == n:
    print(m)
    
elif m < n:
    n = n + 1
    for i in range(m, n):
        if (i + 1) % 10 == 0 or i % 17 == 0 or i % 15 == 0:
            print(i)


n = int(input(""))
for i in range(1, 11):
    print(n, "x", i, "=", n*i) 
"""
import pyttsx3

engine = pyttsx3.init()  # object creation

""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty('rate', 25)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

engine.runAndWait()

from loader import down_generator, download_gen_erator, download_generator

download_gen_erator()

download_generator()
