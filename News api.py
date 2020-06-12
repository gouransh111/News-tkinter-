import requests
import json
import time
from tkinter import *
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def speak1():
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    for articles in arts:
       speak.Speak(articles['title'])
if __name__ == '__main__':
     root = Tk()
     root.geometry("900x600")
     f1 = Frame(root,bg = "cyan",borderwidth = 8)
     f1.pack(side = TOP)    
     root.title("News api")
     ro = Label(f1,text = "My gui on news \n",bg = "black",fg="cyan")
     ro.pack(fill=BOTH)
     f2 = Frame(root,bg = "purple",borderwidth = 8)
     f2.pack(side = BOTTOM) 
     ro2 = Label(f2,text = "Today's Latest News",bg = "black",fg = "cyan",padx = 32,font = "Arial 10 bold")
     ro2.pack(side = BOTTOM)
     f3 = Frame(root,bg = "purple",borderwidth = 8)
     f3.pack(side = TOP,anchor = "nw",fill = X,padx = 20,pady = 10)
     
     try:
        i =1
        speak("News for today ")
        url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=49151b1d44aa4d88afdd8234b07da744"
        news=requests.get(url).text
        news = json.loads(news) 
        arts= news['articles']
        for articles in arts:
            label = Label(f3,text = f"{i}. {articles['title']}",bg = "black",fg = "red",font = "Arial 8  bold")
            label.pack(anchor = "nw",fill = BOTH)
            #speak(articles['title'])
            i += 1
        b1 = Button(root,fg="black",text="For speaking news click here",command=speak1)
        b1.pack(side=BOTTOM)
       # b2 = Button(root,fg="black",text="To stop speaking news click here",command=speak3)
       # b2.pack(side=BOTTOM)
     except Exception as e:
         print(e)

root.mainloop()
