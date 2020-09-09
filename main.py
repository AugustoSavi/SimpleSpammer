import pyautogui, time, threading
from tkinter import *

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.buttons()
        self.inputs()
        root.mainloop()

    def tela(self):
        self.root.title('Simple Spammer')
        self.root.geometry('450x200')
        self.root.resizable(False,False)
    
    def frame(self):
        self.frame = Frame(self.root)
        self.frame.place(relx = 0 , rely = 0,relwidth = 1, relheight = 1)

    def buttons(self):
        #Bottão Clear 
        self.btnClear = Button(self.frame, text = 'F9- Clear', command = self.clear)
        self.btnClear.place ( relx = 0.76, rely = 0.1, width = 100, height = 50)
        #self.btnClear.bind('<Key>',print('teste')

        
        #Bottão Start 
        self.btnStart = Button(self.frame, text = 'F10- Start', command = self.start)
        self.btnStart.place ( relx = 0.76, rely = 0.39, width = 100, height = 50)
        
        #Bottão Stop 
        self.btnStop = Button(self.frame, text = 'F11- Stop')
        self.btnStop.place ( relx = 0.76, rely = 0.68, width = 100, height = 50)
    
    def inputs(self):

        self.labelText = Label(self.frame, text = 'Text:')
        self.labelText.place(relx = 0.01, rely = 0)

        self.textBox = Text(self.frame,height = 10 , width = 40)
        self.textBox.place(relx = 0.02, rely = 0.1)

    def clear(self):
        self.textBox.delete('1.0', END)
         
    def start(self):
        startThreading = threading.Thread(target=self.SpamLoop)
        startThreading.start()
        
    def SpamLoop(self):
        stringTextBox = self.textBox.get('1.0', END)
        
        splitStringTextBox = stringTextBox.splitlines()

        time.sleep(5.0)
        
        for word in splitStringTextBox:
            time.sleep(2.0)
            pyautogui.typewrite(word)
            pyautogui.press('enter')

    def key(event):
        print(event.char)

Application()
#f = open("file.txt",'r') 