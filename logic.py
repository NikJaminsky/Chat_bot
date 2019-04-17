
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
	
	for word in words:
		if word in list_key_words:
			key_words.append(word)
			
	return key_words

#Выбрать шаблон ответа
def selectPattern(key_words, patterns):
	
	for pattern in patterns:
		for word in key_words:
			if word == pattern:
				
	return pattern

#Сформировать ответ
def createAnswer(word, pattern):
	answer = pattern.format(word)	
	return answer

#Уточнить запрос пользователя
def answerDontKnow():
	patterns_ask_again = []
	
	answer_again = random.choice(patterns_ask_again)
	
	return answer_again
	

#Отправить ответ пользователю	
def sendResponse(text):
	return text
