import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')


# print(voices[1].id)
# engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning')

    elif 12 <= hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('I am Jarvis Sir. Please tell me how may I help you')


def takeCommand():
    # It takes microphone command from the user return string output

    r = sr.Recognizer()
    with sr.Microphone() as source2:

        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.2)

        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source2)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        # query = query.lower()
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('Say something again')
        return 'None'
    return query


def callFunction():
    print('function is called...')
    speak('I am Atiqur Rahman.')


def query():
    print('Listening...')
    print('Your Query...')
    print('Jack Ma, is a Chinese business magnate, investor and philanthropist. He is the co-founder and former '
          'executive chairman of Alibaba Group')


if __name__ == "__main__":
    #query()
    # speak("Atiq is a good boy")
    # speak("Allah is Almighty")
    wishMe()

    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print('Your search Query:')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open_new('youtube.com')

        elif 'open google' in query:
            webbrowser.open_new('google.com')

        elif 'open softscholar' in query:
            webbrowser.open_new('softscholar.com')

        elif 'play music' in query:
            music_dir = 'songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'function' in query:
            callFunction()
