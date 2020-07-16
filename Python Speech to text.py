# We are converting our voice to text using "SpeechRecognition" library.
# Some steps to follow-
# 1: Create object of Recognizer class.
# 2: Getting voice using microphone.
# 3: Convert audio into text.
print()

# import speech_recognition as sr
# import wikipedia

# def Listen_Voice():
#     # Creating an object.
#     r=sr.Recognizer()

#     # Getting voice using microphone.
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source,duration=1)
#         print('\nListening...')
#         audio=r.listen(source)

#         print("\nRecognizing...")
#         text=r.recognize_google (audio,language='en-in')
#         print(f"\nUser:  {text}")


# Listen_Voice()
# import re
# from PyDictionary import PyDictionary

# s='find the meaning of github'
# w=s.split(' ')

# dic=PyDictionary()
# mean=dic.meaning('Internet')
# m=mean.get('Noun')
# m1=m[0]
# print(m1)

# import os
# import webbrowser
# import smtplib


# passs='8126484099'
# msg='Hii puneet how are you'

# server=smtplib.SMTP('smtp.gmail.com',587)
# server.ehlo()
# server.starttls()
# server.login('pkv4840@gmail.com',passs)
# server.sendmail('pkv4840@gmail.com','pkv4840@gmail.com',msg)
# server.close()

# from word2number import w2n
# one='ten'
# o=int(w2n.word_to_num(one))

# import wolframalpha

# que=input("Enter query: ")
# app_id='JE47GT-G2l459KLh6'
# client=wolframalpha.Client(app_id)
# result=client.query(que)
# ans=next(result.results).text
# print(ans)    

# s='temperature of delhi'
# ss=s.split(' ')
# city=ss.index('delhi')
# print(city)

# import pyjokes
# joke=pyjokes.get_joke(language='en',category='neutral')
# print(joke)

# import wikiquote
# quo=wikiquote.quote_of_the_day(lang='en')
# print(quo[0])
# print(quo[1])

# tit=wikiquote.random_titles(max_titles=5)
# quo=wikiquote.quotes(tit[0],max_quotes=1)
# print(quo[0])

# s='close chrome browser'
# s.split(' ')
# print(s)
# i=s.index('chrome')
# ss=s[i:]
# print(ss)
import os
import subprocess
# subprocess.Popen(['‪‪C:\\Windows\\SysWOW64\\control.exe'])
os.system('explorer.exe')
