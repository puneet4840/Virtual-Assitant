# This is main file for jarvis project.
print()

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
from random import randint
import webbrowser
from PyDictionary import PyDictionary
import smtplib
from random import randint
from time import sleep
from word2number import w2n
import wolframalpha
import pyjokes
import wikiquote
import subprocess
import requests
import json


wikipedia.set_rate_limiting(True)

# Setting Voice Rate,Volume,Voices(0 for male and 1 for female)
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',185)
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


# This function is used to speak the text.
def speak(audio):
    print(f"Maria: {audio}")
    engine.say(audio)
    engine.runAndWait()


s=sr.Recognizer()
# This function is used to generate text from voice.
def Listen():
    with sr.Microphone() as source:
        print('\nListening...')
        s.adjust_for_ambient_noise(source,duration=0.3)
        s.pause_threshold=0.5
        audio=s.listen(source)
    try:
        print('\nRecognizing...')
        text=s.recognize_google(audio,language='en-in')
        print(f'User:  {text}')
    except:
            speak('Did not Understand!!!')
            speak('say again')
            text=Listen()
    return text.lower()

jarvis_intro='I am Jarvis, Your assistant sir'
user_name='Puneet'
user_email='pkv4840@gmail.com'
email_pass='8126484099'
f_n=''
app_id='JE47GT-G2l459KLh6'
client=wolframalpha.Client(app_id)


def Guess_g():
    speak('this is the guessing a number game')
    speak('please wait for five seconds')
    sleep(5)
    speak('game started')
    r_n=randint(1,100)
    ch=0
    ch_l=5
    speak(f'you have {ch_l} chances to guess a number')
    while True:
        speak('guess a number')
        try:
            y_gue=str(Listen())
            num=int(w2n.word_to_num(y_gue))
        except:
            speak('You guessed invalid number please guess again')
            y_gue=str(Listen())
            num=int(w2n.word_to_num(y_gue))
        y_gue=y_gue.replace(y_gue,'')
        if num==r_n:
            speak('You won')
            speak(f'You guess a correct number {r_n}.')
            ch=ch+1
            speak(f'you guessed {r_n} in {ch} chance')
            ch_l=ch_l-1
            break
            
        elif num<r_n:
            ch=ch+1
            ch_l=ch_l-1
            speak('you guessed low')
            speak(f"you have {ch_l} chance left")
            if ch_l==0:
                speak('you crossed your guessing limit')
                speak('sorry, you lose')
                speak('Game Over')
                break

        elif num>r_n:
            ch=ch+1
            ch_l=ch_l-1
            speak('you guessed high')
            speak(f"you have {ch_l} chance left")
            if ch_l==0:
                speak('you crossed your guessing limit')
                speak('sorry, you lose')
                break

def news():
    url="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=52afef4f44314099adb8a2b5841009df"
    bbc=requests.get(url).json()
    article=bbc["articles"]
    results=[]

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        speak(results[i])




def wish_me():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        speak('Good Morning') 
    elif h>=12 and h<=16:
        speak('Good Afternoon')
    elif h>16 and h<=20:
        speak('Good Evening')
    elif h>20 and h<=24:
        speak('Good Night')
    speak(f'How can i help you ')

h1=datetime.datetime.now().hour

if __name__ == "__main__":
    wish_me()
    while True:
        que=Listen().lower()
        if 'time' in que:
            que=que.replace(que,'')
            str_t=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'the time is: {str_t}')

        elif 'good' in que:
            que=que.replace(que,'')
            speak('Thank You sir.')

        elif 'morning' in que:
            que=que.replace(que,'')
            if h1>0 and h1<12:
                speak('a very good morning sir')
            else:
                speak("it's not morning sir")

        elif 'afternoon' in que:
            que=que.replace(que,'')
            speak('a very good after noon sir')
            

        elif 'evening' in que:
            que=que.replace(que,'')
            speak('a very good evening sir')


        elif 'i want your help' in que:
            que=que.replace(que,'')
            speak('what kind of help i can do for you')

        elif 'meet my friend' in que:
            que=que.replace(que,'')
            speak("what's your friend name")
            f_n=str(Listen())
            speak(f'Hello {f_n}, How are you')

        elif 'wikipedia' in que:
            speak('searching wikipedia')
            result=wikipedia.summary(que,sentences=1)
            que=que.replace(que,'')
            speak('According to wikipedia')
            speak(result)

        elif 'news' in que or 'latest news' in que:
            que=que.replace(que,'')
            speak('todays news:')
            news()

        elif 'who made you' in que:
            que=que.replace(que,'')
            speak('i have been developed by Puneet Kumar')

        elif 'created' in que:
            que=que.replace(que,'')
            speak('I have been created by Puneet Kumar')

        elif 'what can you do' in que:
            que=que.replace(que,'')
            speak('You can ask-')
            speak('time')
            speak('temperature')
            speak('use calculator')
            speak('play music')
            speak('search anything on google')
            speak('play games')
            speak('you can open software')
            speak('send mail to anyone')
            
        elif 'stop' in que or 'exit' in que or 'bye' in que:
            que=que.replace(que,'')
            speak('Thanks for giving me your time.')
            speak('I am quiting.')
            exit()
        
        elif 'play music' in que or 'play song' in que:
            que=que.replace(que,'')
            song_dir="E:\\Python Projects\\Project 1\\Jarvis Project\\songs"
            songs_lst=os.listdir(song_dir)
            r_num=randint(1,len(songs_lst))
            os.startfile(os.path.join(song_dir,songs_lst[r_num]))

        elif 'chrome' in que:
            que=que.replace(que,'')
            speak('Opening chrome')
            subprocess.Popen("C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")

        elif 'mysql' in que or 'sql' in que:
            que=que.replace(que,'')
            speak('so do you want to create data base.')
            speak('opening mysql')
            subprocess.Popen("C:\\Program Files\\MySQL\\MySQL Workbench 8.0 CE\\MySQLWorkbench.exe")

        elif 'pycharm' in que:
            que=que.replace(que,'')
            speak('But Visual Studio Code is your favourite ide')
            speak('opening pycharm')
            subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.4\\bin\\pycharm64.exe')

        elif 'notepad' in que:
            que=que.replace(que,'')
            speak('opening notepad')
            os.system('notepad.exe') 

        elif 'control panel' in que:
            que=que.replace(que,'')
            speak('opening control panel')
            os.system('control.exe')  

        elif 'file explorer' in que or 'explorer' in que:
            que=que.replace(que,'')
            speak('opening file explorer')
            os.system('explorer.exe')

        elif 'this pc' in que:
            que=que.replace(que,'')
            speak('opening this pc')
            os.system('explorer.exe')

        elif 'calculator' in que:
            que=que.replace(que,'')
            os.system('calc.exe')

        elif 'command prompt' in que:
            que=que.replace(que,'')
            os.system('cmd.exe')

        elif 'Wi-Fi' in que:
            que=que.replace(que,'')
            speak('i will also not listening now')
            speak('Wi-Fi turned off')
            os.system("netsh interface set interface 'Wifi' disabled")

        elif 'turn on Wi-Fi' in que or 'Wi-Fi' in que:
            que=que.replace(que,'')
            os.system("netsh interface set interface 'Wifi' enabled")

        elif 'how are you' in que:
            que=que.replace(que,'')
            speak(f'I am good {user_name}')
            speak('So, How are you.')

        elif 'i love you' in que:
            que=que.replace(que,'')
            speak('I am very delighted to hear that')

        elif 'i am fine' in que:
            que=que.replace(que,'')
            speak('okay, god always bless you.')
            speak('what do you want to ask')

        elif 'will you marry me' in que:
            que=que.replace(que,'')
            speak('I wish I can...')
            speak('But you are human and i am AI')

        elif 'good job' in que:
            que=que.replace(que,'')
            speak('Thank Your sir')

        elif 'who are you' in que:
            que=que.replace(que,'')
            speak('My name is Maria and I am your assistant sir')
            speak('I have been created by Puneet')

        elif 'youtube' in que:
            speak('Opening Youtube')
            que=que.replace(que,'')
            webbrowser.open('youtube.com')
        
        elif 'google.com' in que or 'google' in que:
            speak('opening Google.com')
            que=que.replace(que,'')
            webbrowser.open('google.com')

        elif 'python documentation' in que:
            que=que.replace(que,'')
            webbrowser.open('https://docs.python.org/3/')

        elif 'website' in que or 'search' in que:
            if 'website' in que:
                speak('Which website sir')
                website=str(Listen())
                speak(f'I am opening {website}')
                webbrowser.open(website)
            else:
                speak('what do you want to search.')
                search=str(Listen())
                speak(f'searching...{search}')
                webbrowser.open(search)

        elif 'what is your name' in que:
            que=que.replace(que,'')
            speak('My name is Maria')
            speak('Thanks for asking')
        
        elif 'tell me my name' in que:
            que=que.replace(que,'')
            speak(f'Your name is {user_name}')
        
        elif 'what is your age' in que:
            que=que.replace(que,'')
            speak('My age is not defined')
            speak('Ask anything rather then the personal question, Please')

        elif 'meaning' in que:
            que=str(que)
            w=que.split(' ')
            word=w[-1]
            w=w.clear()
            que=que.replace(que,'')
            speak(f"Just wait,Finding the meaning of {word}")
            di=PyDictionary()
            mean=di.meaning(word,disable_errors=True)
            mm=mean.get('Noun')
            mmm=mm[0]
            speak(f'The meaning of {word} is {mmm}')

        elif 'close' in que:
            que=que.replace(que,'')
            speak('What do you want to close sir')
            w=Listen()
            if 'code' in w or 'vs code' in w:
                speak('code is closing sir')
                os.system('taskkill /f /im'+' Code.exe')
            elif 'chrome browser' in w:
                speak('chrome browser is closing sir')
                os.system('taskkill /f /im'+' Chrome.exe')

            elif 'git bash' in w:
                w=w.replace(w,'')
                speak('Git is closing sir')
                os.system('taskkill /f /im'+' git-cmd.exe')

            elif 'adobe premiere pro' in w or 'premiere pro' in w:
                w=w.replace(w,'')
                speak('Abobe premiere pro is closing sir')
                os.system('taskkill /f /im'+' Adobe Premiere Pro.exe')

            elif 'audacity' in w:
                w=w.replace(w,'')
                speak('Audacity is closing sir')
                os.system('taskkill /f /im'+' audacity.exe')

            elif 'settings' in w or 'settings' in w:
                w=w.replace(w,'')
                os.system('taskkill /f /im'+' Control.exe')

        elif 'locate' in que or 'map' in que:
            que=que.replace(que,'')
            speak('what do you want to locate')
            loc=Listen()
            webbrowser.open('https://www.google.com/maps/place/'+loc)

        elif 'maps' in que or 'google map' in que:
            que=que.replace(que,'')
            speak('what do you want to locate')
            loc=Listen()
            webbrowser.open('https://www.google.com/maps/place/'+loc)

        
        elif 'send email' in que:
            que=que.replace(que,'')
            speak("input sender's email")
            e_m=input('Input email here: ')
            speak('what should i say')
            msg=Listen()
            speak('sending email...')
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login(user_email,email_pass)
            server.sendmail(user_email,e_m,msg)
            server.close()
            speak('email has been sent.')

        elif 'play game' in que:
            que=que.replace(que,'')
            speak('we can play guessing number game')
            print("Speak ok  or let's play to start the game.")
            y=Listen()
            if 'ok' in y:
                print('***Game Started***')
                y=y.replace(y,'')
                Guess_g()

            elif 'lets play' in y:
                print('***Game Started***')
                y=y.replace(y,'')
                Guess_g()
            elif 'no' in y:
                y=y.replace(y,'')
                speak('Okay, we are not playing a game now.')

        elif 'play a game' in que:
            que=que.replace(que,'')
            speak('we can play guessing number game')
            print("Speak ok  or let's play to start the game.")
            y=Listen()
            if 'ok' in y:
                print('***Game Started***')
                y=y.replace(y,'')
                Guess_g()

            elif 'lets play' in y:
                print('***Game Started***')
                y=y.replace(y,'')
                Guess_g()
            elif 'no' in y:
                y=y.replace(y,'')
                speak('Okay, we are not playing a game now.')

        elif 'list of games' in que:
            que=que.replace(que,'')
            speak('These are the games')
            speak('1: Guessing the number game')

        elif 'what' in que or 'who' in que:
            speak('Wait for the result')
            try:
                result=client.query(que)
                que=que.replace(que,'')
                ans=next(result.results).text
                speak(f"Result is:  {ans}")
            except:
                speak('Unable to find')

        elif 'when' in que or 'where' in que:
            speak('Wait for the result')
            try:
                result=client.query(que)
                que=que.replace(que,'')
                ans=next(result.results).text
                speak(f"Result is:  {ans}")
            except:
                speak('Unable to find')

        elif 'temperature of' in que or 'temperature in' in que:
            speak('Just wait.')
            temp=que.split(' ')
            city=temp[2]
            result1=client.query(que)
            ans1=next(result1.results).text
            que=que.replace(que,'')
            speak(f"Temperature of {city} is {ans1}")

        elif 'joke' in que:
            que=que.replace(que,'')
            joke=pyjokes.get_joke(language='en',category='neutral')
            speak(joke)

        elif 'quote of the day' in que:
            que=que.replace(que,'')
            quot=wikiquote.quote_of_the_day(lang='en')
            speak(quot[0])
            speak(f'By:  {quot[1]}')

        elif 'quote' in que:
            que=que.replace(que,'')
            tit=wikiquote.random_titles(max_titles=5)
            quote=wikiquote.quotes(tit[0],max_quotes=1)
            speak(quote)

        elif 'shutdown' in que:
            que=que.replace(que,'')
            speak('Do you really want to shutdown your PC')
            speak('Yes: Shutdown\nNo: Terminate shutdown')
            y_n=str(Listen())
            
            if 'yes' in y_n:
                speak('Shutting down your PC...')
                os.system("shutdown /s /t 1")
                
            elif 'no' in y_n:
                speak('Shutdown process stop')
                exit()

        elif 'restart' in que:
            que=que.replace(que,'')
            speak('Do you really want to restart your PC')
            speak('Yes:  Restart\nNo:  Terminate restart')
            r_p=Listen()
            
            if 'yes' in r_p:
                speak('Restarting your PC...')
                os.system("shutdown /r /t 1")

            elif 'no' in r_p:
                speak('Restart process stop')
                exit()