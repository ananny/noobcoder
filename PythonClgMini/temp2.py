import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP

win = Tk()

win.geometry("600x450+100+100")
win.title("Emotion Selection")


def extract_emote(urlhere):
	response = HTTP.get(urlhere)
	data = response.text 
	soup = SOUP(data, "lxml") 
	return soup

def get_title(soup):
	my_title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
	return my_title



def split_emote(a,emotion):
	count = 0
	for i in a:
			tmp = str(i).split('>')
			if(len(tmp) == 3):
				print(tmp[1][:-3])
				if(count > 11): 
					break
				count+=1	
	return 

    


def action_Sad():
	emotion="Sad"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return

def action_Disgust():
	emotion="Disgust"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return

def action_Anger():
	emotion="Anger"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return

def action_Anticipation():
	emotion="Anticipation"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return

def action_Fear():
	emotion="Fear"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return

def action_Enjoyment():
	emotion="Enjoyment"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return

def action_Trust():
	emotion="Trust"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return

def action_Surprise():
	emotion="Surprise"
	print("\nThe Recommended Movies by The Emotional Buff for "+emotion+" Emotion are:\n")
	urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
	soup=extract_emote(urlhere)
	a=get_title(soup)
	split_emote(a,emotion)
	return


label = Label(win, font = ('arial',25,'bold'), text ="How are you feeling today?", fg = "steel blue", bd = 15, anchor = 'w').pack()

Sad_but=Button(win,font = ('arial',15), text="Sad",border='3px',command= action_Sad).pack()
Disgusted_but=Button(win,font = ('arial',15), text="Disgusted",border='3px',command= action_Disgust).pack()
Anger_but=Button(win,font = ('arial',15), text="Anger",border='3px',command= action_Anger).pack()
Excited_but=Button(win,font = ('arial',15), text="Excited",border='3px',command= action_Anticipation).pack()
Fearful_but=Button(win,font = ('arial',15), text="Fearful",border='3px',command= action_Fear).pack()
Joyful_but=Button(win,font = ('arial',15), text="Joyful",border='3px',command= action_Enjoyment).pack()
Trusted_but=Button(win,font = ('arial',15), text="Trusted",border='3px',command= action_Trust).pack()
Surprised_but=Button(win,font = ('arial',15), text="Surprised",border='3px',command= action_Surprise).pack()

win.mainloop()
