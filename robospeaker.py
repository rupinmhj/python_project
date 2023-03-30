import pyttsx3
if __name__=='__main__':
    while True:
        print("#### Welcome to robospeaker ####")
        text=input("Enter the text you want to convert in speech: ")
        if text=='quit':
            break
        engine=pyttsx3.init() # initialize the pyttsx3 engine
        engine.say(text) #convert text to speech
        engine.runAndWait() # tells 'pyttsx3' engine to speak the text and wait 
                            # until the speech is complete