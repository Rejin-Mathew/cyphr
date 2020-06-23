import pyttsx3
import webbrowser
import smtplib
import random
import sqlite3
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import urllib.request
import urllib.parse
import re
import webbrowser as wb

cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
email_qus = ['send email','i want to send an email','send mail']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?',"how are you?", "are you okay?", "you okay there", "is everything okay?", "hope you doing well"]
responses = ['Okay', "I'm fine","I am fine, Thank you", "I am okay", "I guess i am okay",'Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
var1 = ['who made you', 'who created you',"Who are you?", "Tell me about yourself ", "who do you think you are?","explain yourself",'what is you name']
var2 = ["I am cyphr a digital assistant.A group of programmers known as Lonely programmers created me."]
cmd2 = ['play music', 'play songs', 'play a song']
cmd4 = ['open youtube', 'i want to watch a video']
cmd6 = ['exit', 'close', 'goodbye', 'abort','stop']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?', 'are you black or white?', 'are you black or white']
colrep = ['I am not a racist come on man why do you ask that,you guys all bleed the same colour']
cmd8 = ['what is your favourite colour', 'what is your favourite color']
cmd9 = ['I prefer sky blue']
cmd10 = ['thank you']
cmd11 = ['youre welcome', 'glad i could help you']
todo = ['i want to create a to do list','open to do list','to do list']
which_email = ['use your email id', 'use your email', 'use yours']
random_email = ['use mine','use my email id','use my email']
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('QXJREJ-8PUHE9PVTX')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Cyphr: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant Cipher!')
speak('How may I help you?')
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':
    while True:
        query = myCommand();
        query = query.lower()
        if query in cmd4:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open facebook' in query:
            speak('okay')
            webbrowser.open('https://www.facebook.com/')
        elif 'open twitter' in query:
            speak('okay')
            webbrowser.open('https://twitter.com/')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif query in cmd3:
            speak(random.choice(jokes))
        elif query in question:
            #stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(responses))
        elif query in var1:
            speak(random.choice(var2))
        elif query in cmd7:
            speak(random.choice(colrep))
        elif query in cmd8:
            speak(random.choice(cmd9))
        elif query in email_qus :
            speak("Do you want me to use my email id to sent your email or yours?")
            option = myCommand()
            if option in which_email:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()

                    smtp.login('cyphr.personalassistant@gmail.com','virtualassistantcyphr')
                    speak("enter the subject:")
                    subject = myCommand()
                    speak("enter the content:")
                    body = myCommand()
                    to_email = str(input("enter the recipients email:"))


                    msg = f'Subject: {subject}\n\n{body}'

                    smtp.sendmail('cyphr.personalassistant@gmail.com',to_email, msg)
            elif option in random_email:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    email_id = str(input("enter your email id of the sender:"))
                    pass_id = str(input("enter your password:"))
                    to_email = str(input("enter the recipients email:"))


                    smtp.login(email_id,pass_id)
                    speak("enter the subject:")
                    subject = myCommand()
                    speak("enter the content:")
                    body = myCommand()
                    #subject = str(input("enter the Subject"))
                    #body = input("enter the content:")

                    msg = f'Subject: {subject}\n\n{body}'

                    smtp.sendmail(email_id,to_email, msg)
            else:
                speak('Sorry Sir! I am unable to send your message at this moment!')
        elif query in cmd6:
            speak('okay')
            speak('Bye Sir, have a good day.')
            #db.commit()
            #db.close()
            sys.exit()
        elif query in greetings :
            speak(random.choice(greetings))
        elif 'bye' in query:
            speak('Bye Sir.')
        elif query in cmd10:
            speak(random.choice(cmd11))
        elif query in cmd2 :
            #music_folder = Your_music_folder_path
            #music = [music1, music2, music3, music4, music5]
            #random_music = music_folder + random.choice(music) + '.mp3'
            #os.system(random_music)
            #cont = myCommand()
            speak('please say what you want to hear')
            cont = myCommand()
            query_string = urllib.parse.urlencode({"search_query" : cont})#input()})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            print("http://www.youtube.com/watch?v=" + search_results[0])
            wb.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))
            #webbrowser.open('https://google.com/search?q=%s'%(cont))
            speak('Okay, here is your music! Enjoy!')
        elif query in todo:         #todo list starts here
            db = sqlite3.connect('TODO_LIST.db')
            c = db.cursor()
            def insert_content(todo_contentnumber,todo_content,todo_datetime):
                with db:
                    c.execute("INSERT INTO todolist VALUES(:content_number,:content,:content_date_time)", {'content_number':todo_contentnumber,'content':todo_content,'content_date_time':todo_datetime})

            def get_content():
                c.execute("SELECT * FROM todolist") #WHERE content=content",{'content':random_content})
                #print(c.fetchall())
                obj = c.fetchall()
                row_count = len(obj)
                j = 0
                str1="Number"
                str2="Content"
                str3="Date-Time"
                print(str1.center(00),end = " ")
                print(str2.center(10),end = " ")
                print(str3.center(10),end = "\n")
                print("---------------------------------------------------------------------")
                while j<row_count:
                    print(obj[j][0],end = " ")
                    print(obj[j][1],end = " ")
                    print(obj[j][2],end = "\n")
                    #print(obj[j][0],' '*(12-len(obj[j])),obj [j][1],' '*(12-len(obj[j][1])), obj [j][2],' '*(12-len(obj[j][2])))
                    j = j+1
                print("\n\n")
            def delete_content(remove_content):
                with db:
                    c.execute("DELETE FROM todolist WHERE content=:content", {'content':remove_content})




            content = []
            while True:
                speak("TO DO LIST MENU")
                speak("1)add to the list")
                speak("2)remove from the list")
                speak("3)Display the list")
                speak("4)exit the list")
                #option = input(speak("enter the option"))
                speak("enter the option")
                option = myCommand()
                if option == '1':
                    #num = int(input(speak("How many contents do you wish to add?")))
                    speak("How many contents do you wish to add?")
                    num = int(myCommand())
                    for i in range(num):
                        #todo_content = input(speak("enter the content"))
                        speak("enter the content")
                        todo_content = myCommand()
                        #todo_datetime = input(speak("enter the corresponding date and time"))
                        speak("enter the corresponding date and time")
                        todo_datetime = myCommand()
                        todo_contentnumber = i
                        todo_contentnumber +=1
                        insert_content(todo_contentnumber,todo_content,todo_datetime)
                        #content.append(add_content)
                elif option == '2':
                    try:
                        #remove_content = input(speak("enter the content to remove"))
                        speak("enter the content to remove")
                        remove_content = myCommand()
                        delete_content(remove_content)
                        #content.remove(remove_content)
                    except IndexError:
                        speak("cannot perform task")
                elif option == '3':
                    #for i in range(len(content)):
                        #print(content[i])
                    #random_content = input("enter the content to display")
                    get_content()
                elif option == '4':
                    db.commit()
                    db.close()
                    break

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    #speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                except:
                     results = wikipedia.summary(query, sentences=3)
                     speak('Got it.')
                     #speak('WIKIPEDIA says - ')
                     speak(results)
            except:
                #webbrowser.open('www.google.com')
                webbrowser.open('https://google.com/search?q=%s'%(query))
                speak('Next Command! Sir!')
