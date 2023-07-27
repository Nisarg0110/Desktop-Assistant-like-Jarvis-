import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit as kit
import os

paths_pc = {
    'vscode': "C:\\Program Files\\Microsoft VS Code\\Code.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
	'noteped': "C:\\Program Files\\Notepad++\\notepad++.exe"
}

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am desktop assistant Sir. Please tell me how may I help you")

def takeCommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Listening')
		
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	
	engine.setProperty('voice', voices[0].id)
	
	engine.say(audio)

	engine.runAndWait()

def tellDay():
	
	day = datetime.datetime.today().weekday() + 1
	
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	time = str(datetime.datetime.now())
	
	print(time)
	# speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")

def Hello():
	
	speak("hello sir I am your desktop assistant. /Tell me how may I help you")

def play_on_youtube(video):

    kit.playonyt(video)

def Take_query():

	# Hello()
	
	while(True):
		
		query = takeCommand().lower()
		if "open geeksforgeeks" in query:
			speak("Opening GeeksforGeeks ")
			webbrowser.open("www.geeksforgeeks.com")
			continue
		
		elif "open stack overflow" in query:
			webbrowser.open("stackoverflow.com")
			continue
			
		elif "open google" in query:
			speak("Opening Google ")
			# webbrowser.open("www.google.com")
			speak("Enter what you want to search ")
			exp1=input()
			kit.search(exp1)
			continue
		
		elif "open calculator" in query:
			# speak("so enter the expression you want to calculte ")
			# st="https://"
			# en=".com"
			speak("Enter the two operands")
			exp1=input()
			exp2=input()
			speak("Enter the operation you want to perform")
			ch=input()
			if ch == '+':
				exp3=" add "
				exp1=exp1+exp3+exp2
			elif ch == '-':
				exp3=" minus "
				exp1=exp1+exp3+exp2
			elif ch == '*':
				exp3=" multiply "
				exp1=exp1+exp3+exp2
			elif ch == '/':
				exp3=" divide "
				exp1=exp1+exp3+exp2
			# st=st+exp
			# st=st+en
			print(exp1)
			# target1=exp
			kit.search(exp1)
			# webbrowser.open("exp")
			continue
		
		elif "vs code" in query:
			speak("Opening vscode")
			os.startfile(paths_pc['vscode'])
			continue

		elif "youtube" in query:
			speak("Enter what you want to search")
			search_yt=input().lower()
			play_on_youtube(search_yt)
			continue

		elif "wikipedia" in query:
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue
			
		elif "which day it is" in query:
			tellDay()
			continue
		
		elif "tell me the time" in query:
			tellTime()
			continue

		elif "bye" in query:
			speak("Bye, sir")
			exit()
		
		elif "tell me your name" in query:
			speak("I am Your desktop Assistant")
			continue

# if _name_ == "_main_":
	
	# main method for executing
	# the functions
wishMe()
Take_query()