# write a program that converts text to speech
import pyttsx3
engine = pyttsx3.init()



engine.say("Hello, I am a text to speech engine. I can convert your text into speech. How can I help you today?")
engine.runAndWait()