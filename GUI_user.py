import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import logic
import connect_DB

class Form(QWidget):       
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        
        #Чат
        self.te_chat = QTextEdit(self)
        self.te_chat.setReadOnly(True)
        self.te_chat.setFont(QFont("Arial",14))
        self.te_chat.setAlignment(Qt.AlignLeft)
        self.te_chat.resize(230, 300)  
        grid.addWidget(self.te_chat, 1, 0, 1, 3)       
        
        #Поле для ввода текста 
        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Arial",14))
        self.input_field.setAlignment(Qt.AlignLeft)
        self.input_field.resize(230, 30)  
        grid.addWidget(self.input_field, 2, 0, 1, 3) 
        #input_text = input_field.text()        
        
        #Кнопка "Отправить сообщение"
        btn_send_message = QPushButton('Отправить сообщение', self)
        btn_send_message.clicked.connect(self.allOperation)
        btn_send_message.resize(btn_send_message.sizeHint())
        grid.addWidget(btn_send_message, 3, 0, 1, 1)
        
        #Кнопка "Закрыть чат"
        btn_close = QPushButton('Закрыть чат', self)
        btn_close.clicked.connect(QCoreApplication.instance().quit)
        btn_close.resize(btn_close.sizeHint())
        grid.addWidget(btn_close, 3, 2, 1, 1)
        
        
        self.setLayout(grid)
        self.resize(250, 500)
        self.center()       
        self.setWindowTitle('Chat Bot')
        #self.setWindowIcon(QIcon('icon.png'))        
        self.show()
        
    #Разместить окно по центру экрана
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())  
    
    #Обработать запрос пользователя
    def allOperation(self):
        user = "Me>> " + self.input_field.text()
        self.te_chat.append(user)
        message = logic.sendMessage(self.input_field.text())

        words = logic.separateMessage(message)

        key_words = logic.selectKeyWord(words)
        
        if key_words != []:
            req = connect_DB.searchInDB(key_words)
            rezult = connect_DB.connectToDB(req)
            patt = logic.selectPattern(key_words)
            answer = logic.createAnswer(rezult, patt)
        else:
            answer = logic.answerDontKnow()
        
        bot = "Bot>> " + logic.sendResponse(answer)
        self.te_chat.append(bot)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    sys.exit(app.exec_())