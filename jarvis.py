import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            command = listener.recognize_google(audio).lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print("User Command:", command)
    except Exception as e:
        print(e)
        return ""
    return command.strip()

def run_jarvis():
    while True:
        command = take_command()
        print("Command:", command)
        if "play" in command:
            song = command.replace('play', '').strip()
            talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + current_time)
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Today's date is " + current_date)
        elif 'how are you' in command:
            talk('I am fine, how about you?')
        elif 'what is your name' in command:
            talk('I am Jarvis, What can I do for you?')
        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        else:
            talk('Please repeat your command.')

if __name__ == "__main__":
    run_jarvis()