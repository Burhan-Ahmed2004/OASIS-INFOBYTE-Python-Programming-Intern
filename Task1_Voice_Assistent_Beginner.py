import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize voice
def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the internet.")
        return ""

# Main loop
speak("Hi! I am your voice assistant.")
while True:
    command = get_command()

    if "hello" in command:
        speak("Hello! How can I help you today?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + now)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak("Today's date is " + today)

    elif "search" in command:
        speak("What should I search for?")
        search_query = get_command()
        if search_query:
            speak("Searching for " + search_query)
            webbrowser.open("https://www.google.com/search?q=" + search_query)

    elif "stop" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        break

    else:
        speak("Sorry, I didn't understand. Please try again.")
