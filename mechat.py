import re
from tkinter import *
import tkinter.font as font
root = Tk()

def chat():
    chat = "Me:"+ e.get()
    text.insert(END,"\n" + chat)
    match = re.search(r'([\d\-+*\\]+)', e.get())
    
    if(e.get().lower()=='hi'or e.get().lower()=='hello' or e.get().lower()=='hey'):
        text.insert(END, "\n" + "Bot: Hey, how may I help you...")
    elif(e.get().lower()=='how are you?'):
        text.insert(END, "\n" + "Bot: I'm fine and you?")
    elif (e.get().lower() == 'i\'m also fine'):
        text.insert(END, "\n" + "Bot: Great!:)")
    elif (e.get().lower() == "what is your name" or e.get().lower() == "Who are you?"):
        text.insert(END, "\n" + "Bot: I am Jack Sparrow, your personal assistant.")
    elif (e.get().lower() == "tell me a joke"):
        text.insert(END, "\n" + "Bot: Do you have a mirror?...")
    elif (e.get().lower() == "tell me another joke"):
        text.insert(END, "\n" + "Bot: Knock-knock!")
    elif (e.get().lower() == "who's there"):
        text.insert(END, "\n" + "Bot: Your assisgnment deadlines...looool")
    elif (e.get().lower() == "are you a real person?"):
        text.insert(END, "\n" + "Bot: What th dude. I'm a robot developed by Greg...\n HUMANS!(sigh)")
    elif (e.get().lower() == "not funny"):
        text.insert(END, "\n" + "Bot: Lol...I'll try harder next time")
    elif match:
        expr = match[1]
        text.insert(END, "\n" + f"Bot: The answer is {eval(expr)}")
    else:
        text.insert(END, "\n" + "Bot: I don't understand.")

    
    
text = Text(root,bg='white', fg='red')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=90)
chat = Button(root,text='Chat',bg='black', fg='yellow', width=30,command=chat).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('MeChat')


root.mainloop()
