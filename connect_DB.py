import psycopg2

#Соединение с БД
def connectToDB(request):#(request, db_file, db_user, db_password, localhost)
	#Соеденить с БД
	conn = psycopg2.connect(dbname='db_file', 
							user='db_user', 
							password='db_password', 
							host='localhost')
	cursor = conn.cursor()
	
	#Выполнить запрос
	cursor.execute(request)#('''SELECT * 
							#   FROM table''')
	answer = cursor
	cursor.close()
	conn.close()
	return answer

#Поиск в БД по ключевому слову
def searchInDB(word):
	#ключевое слово: запрос
	#Пример 'расписание': 'SELECT что-то FROM timetable',
	requests = {
		'': '',
		'': '',
		'': '',
		'': '',
		}
	#Выбрать запрос по ключевому слову
	for key, value in requests:
		if word == key:
			request = value
	
	return request
