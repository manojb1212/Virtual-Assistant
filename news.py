from newsapi import NewsApiClient
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

api = NewsApiClient(api_key='8d05d43fa57142b1acbe6f10a053f45a')


def querynews(command):
	
	words = word_tokenize(command)
	headlines = ' '

	if 'india' in words:
		data = api.get_top_headlines(sources='the-times-of-india')
		i = 0
		for each in data['articles'] :
			headlines = str(headlines) + '\n' + data['articles'][i]['title']
			i = i + 1
		return(headlines)

	elif 'cricket' in words:
		data = api.get_top_headlines(sources='espn-cric-info')
		i = 0
		for each in data['articles'] :
			headlines = str(headlines) + '\n' + data['articles'][i]['title']
			i = i + 1
		return(headlines)
	else:
		data = api.get_top_headlines(sources='bbc-news')
		i = 0
		for each in data['articles'] :
			headlines = str(headlines) + '\n' + data['articles'][i]['title']
			i = i + 1
		return(headlines)
	

