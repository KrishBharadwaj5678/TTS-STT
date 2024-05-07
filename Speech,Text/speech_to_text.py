# Speech/Voice To Text Convertor

# First we will import speech_recognition
from speech_recognition import *

# Create an object of Recognizer
speechrecog=Recognizer()

# Printing message on screen
print("I am Listening You............")

# using with statement which will automatically close the Microphone() class as m
with Microphone() as m:

    # Using listen() to Capture Microphone Input
    audio=speechrecog.listen(m)

    # here the listened voice will be converted into specified language
    query=speechrecog.recognize_google(audio,language='eng')

    # And at last we will print the voice converted into text
    print(query)
