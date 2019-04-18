#import psycopg2
import sqlite3

#Соединение с БД
def connectToDB(request):#(request, db_file, db_user, db_password, localhost)
    #conn = psycopg2.connect(dbname='db_file', 
    #    user='db_user', 
    #    password='db_password', 
    #    host='localhost')
    conn = sqlite3.connect('vault.db')
    cursor = conn.cursor()
    
    cursor.execute(str(request),'1')
    #('''SELECT * 
    #   FROM table''')
    answer = cursor.fetchone()
    cursor.close()
    conn.close()
    return answer[0]

def searchInDB(words):
    #ключевое слово: запрос
    requests = {
        'хочу': 'SELECT path_source FROM files WHERE file_id=?',
        'у': 'у',
        'в': 'в',
        'й': 'й',
        'ц': 'ц',
    }

    for key, value in requests.items():
        for word in words:
            if word == key:
                request = value
                return request
