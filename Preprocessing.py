from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import PembagianDataTraining as training
import re

def lexical_analysis(regex, data_test):
	p = re.compile(regex)
	for row in data_test:
		m = p.search(row["Teks"])
		string = row["Teks"]
		#print(m)
		while m != None and m.end() - m.start() != 0:
			string = string[:m.start()] + string[int(m.end()):]
			string = string.lstrip(' ')
			m = p.search(string)
			#print(m)
		#print(string)
		row["Teks"] = string
	return data_test
		
def printData(data_test):
	for row in data_test:
		print(row["Teks"])
			
def stemming(data_test):
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()
	
	for row in data_test:
		kalimat = row["Teks"]
		katadasar = stemmer.stem(kalimat)
		row["Teks"] = katadasar
	return data_test

RENumber = '[-*#:]?([\d]+([^ ]?[a-zA-Z/]*))+'
RELink = '((http://)[0-9a-z\./_+\(\)\$\#\&\!\?]+)'
RESymbol = '([a-zA-Z]*[-*&+/]{1}[a-zA-Z]*)'
data_csv = training.openFileCsv('data_coba.csv')	
data_csv = lexical_analysis(RENumber, data_csv)
data_csv = lexical_analysis(RELink, data_csv)
data_csv = lexical_analysis(RESymbol, data_csv)
data_csv = stemming(data_csv)
#printData(data_csv)

training.createFileCsv('hasil_preprocessing.csv', data_csv)