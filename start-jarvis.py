import aiml
import pyttsx
import pyaudio
import speech_recognition as sr
import os

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

r = sr.Recognizer()
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
	
# Press CTRL-C to break this loop
while True:
	print("Say something!")
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		input = r.recognize_google(audio)
		print("You said : " + input)
		response = kernel.respond(input)
		print("Jarvis said: " + response)
		engine.say(response)
		engine.runAndWait()
	except sr.UnknownValueError:
		engine.say("I could not understand what you just said")
		engine.runAndWait()
	except sr.RequestError as e:
		print("Could not request results".format(e))
