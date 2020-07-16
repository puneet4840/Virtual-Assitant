# We are converting our voice to text using "SpeechRecognition" library.
# Some steps to follow-
# 1: Create object of Recognizer class.
# 2: Getting voice using microphone.
# 3: Convert audio into text.
print()

import speech_recognition as sr

def Listen_Voice():
    # Creating an object.
    r=sr.Recognizer()

    # Getting voice using microphone.
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('\nListening...')
        audio=r.listen(source)

        print("\nRecognizing...")
        text=r.recognize_google (audio,language='en-in')
        print(f"\nUser:  {text}")


Listen_Voice()
