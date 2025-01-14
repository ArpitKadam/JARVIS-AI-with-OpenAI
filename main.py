import datetime
import os
import webbrowser
import openai
import pyttsx3
import speech_recognition as sr
from config import api_key

# Set the OpenAI API key
openai.api_key = api_key

def ai(prompt):
    """Handles AI interactions for standalone queries."""
    line = "*" * 73
    text = f"OpenAI response for '{prompt}'\n{line}\n\n"
    time = datetime.datetime.now().strftime("%H-%M-%S")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated to a supported model
            messages=[
                {"role": "system", "content": "You are Jarvis AI, a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and save the response content
        content = response['choices'][0]['message']['content']
        print(content)

        if not os.path.exists("Openai"):
            os.makedirs("Openai")

        with open(f"Openai/{time}.txt", "w") as f:
            text += content
            f.write(text)

    except Exception as e:
        print(f"An error occurred: {e}")

chatStr = ""  # Maintains a conversation log

def chat(text):
    """Handles continuous AI chat conversations."""
    global chatStr
    chatStr += f"Arpit : {text}\nJarvis AI : "

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated to a supported model
            messages=[
                {"role": "system", "content": "You are Jarvis AI, a helpful assistant."},
                {"role": "user", "content": chatStr}
            ]
        )

        content = response['choices'][0]['message']['content']
        say(content)
        chatStr += f"{content}\n"
        return content

    except Exception as e:
        print(f"An error occurred: {e}")
        return "I'm sorry, I couldn't process your request."

def say(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 110)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    """Listens to user input via microphone and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        print("Listening...")
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from the service.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    print("Hello, I am Jarvis AI. Nice to meet you!")
    say("Hello, I am Jarvis AI. Nice to meet you!")
    while True:
        text = takecommand()

        if not text:
            say("Sorry, I didn't catch that.")
            continue

        # Handle predefined commands
        web_sites = [
            ["youtube", "https://www.youtube.com"],
            ["github", "https://github.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["google", "https://www.google.com"]
        ]
        for site in web_sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
                break

        music_dir = [
            ["happy", "C:\\Users\\Arpit Kadam\\PycharmProjects\\JARVIS-AI-with-OpenAI\\music\\happy day.mp3"],
            ["mirzapur", "C:\\Users\\Arpit Kadam\\PycharmProjects\\JARVIS-AI-with-OpenAI\\music\\Mirzapur.mp3"],
            ["singham", "C:\\Users\\Arpit Kadam\\PycharmProjects\\JARVIS-AI-with-OpenAI\\music\\Singham.mp3"]
        ]
        for music in music_dir:
            if f"play {music[0]} music".lower() in text.lower():
                say(f"Playing {music[0]} music...")
                os.startfile(music[1])
                break

        if "time" in text.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")

        elif "whatsapp" in text.lower():
            say("Opening WhatsApp...")
            os.startfile("C:\\Users\\Arpit Kadam\\Desktop\\WhatsApp.lnk")

        elif "instagram" in text.lower():
            say("Opening Instagram...")
            os.startfile("C:\\Users\\Arpit Kadam\\Desktop\\Instagram.lnk")



        elif "ai" in text.lower():
            ai(prompt=text)

        else:
            chat(text=text)
