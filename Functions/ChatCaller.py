import ChatFunctions

def startChat():
    greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
    dateIntent = ["date", "tell me date", "please tell me date", "what's the date"]
    timeIntent = ["time", "tell me time", "please tell me time", "what's the time"]
    musicIntent = ["play song", "start song", "play music"]
    newsIntent = ["show news", "news", "what's the news"]

    chat = True

    while chat:
        msg = input("Enter your message : ")
        msg = msg.lower()

        if msg in greetIntent:
            ChatFunctions.greet(greetIntent)
        elif msg in dateIntent:
            ChatFunctions.showDate()
        elif msg in timeIntent:
            ChatFunctions.showTime()
        elif msg in musicIntent:
            ChatFunctions.playMusic()
        elif msg in newsIntent:
            ChatFunctions.showNews()
        elif msg == "bye":
            print("Bye User")
            chat = False
        else:
            print("I don't understand")

startChat()