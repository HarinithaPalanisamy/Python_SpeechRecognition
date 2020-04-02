import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import sys
from bs4 import BeautifulSoup
import datetime
engine = pyttsx3.init()
while True:
    x = input("Enter Password:  ")
              
    if x == "":
        print("""

            """)
        print( '  /\   |     ___  \ /   /\ ')
        print( " /__\  |    |___   \   /__\ ")
        print( '/    \ |___ |___  / \ /    \     --Verision 3.0.28')
        print("""

            """)
        print("C: Hi! I am Alexa,your Virtual Assistant")
        engine.say("hey hi")
        engine.say("I am Alexa,your Virtual Assistant")
        engine.say("speed one megabyte,memory one gigabyte")
        time = datetime.datetime.now()
        print("C: How can I help you Boss?")
        engine.say("How can I help you Boss")
        engine.runAndWait()
        while True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                                       print("C: Listening...")
                                       engine.say("listening")
                                       engine.runAndWait()
                                       audio = r.listen(source)
                                       speech = r.recognize_google(audio)
                                       print("You Said-- "+speech)
                                       
                                       
                                                                        
                                       if "open Facebook" in speech:
                                                           r = sr.Recognizer()
                                                           with sr.Microphone() as source:
                                                                           print("C: Opening facebook...")
                                                                           engine.say("opening facebook")
                                                                           webbrowser.open("www.facebook.com")
                                                                           print("C: Do you Want to continue???  (Yes or No)")
                                                                           engine.say("do you want to continue?")
                                                                           print("Listening...")
                                                                           engine.say("listening")
                                                                           engine.runAndWait()
                                                                           audiia = r.listen(source)
                                                                           speiia = r.recognize_google(audiia)
                                                                           print("You said--",speiia)
                                                                           if "no" in speiia:
                                                                               print("""C: Thank you , Have a nice day""")
                                                                               engine.say("Thank you, have a nice day")
                                                                               engine.runAndWait()
                                                                               sys.exit()
                                                                               
                                                                           else:
                                                                               print("C: How could I help you Boss??? ")
                                                                               engine.say("how could i help you boss")
                                                                               engine.runAndWait()
                                                                               
                                       elif 'Wikipedia' in speech:
                                                           r = sr.Recognizer()
                                                           with sr.Microphone() as source:
                                                                           print("C: What to search with BOSS?  ")
                                                                           engine.say("what to search with boss")
                                                                           print("C: Listening...")
                                                                           engine.say("listening")
                                                                           engine.runAndWait()
                                                                           audio = r.listen(source)
                                                                           speec = r.recognize_google(audio)
                                                                           print("You said-- ",speec)
                                                                           speec = wikipedia.summary(speec)
                                                                           print(speec)
                                                                           print("C: Do you Want to continue???  (Yes or No)")
                                                                           engine.say("do you want to continue?")
                                                                           print("Listening...")
                                                                           engine.say("listening")
                                                                           engine.runAndWait()
                                                                           audiia = r.listen(source)
                                                                           speiia = r.recognize_google(audiia)
                                                                           print("You said--",speiia)
                                                                           
                                                                           if "no" in speiia:
                                                                               
                                                                               print("""C: Thank you , Have a nice day""")
                                                                               engine.say("Thank you, have a nice day")
                                                                               engine.runAndWait()
                                                                               sys.exit()
                                                                           else:
                                                                               print("C: How could I help you Boss??? ")
                                                                               engine.say("how could i help you boss")
                                                                               engine.runAndWait()
                                       
                                                                                               
                                                                           
                                       elif 'open Google' in speech:
                                                           r = sr.Recognizer()
                                                           with sr.Microphone() as source:
                                                                           print("C: What to search in Google BOSS?")
                                                                           engine.say("what to search with boss")
                                                                           print("C: Listening...")
                                                                           engine.say("listening")
                                                                           engine.runAndWait()
                                                                           audioo = r.listen(source)                                                               
                                                                           speeco = r.recognize_google(audioo)
                                                                           print("You Said-- "+speeco)
                                                                           webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN806IN808&ei=-OCzXeHaEZqv9QOG2ZCYAg&q="+speeco+"&oq="+speeco+"&gs_l=psy-ab.3..0l10.11272.19534..20584...0.2..3.308.2802.0j17j1j1......0....1..gws-wiz.....6..0i71j0i131i67j0i131j0i362i308i154i357j0i67j0i10i67.zNzffdQ9Tj8&ved=0ahUKEwjhtpLcn7nlAhWaV30KHYYsBCMQ4dUDCAs&uact=5")
                                                                           print("C: Do you Want to continue???  (Yes or No)")
                                                                           engine.say("do you want to continue?")
                                                                           print("Listening...")
                                                                           engine.say("listening")
                                                                           engine.runAndWait()
                                                                           audiia = r.listen(source)
                                                                           speiia = r.recognize_google(audiia)
                                                                           print("You said--",speiia)
                                                                           
                                                                           if "no" in speiia:
                                                                               
                                                                               print("""C: Thank you , Have a nice day""")
                                                                               engine.say("Thank you, have a nice day")
                                                                               engine.runAndWait()
                                                                               sys.exit()
                                                                           else:
                                                                               print("C: How could I help you Boss??? ")
                                                                               engine.say("how could i help you boss")
                                                                               engine.runAndWait()
                                       elif 'time' in speech:
                                                           print("C: It's Now", time.strftime("%H : %M"))
                                                           r = sr.Recognizer()
                                                           with sr.Microphone() as source:
                                                                           print("C: Do you Want to continue???  (Yes or No)")
                                                                           engine.say("do you want to continue?")
                                                                           print("Listening...")
                                                                           engine.say("listening")
                                                                           engine.runAndWait()
                                                                           audiia = r.listen(source)
                                                                           speiia = r.recognize_google(audiia)
                                                                           print("You said--",speiia)
                                                                           engine.runAndWait()
                                                                           if "no" in speiia:
                                                                               
                                                                               print("""C: Thank you , Have a nice day""")
                                                                               engine.say("Thank you, have a nice day")
                                                                               engine.runAndWait()
                                                                               sys.exit()
                                                                           else:
                                                                               print("C: How could I help you Boss??? ")
                                                                               engine.say("how could i help you boss")
                                                                               engine.runAndWait()
                                       elif 'nothing' in speech:
                                                           print("C: Your's Welcome BOSS")
                                                           engine.say("yours welcome boss")
                                                           engine.runAndWait()                                                           
                                                           sys.exit()
                                                           
                                                       
                                       elif 'open YouTube' in speech:
                                                           r = sr.Recognizer()
                                                           with sr.Microphone() as source:
                                                                print("C: What to play Boss?")
                                                                engine.say("what to play boss")
                                                                print("Listening...")
                                                                engine.say("listening")
                                                                engine.runAndWait()
                                                                audios = r.listen(source)
                                                                speechs = r.recognize_google(audios)
                                                                print("You Said-- "+speechs)
                                                                webbrowser.open("https://www.youtube.com/results?search_query="+speechs)
                                                                print("C: Do you Want to continue???  (Yes or No)")
                                                                engine.say("do you want to continue?")
                                                                print("Listening...")
                                                                engine.say("listening")
                                                                engine.runAndWait()
                                                                audiia = r.listen(source)
                                                                speiia = r.recognize_google(audiia)
                                                                print("You said--",speiia)
                                                                
                                                                if "no" in speiia:
                                                                     
                                                                     print("""C: Thank you , Have a nice day""")
                                                                     engine.say("Thank you, have a nice day")
                                                                     engine.runAndWait()
                                                                     sys.exit()
                                                                else:
                                                                     print("C: How could I help you Boss??? ")
                                                                     engine.say("how could i help you boss")
                                                                     engine.runAndWait()
                                           
                                       elif "open command prompt" in speech:
                                               import subprocess
                                               subprocess.Popen([r"cmd"])
                                               print("C: Do you Want to continue???  (Yes or No)")
                                               engine.say("do you want to continue?")
                                               print("Listening...")
                                               engine.say("listening")
                                               engine.runAndWait()
                                               audiia = r.listen(source)
                                               speiia = r.recognize_google(audiia)
                                               print("You said--",speiia)
                                               
                                               if "no" in speiia:
                                                   
                                                   print("""C: Thank you , Have a nice day""")
                                                   engine.say("Thank you, have a nice day")
                                                   engine.runAndWait()
                                                   sys.exit()
                                               else:
                                                   print("C: How could I help you Boss??? ")
                                                   engine.say("how could i help you boss")
                                                   engine.runAndWait()
                                                           
                                       else:
                                            print("C: I can't Understand BOSS")
                                            engine.say("i cant understand boss")
                                            print("C: Try using simple Words ")
                                            engine.say("try using simple words")
                                            engine.runAndWait()
    else:
        print("C: Incorrect Password")
        print("C: Please try again")
        print("""
""")
    engine.runAndWait()
