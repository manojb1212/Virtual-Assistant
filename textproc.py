# All functions defined here

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
import numpy as np


def querycsv(command):
	words = word_tokenize(command)
    
	if 'p1' in words and 'june' in words:   
        	mydf = pd.read_csv("hackathon.csv")
       		counts = mydf[(mydf.Type == 'P1') & (mydf.Month == 'June')].shape[0]
		return(counts)
    
	elif 'p2' in words and 'june' in words:
       		mydf = pd.read_csv("hackathon.csv")
       		counts = mydf[(mydf.Type == 'P2') & (mydf.Month == 'June')].shape[0]
		return(counts)       
         
	elif 'p1' in words and 'august' in words:
       		mydf = pd.read_csv("hackathon.csv")
       		counts = mydf[(mydf.Type == 'P1') & (mydf.Month == 'August')].shape[0]
		return(counts)     

	elif 'p2' in words and 'august' in words:
       		mydf = pd.read_csv("hackathon.csv")
       		counts = mydf[(mydf.Type == 'P2') & (mydf.Month == 'August')].shape[0]
		return(counts)     
	else:
		return 0
   
	               
