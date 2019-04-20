#import psycopg2
import sqlite3

#Соединение с базой данных
def connectToDB(request):
    conn = sqlite3.connect('db_users.db')
    cursor = conn.cursor()
    
    cursor.execute(str(request),'1')
    answer = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return answer[0]

#Выбрать запрос к базе данных
def searchInDB(words):
    #ключевое слово: запрос
    requests = {
        'номер': 'SELECT number FROM users WHERE id=?',
        'телефон': 'SELECT number FROM users WHERE id=?',
        'почта': 'SELECT email FROM users WHERE id=?',
        'email': 'SELECT email FROM users WHERE id=?',
    }
    
    for key, value in requests.items():
        for word in words:
            if word == key:
                request = value
                return request
