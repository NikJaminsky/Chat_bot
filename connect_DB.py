import psycopg2

#Соединение с БД
def connectToDB(request, db_file, db_user, db_password, localhost)
    conn = psycopg2.connect(dbname=db_file, 
							user=db_user, 
							password=db_password, 
							host=localhost)
    cursor = conn.cursor()
    
    cursor.execute(request)#('''SELECT * 
							#   FROM table''')
    
    cursor.close()
    conn.close()

def searchInDB(word):
    requests = {
		'': '',
		'': '',
		'': '',
		'': '',
		'': '',
		}
	
	for key, value in requests:
		if word == key:
			request = value
	
	return request
