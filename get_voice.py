import pyttsx3 

engine = pyttsx3.init()
name = input("Please Enter Your First Name in lowCase : ")
if name == 'yahya':
    name = 'yoyo'
elif name == 'yousef':
    name = 'jo'
elif name == 'omar':
    name = 'mora'
engine.say(f"hello {name}")
engine.runAndWait()
