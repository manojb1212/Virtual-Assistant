import wx                                   
import wikipedia                   
import wolframalpha                
import  nltk
from nltk.tokenize import sent_tokenize, word_tokenize                       
from gtts import gTTS 
import speech_recognition as sr 
import os 
import re 
import webbrowser 
import smtplib 
import requests 
import psutil
import textproc
import news


app_id = "R2HYT6-GR3WKKWP6U"
client = wolframalpha.Client(app_id)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Digi")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am your Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):

        input = self.txt.GetValue()
        input = input.lower()
        

        if 'open website' in input: 
            reg_ex = re.search('open website (.+)', input) 
            if reg_ex: 
                domain = reg_ex.group(1) 
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url) 
                print('Done!') 

        elif 'current weather' in input:
            reg_ex = re.search('current weather in (.*)', input)
            if reg_ex:
                city = reg_ex.group(1)
                res = client.query(input)
                answer = next(res.results).text
                print(answer)

        elif 'whats cpu' in input:
            reg_ex = re.search('whats cpu (.*)', input)
            if reg_ex:
                parameter = reg_ex.group(1)
                param = 'cpu_'+ parameter
                answer = psutil.cpu_percent(interval = 1)
                print(answer)
       
        elif 'defects' in input:
             answer = textproc.querycsv(input)
             print(answer)

               
        elif 'news' in input:
             answer = news.querynews(input)
             print(answer)
       
        else:
	      print('Sorry..I dont know')	
  


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
