
#Отправить сообщение боту
def sendMessage(text):
	return text

#Разделить сообщение на слова
def separateMessage(text):
	words = text.split(' ')	
	return words

#Выделить ключевые слова
def selectKeyWord(words):
	key_words = []
	
	select_word = []
	
	for word in words:
		if word in key_words:
			select_word.append(word)
			
	return select_word

#Выбрать шаблон ответа
def selectPattern(key_words):
	patterns = {
		'': 'Вот результат',
		'': 'Предоставляю всё необходимое',
		'': 'Расписание ',
		'': 'Телефон филиала',
		}

	for key, value in patterns:
		for word in key_words:
			if word == key:
				pattern = value
				
	return pattern

#Сформировать ответ
def createAnswer(word, pattern):
	answer = pattern.format(word)	
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
