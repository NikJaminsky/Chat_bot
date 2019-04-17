import logic
import connect_DB

print("Chat Bot")

print("Какой вопрос вас интересует?")

while True:
	message = logic.sendMessage(input())
	
	words = logic.separateMessage(message)
	
	key_words = logic.selectKeyWord(words)
	
	if not key_words:
		req = connect_DB.searchInDB(key_words)
		rezult = connect_DB.connectToDB(req)
		patt = logic.selectPattern(key_words)
		answer = logic.createAnswer(rezult, patt)
	else:
		answer = logic.answerDontKnow()
		
	print(logic.sendResponse(answer))
	