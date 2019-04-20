import sys
import sqlite3

#Соединение с базой данных
def connectToDB(request, surname):
    conn = sqlite3.connect('db_users.db')
    cursor = conn.cursor()

    cursor.execute(str(request), (surname,))#,'1'
    answer = cursor.fetchone()

    cursor.close()
    conn.close()
    return answer[0]

#Выбрать запрос к базе данных
def searchInDB(word):
    #ключевое слово: запрос
    requests = {
        'номер': 'SELECT number FROM users WHERE middle_name=?',
        'телефон': 'SELECT number FROM users WHERE middle_name=?',
        'почта': 'SELECT email FROM users WHERE middle_name=?',
        'email': 'SELECT email FROM users WHERE middle_name=?',
    }
    #print(word)
    for key, value in requests.items():
        if key == word:
            request = value
            return request

#Загрузить ФИО
def loadName():
    conn = sqlite3.connect('db_users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT name, middle_name, second_name FROM users')
    answer = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return answer