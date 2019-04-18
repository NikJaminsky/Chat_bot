import random

#Отправить сообщение боту
def sendMessage(text):
    return text

#Разделить сообщение на слова
def separateMessage(text):
    words = text.split(' ')	
    return words

#Выделить ключевые слова
def selectKeyWord(words):
    key_words = ['хочу']
    
    select_word = []
    
    for word in words:
        for key in key_words:
            if key == word:
                select_word.append(word)
          
    return select_word

#Выбрать шаблон ответа
def selectPattern(key_words):
    patterns = {
        'хочу': 'Вот результат, {}',
#       '': 'Предоставляю всё необходимое',
#       '': 'Расписание ',
#       '': 'Телефон филиала',
        }

    for key, value in patterns.items():
        for word in key_words:
            if word == key:
                pattern = value
                return pattern

#Сформировать ответ
def createAnswer(word, pattern):
    patt = str(pattern)
    answer = patt.format(word)
    return answer

#Уточнить запрос пользователя
def answerDontKnow():
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
