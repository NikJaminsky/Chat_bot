
#��������� ��������� ����
def sendMessage(text):
	return text

#��������� ��������� �� �����
def separateMessage(text):
	words = text.split(' ')	
	return words

#�������� �������� �����
def selectKeyWord(words):
	key_words = []
	
	for word in words:
		if word in list_key_words:
			key_words.append(word)
			
	return key_words

#������� ������ ������
def selectPattern(key_words, patterns):
	
	for pattern in patterns:
		for word in key_words:
			if word == pattern:
				
	return pattern

#������������ �����
def createAnswer(word, pattern):
	answer = pattern.format(word)	
	return answer

#�������� ������ ������������
def answerDontKnow():
	patterns_ask_again = []
	
	answer_again = random.choice(patterns_ask_again)
	
	return answer_again
	

#��������� ����� ������������	
def sendResponse(text):
	return text
