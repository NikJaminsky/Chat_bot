import random
from connect_DB import loadName

#Отправить сообщение боту
def sendMessage(text):
    return text

#Разделить сообщение на слова
def separateMessage(text):
    words = text.split(' ')	
    return words

#Выделить ключевые слова
def selectKeyWord(words):
    #Ключевые слова
    key_words = [
        'номер',
        'телефон',
        'почта',
        'email'
        ]

    select_word = ''
    select_surname = ''
    
    #Извлечь все ФИО
    names = loadName() 
    
    for word in words:
        for key in key_words:
            if key == word:
                select_word = word
        for tuple in names:
            if word in tuple:
                select_surname = tuple[1]
        
    return select_word, select_surname

#Выбрать шаблон ответа
def selectPattern(key_word):
    #Шаблон ответа
    patterns = {
        'номер': 'Телефон данного сотрудника, {0}',
        'телефон': 'Номер телефона {0} {1}',
        'почта': 'Почта {0} {1}',
        'email': 'Запрашиваемый электронный адрес {1} {0}',
        }

    for key, value in patterns.items():
        if key_word == key:
            pattern = value
            return pattern

#Сформировать ответ
def createAnswer(word, pattern, surname):
    patt = str(pattern)
    answer = patt.format(word, surname)
    return answer

#Уточнить запрос пользователя
def answerDontKnow():
    #Шаблон ответа на сообщение без ключевых слов
    patterns_ask_again = [
        'Пожалуйста, повторите запрос',
        'Пожалуйста, уточните вопрос',
        'Не могли бы сформулировать иначе?'
        ]
    
    answer_again = random.choice(patterns_ask_again)
    
    return answer_again
    

#Отправить ответ пользователю
def sendResponse(text):
    return text
