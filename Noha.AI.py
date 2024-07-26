#it is a text to speech conversion librey in python,install by terminal.
import pyttsx3 

 #it is use where we need time and date.it is already install.
import datetime

 # it is a machine ability to yo listen to spoken words and identify them,install by terminal.
import speech_recognition as sr

# it is use to search anything in browser.and install by terminal
import webbrowser

# it is use to operate whatsapp funtion.install by terminal.
import pywhatkit

 # it give a data from wikipedia , install by terminal.
import wikipedia

#already install
import os

 # It is control the mouse and keyboard to automate interactions with other applications,it is use for screen short.already installed.
import pyautogui

import keyboard

import pyjokes


# In this we can add  the voices . in computer present only two voice,in this added more voices with the help of setting.voice is present in male and female both and this voice controll speed ,quality etc. voices is present in number.
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voice', voices[1].id)

# this function is use for voice,audio and speak.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Noha maam. please tell me how may i help you")
# here is interduce a takecommand.

def takecommand():
    # it takes microphone input fron the user and return string output.

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold= 1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said :{ query}\n")

    except Exception as e:
        #print(e)

        print("say that again please...")
        return "None"
    return query
# Here is  define a music funtion.here is important to put the location of file.

def music():
    speak("Tell Me The Name of Song")
    musicName=takecommand()
    if 'kaffi hai'in musicName:
        os.startfile('C:\\User\\NIKKI\\Music\\kaffi hai.mp3')

    elif 'meri baari'in query:
        os.startfile('C:\\User\\NIKKI\\Music\\meri baari.mp3')

    else:
        pywhatkit.playonyt(musicName)

    speak("Ypur Song Has Been Started, Enjoy Maam")
# Here is define a whatsapp function.

def whatsapp():
    speak("Tell Me The Name of Person")
    name=takecommand()

    if 'Babita'in name:
        speak("Tell Me The Message!")
        msg=takecommand()
        speak("Tell Me The Time Maam!")
        speak("Time In Hour!")
        hour=int(takecommand())
        speak("Time In Minutes!")
        min=int(takecommand())
        pywhatkit.sendwhatmsg("+917972944292",msg,hour,min,20)
        speak("ok maam!,Sending whatsapp message")


    elif 'mitali'in name:
        speak("Tell Me The Message!")
        msg=takecommand()
        speak("Tell Me The Time Maam!")
        speak("Time In Hour!")
        hour=int(takecommand())
        speak("Time In Minutes!")
        min=int(takecommand())
        pywhatkit.sendwhatmsg("+919322516364",msg,hour,min,20)
        speak("ok maam!,Sending whatsapp message")


    elif 'secret book'in name:
        speak("Tell Me The Message!")
        msg=takecommand()
        speak("Tell Me The Time Maam!")
        speak("Time In Hour!")
        hour=int(takecommand())
        speak("Time In Minutes!")
        min=int(takecommand())
        pywhatkit.sendwhatmsg("+917045856998",msg,hour,min,20)
        speak("ok maam!,Sending whatsapp message")

    else:
        speak("Tell Me The Message!")
        msg=takecommand()
        phone=int(takecommand())
        ph='+91'+ phone
        speak("Tell Me The Time Maam!")
        speak("Time In Hour!")
        hour=int(takecommand())
        speak("Time In Minutes!")
        min=int(takecommand())
        pywhatkit.sendwhatmsg("ph",msg,hour,min,20)
        speak("ok maam!,Sending whatsapp message")
        

def OpenApp():
    speak("ok maam,wait a second")

    if 'code 'in query:
        os.startfile("C:\\Users\\NIKKI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif ' telegram' in query:
        webbrowser.open("https://web.telegram.org/a/")

    elif 'chrome' in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'facebook'in query:
        webbrowser.open("https://www.facebook.com/")

    elif 'instagram' in query:
        webbrowser.open("https://www.instagram.com/")

    
    elif 'map' in query:
        webbrowser.open("https://www.google.com/maps/place/@19.117621,72.8656388,17z")

    elif 'spotify' in query:
        webbrowser.open("spotify.com")

    elif "youtube" in query :
        webbrowser.open("youtube.com")

        speak("your command has been completed maam!") 


def CloseApp():
    speak("ok maam,wait a second ")

    if 'youtube' in query:
        os.system(f"TASKKILL /f/in youtube.exe")
        
        

    elif 'instagram' in query:
        os.system("TASKKILL/f/in instagram.exe")
        

    elif 'code 'in query:
        os.system("TASKKILL/f/in code.exe")

    elif 'telegram' in query:
        os.system("TASKKILL/f/in telegram.exe")

    elif 'facebook'in query:
        os.system("TASKKILL/f/in facebook.exe")


    elif 'map' in query:
        os.system("TASKKILL/f/in map.exe")

    elif 'spotify' in query:
        os.system("TASKKILL/f/in spotify.exe")

    elif 'chrome' in query:
        os.system("TASKKILL/f/in chorme.exe")

        speak("your command has been completed maam!") 


def YoutubeAuto():
    speak("what yiur command?")
    comm=takecommand()

    if 'pause' in comm:
        keyboard.press("space bar")

    elif 'restart' in comm:
        keyboard.press("0")

    elif 'mute' in comm:
        keyboard.press("m")

    elif 'skip' in comm:
        keyboard.press("1")

    elif 'back' in comm:
        keyboard.press("j")

    elif 'full screen' in comm:
        keyboard.press("f")

    elif 'film mode' in comm:
        keyboard.press("t")

        speak("Done Maam")


def ChormeAuto():
    speak("Chrome Automation Started")
    command=takecommand()

    if 'close this tab' in command:
        keyboard.press_and_release("ctrl+w")

    elif 'open new tab' in command:
        keyboard.press_and_release("ctrl+t")

    elif 'open new window' in command:
        keyboard.press_and_release("ctrl+n")

    elif 'histroy' in command:
        keyboard.press_and_release("ctrl+h")

        speak("Done Maam")



__name__=="_main_"
wishMe()
while True:
#if 1:
    query = takecommand().lower()


    if 'youtube search ' in query :
        speak("ok maam,This is what ,I found for your searching")
        query=query.replace("Noha","")
        query=query.replace("youtube search","")
        web="https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        speak("Done maam!")


    elif  'Google search ' in query :
        speak("ok maam,This is what ,I found for your searching")
        query=query.replace("Noha","")
        query=query.replace("Google search","")
        pywhatkit.search(query)
        speak("Done maam!")


    elif 'wikipedia' in query:
        speak('wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=4)
        speak("According to wikipedia")
        speak(results)

    elif 'Launch' in query:
        speak("Tell Me The Name of The Website")
        name=takecommand()
        web='https://www.'+ name +'.com'
        webbrowser.open(web)
        speak("Done maam!")


    elif 'play music' in query:
        music() 


    elif 'wikipedia' in query:
        speak("searching wikipedia......")
        query=query.replace("Noha","")
        query=query.replace("wikipedia","")
        wiki=wikipedia.summary(query,4)
        speak("According to wikipedia:{wiki}")


    elif'whatsapp' in query:
        whatsapp()


    elif 'screenshot' in query:
        a=pyautogui.screenshot()
        a.save("C:\\Users\\NIKKI\\Pictures\\Saved Pictures")


    elif 'open code 'in query:
        OpenApp()


    elif 'open telegram' in query:
        OpenApp()


    elif 'open chrome' in query:
         OpenApp()


    elif 'open facebook'in query:
        OpenApp()


    elif 'open instagram' in query:
        OpenApp()

        OpenApp()


    elif'open map' in query:
        OpenApp()


    elif 'open spotify' in query:
        OpenApp()


    elif "open youtube" in query :
        OpenApp()


    elif 'close youtube' in query:
        CloseApp()


    elif 'close instrgram' in query:
        CloseApp()


    elif 'close code 'in query:
        CloseApp()


    elif 'close telegram' in query:
        CloseApp()


    elif 'close facebook'in query:
        CloseApp()


    elif 'close map' in query:
        CloseApp()


    elif 'close spotify' in query:
        CloseApp()


    elif 'close chrome' in query:
        CloseApp()


    elif'pause' in query:
        keyboard.press("space bar")

    elif 'restart' in  query:
        keyboard.press("0")

    elif 'mute' in  query:
        keyboard.press("m")

    elif 'skip' in  query:
        keyboard.press("1")

    elif 'back' in  query:
        keyboard.press("j")

    elif 'full screen' in  query:
        keyboard.press("f")

    elif 'film mode' in  query:
        keyboard.press("t")

    elif 'youtube tool' in query:
        YoutubeAuto()


    elif 'close this tab' in query:
        keyboard.press_and_release("ctrl+w")

    elif 'open new tab' in query:
        keyboard.press_and_release("ctrl+t")

    elif'open new window' in query:
        keyboard.press_and_release("ctrl+n")

    elif 'histroy' in query:
        keyboard.press_and_release("ctrl+h")

    elif 'chorme automation' in query:
        ChormeAuto()

    elif 'joke ' in query:
        get=pyjokes.get_joke()
        speak(get)

    elif 'repeat my word' in query:
        speak("speak maam")
        jj=takecommand()
        speak(f"You Said:[jj]")

    
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"maam, the time is {strTime}")



    




    










    

 