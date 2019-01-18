# Voice Recognization using Python

### Text to speec ###


# import pyttsx3 import time engine = pyttsx3.init() engine.say('What
# is the time now?') time.sleep(2) engine.say('It is 28 past 9')
# engine.runAndWait()

# from gtts import gTTS
# import os
# tts = gTTS(text='Hi, How are you? What do you do? ', lang='en')
# tts.save("good.mp3")
# os.system("good.mp3")


import speech_recognition as sr                                     # pip install SpeechRecognizarion
from gtts import gTTS                                               # pip instal gtts --> Google text to speech
import os

 # obtain audio from the microphone  
r = sr.Recognizer()                                                 # creating speech recognization object
with sr.Microphone() as source:                                     # idenify audio with microphone , comes form micropone
   print("Say something!")                                          
   audio = r.listen(source)                                         # creating audio file using listen function
   
 # recognize speech using Sphinx                                    # pip install packetsphinx
try:  
   print("Sphinx thinks you said '" + r.recognize_sphinx(audio)     # using spinx module convert audio into text , print it 
   + "'") 
   tts = gTTS(r.recognize_sphinx(audio), lang='en')                 # tts object to save text file to audio     
   tts.save("good.mp3")
   os.system("good.mp3")                                            # play saved audio
except sr.UnknownValueError:     
   print("Sphinx could not understand audio")  
except sr.RequestError as e:  
   print("Sphinx error; {0}".format(e))  


# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# # Create a new chat bot named Charlie
# chatbot = ChatBot('Charlie')

# trainer = ListTrainer(chatbot)

# trainer.train([
#     "Hi, can I help you?",
#     "Sure, I'd like to book a flight to Iceland.",
#     "Your flight has been booked."
# ])

# # Get a response to the input text 'I would like to book a flight.'
# response = chatbot.get_response('I would like to book a flight.')

# print(response)