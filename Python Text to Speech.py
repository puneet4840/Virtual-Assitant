# pyttsx3 module is used to convert text to speech.
print()

import pyttsx3

engine=pyttsx3.init('sapi5')

# Creating an object and start speaking.

# Directly start speaking.
# pyttsx3.speak('Puneet')

# Changing Rate
rate=engine.getProperty('rate')
engine.setProperty('rate',150)

engine.say('Hii, I am Puneet.')
engine.runAndWait()

# Changing Volume
volume=engine.getProperty('volume')
print(f"Volume: {volume}")


# Changing Voice
voices=engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voice.id)
    engine.say('Hii, I am Puneet.')
    engine.runAndWait()

