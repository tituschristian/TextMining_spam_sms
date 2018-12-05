from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math
import csv
import numpy as np
import string
from collections import OrderedDict
exclude = set(string.punctuation)
import re
 
#stopword
file_sw=open('tala.txt','r')
stopword= file_sw.read()
array_sw = stopword.split()

#stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def openFileCsv(namaFile):
	data_hasil = []
	with open(namaFile, mode='r', encoding='utf8') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		for row in csv_reader:
			data_hasil.append(row)
			line_count += 1
		print(f'Processed {line_count} lines.')
	return data_hasil

def lexicalAnalysis(sentence):
	#print(sentence)
	#case folding
	sentence = sentence.lower()
	
    #get all words to array
	words = sentence.split()
	
	#deleting link
	for n, row in enumerate(words):
		regex = r'((http(s)?://)[0-9a-z\./_+\(\)\$\#\&\!\?]+)'
		find_urls= re.compile(regex)
		url = find_urls.search(row)
		if url is not None:
			del words[n]
	#print("del link")
	#print(words)
	
	#deleting number
	for i in range(len(words)):
		temp =re.sub(r'[-*#:]?([\d]+([^ ]?[a-z\.\)/]*))+',' ',str(words[i]))
		words[i] = temp
	#print("del number")
	#print(words)
	
	#deleting symbol
	for i in range(len(words)):
		temp = re.sub(r'([a-z]*[-*&+/]{1}[a-z0-9]*)',' ',str(words[i]))
		words[i] = temp
	#print("del symbol")
	#print(words)
	
	#clean the space
	token=[]
	for row in words:
		temp = row.split()
		token += temp
	#print("del space")
	#print(token)
	
	return token
	
def stopwordRemoval(data):
    #filtered by sastrawi
    for i in range(len(data)):
        for n, row in enumerate(data):
            if row in array_sw:
                del data[n]
    return data

def stemming(data):
    sentence = ' '.join(data)
    output = stemmer.stem(sentence)
    hasil_stem = output.split()
    array_stem = []
    for row in hasil_stem:
        array_stem.append(row)
    return array_stem

def generateTerm(sentence):
	#print(sentence)
	token = lexicalAnalysis(sentence)
	#print(token)
	token = stemming(token)
	#print(token)
	term = stopwordRemoval(token)
	#print(term)
	return term
	
def generateTermInSentence(sentence):
	term = generateTerm(sentence)
	newSentence = ""
	for word in term:
		newSentence += word + " "
	#print(term)
	return newSentence.rstrip()
	
def getAllTerm():
	file = openFileCsv('data_coba_training.csv')
	term = []
	for row in file:
		thisTerm = generateTerm(row["Teks"])
		for item in thisTerm:
			if item not in term:
				term.append(item)
	return term