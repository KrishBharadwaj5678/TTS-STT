#Text To Speech Convertor

# This module is imported so that we can  
# play the converted audio 
from gtts import *
from playsound import *

# The text that you want to convert to audio
text=input("Enter Your Text:")

#Language of the Text
language=input("Enter You Language Code:") 

# Passing the text and language to the engine 
sound=gTTS(text,lang=language)

# Saving the converted audio in a mp3 file named 
sound.save("Krish.mp3")

# Playing the converted file 
playsound("Krish.mp3")
