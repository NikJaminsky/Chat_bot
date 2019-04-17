import logic
import connect_DB

print("Chat Bot")

print("Какой вопрос вас интересует?")

while True:
	message = sendMessage(input())
	
	words = separateMessage(message)
	
	key_words = selectKeyWord(words)
	
	connectToDB(db_file, db_user, db_password, localhost)
	
	if :
		pass
	else:
		answer = answerDontKnow()