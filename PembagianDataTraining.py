import csv

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

def generateData(csv_file):
	line_count = 0
	count_zero = 455 # 569 * 80 %
	count_one  = 268 # 335 * 80 %
	count_two  = 191 # 239 * 80 %
	global list_zero
	global list_one
	global list_two
	global list_data_uji
	for row in csv_reader:
		if line_count != 0:
			#print("---> ", row)
			if int(row["label"]) == 0 and count_zero != 0:
				list_zero.append(row)
				count_zero -= 1
			elif int(row["label"]) == 1 and count_one != 0:
				list_one.append(row)
				count_one -= 1
			elif int(row["label"]) == 2 and count_two != 0:
				list_two.append(row)
				count_two -= 1
			else:
				list_data_uji.append(row)
		line_count += 1
	print(f'Processed read {line_count} lines.')
		
def createFileCsv(namaFile, data0, data1 = [], data2 = []):
	with open(namaFile, mode='w' , newline='', encoding='utf8') as csv_file:
		fieldnames = ['Teks', 'label']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

		writer.writeheader()
		
		line_count = 0
		for row in data0:
			writer.writerow({'Teks': row["Teks"], 'label': row["label"]})
			line_count += 1
			
		for row in data1:
			writer.writerow({'Teks': row["Teks"], 'label': row["label"]})
			line_count += 1
			
		for row in data2:
			writer.writerow({'Teks': row["Teks"], 'label': row["label"]})
			line_count += 1
			
		print(f'Processed write {line_count} lines.')

def run():
	list_zero = []
	list_one = []
	list_two = []
	list_data_uji = []
	data_set = openFileCsv('dataset_kemarin_malam.csv')
	generateData(data_set)
	createFileCsv('data_training.csv', list_zero, list_one, list_two)
	createFileCsv('data_uji.csv', list_data_uji)