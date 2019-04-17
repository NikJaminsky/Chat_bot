import tkinter as tk

class Application(tk.Frame): 
	def __init__(self, master=None):
		tk.Frame.__init__(self, master) 
		self.grid() 
		self.createWidgets()
		
	def createWidgets(self):
		self.yScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
		self.yScroll.grid(row=0, column=1, sticky=tk.N+tk.S)
		self.textChat = tk.Listbox(self, height=20, width=20, font='Arial 12', 
			yscrollcommand=self.yScroll.set, state=tk.DISABLED)
		self.textChat.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
		self.yScroll['command'] = self.textChat.yview
		
		self.sendText = tk.Text(self, height=2, width=20, pady=3, 
			padx=4, font='Arial 12', wrap=tk.WORD)
			
		self.sendButton = tk.Button(self, text='Отправить сообщение',
			command=self.sendText) 
			
		self.quitButton = tk.Button(self, text='Выход',
			command=self.quit) 	

		#self.textChat.grid()
		self.sendText.grid() 
		self.sendButton.grid() 
		self.quitButton.grid() 
	
	def sendText(self):
		text = self.sendText.get('1.0', END+'-1c')
		self.textChat.insert(END, 'Я >> {}\n'.format(text))#Добавить имя пользователя?
	
app = Application() 
app.master.title('Chat Bot') 
app.mainloop()