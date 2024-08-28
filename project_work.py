from time import sleep
import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os
import smtplib
import pyjokes
import pyautogui
import requests as get
import pywhatkit as kit
import subprocess as sp
import pygame

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def make_request(url):
    response = get.get(url)
    return response.text

def open_cmd():
    os.system('start cmd')

def search_on_google(query):
    kit.search(query)

def play_on_youtube(video):
    kit.playonyt(video)

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')  
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def get_random_advice():
    res = get.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def find_my_ip():
    ip_address = get.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jack a Voice Assistant. Please tell me how may I help you")

def run_intro_animation():
    pygame.init()

    font_size = 20
    font = pygame.font.SysFont('monospace', font_size)

    black = (0, 0, 0)
    white = (255, 255, 255)

    def print_row(*col):
        row = ""
        for i in range(5):
            if i in col:
                row += "*"
            else:
                row += " "
        return row

    def A():
        return [print_row(1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 1, 2, 3, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4)]

    def B():
        return [print_row(0, 1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 1, 2, 3)]

    def C():
        return [print_row(1, 2, 3, 4),
                print_row(0),
                print_row(0),
                print_row(0),
                print_row(0),
                print_row(0),
                print_row(1, 2, 3, 4)]

    def D():
        return [print_row(0, 1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 1, 2, 3)]

    def E():
        return [print_row(0, 1, 2, 3, 4),
                print_row(0),
                print_row(0),
                print_row(0, 1, 2, 3),
                print_row(0),
                print_row(0),
                print_row(0, 1, 2, 3, 4)]

    def F():
        return [print_row(0, 1, 2, 3, 4),
                print_row(0),
                print_row(0),
                print_row(0, 1, 2, 3),
                print_row(0),
                print_row(0),
                print_row(0)]

    def G():
        return [print_row(1, 2, 3, 4),
                print_row(0),
                print_row(0),
                print_row(0, 3, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(1, 2, 3, 4)]

    def H():
        return [print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 1, 2, 3, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4)]

    def I():
        return [print_row(1, 2, 3),
                print_row(2),
                print_row(2),
                print_row(2),
                print_row(2),
                print_row(2),
                print_row(1, 2, 3)]

    def J():
        return [print_row(2, 3, 4),
                print_row(4),
                print_row(4),
                print_row(4),
                print_row(4),
                print_row(0, 4),
                print_row(1, 2, 3)]

    def K():
        return [print_row(0, 4),
                print_row(0, 3),
                print_row(0, 2),
                print_row(0, 1),
                print_row(0, 2),
                print_row(0, 3),
                print_row(0, 4)]

    def L():
        return [print_row(0),
                print_row(0),
                print_row(0),
                print_row(0),
                print_row(0),
                print_row(0),
                print_row(0, 1, 2, 3, 4)]

    def M():
        return [print_row(0, 4),
                print_row(0, 1, 3, 4),
                print_row(0, 2, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4)]

    def N():
        return [print_row(0, 4),
                print_row(0, 1, 4),
                print_row(0, 2, 4),
                print_row(0, 3, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4)]

    def O():
        return [print_row(1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(1, 2, 3)]

    def P():
        return [print_row(0, 1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 1, 2, 3),
                print_row(0),
                print_row(0),
                print_row(0)]

    def Q():
        return [print_row(1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 2, 4),
                print_row(1, 2, 3, 5)]

    def R():
        return [print_row(0, 1, 2, 3),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 1, 2, 3),
                print_row(0, 2),
                print_row(0, 3),
                print_row(0, 4)]

    def S():
        return [print_row(1, 2, 3, 4),
                print_row(0),
                print_row(0),
                print_row(1, 2, 3, 4),
                print_row(4),
                print_row(4),
                print_row(0, 1, 2, 3)]

    def T():
        return [print_row(0, 1, 2, 3, 4),
                print_row(2),
                print_row(2),
                print_row(2),
                print_row(2),
                print_row(2),
                print_row(2)]

    def U():
        return [print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(1, 2, 3)]

    def V():
        return [print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(1, 3),
                print_row(2)]

    def W():
        return [print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(0, 2, 4),
                print_row(0, 1, 3, 4),
                print_row(0, 4)]

    def X():
        return [print_row(0, 4),
                print_row(0, 4),
                print_row(1, 3),
                print_row(2),
                print_row(1, 3),
                print_row(0, 4),
                print_row(0, 4)]

    def Y():
        return [print_row(0, 4),
                print_row(0, 4),
                print_row(0, 4),
                print_row(1, 3),
                print_row(2),
                print_row(2),
                print_row(2)]

    def Z():
        return [print_row(0, 1, 2, 3, 4),
                print_row(4),
                print_row(3),
                print_row(2),
                print_row(1),
                print_row(0),
                print_row(0, 1, 2, 3, 4)]
    
   
    letters = {
        'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G,
        'H': H, 'I': I, 'J': J, 'K': K, 'L': L, 'M': M, 'N': N,
        'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T, 'U': U,
        'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z
    }

    def draw_letter(letter_pattern, x_offset, y_offset):
        for row_index, row in enumerate(letter_pattern):
            for col_index, char in enumerate(row):
                if char == '*':
                    label = font.render('*', True, white)
                    screen.blit(label, (x_offset + col_index * font_size, y_offset + row_index * font_size))

    def print_word(word):
        word = word.upper()  
        letter_patterns = [letters[char]() for char in word]
        x_offset = 50  
        y_offset = 100  
        for pattern in letter_patterns:
            draw_letter(pattern, x_offset, y_offset)
            pygame.display.flip()
            sleep(1)
            x_offset += (5 * font_size) + 20  

    def calculate_screen_dimensions(word):
        word_length = len(word)
        screen_width = (word_length * (5 * font_size + 20)) + 100  
        screen_height = (7 * font_size) + 200  
        return screen_width, screen_height

    
    word = "BHAGAVAN"

    screen_width, screen_height = calculate_screen_dimensions(word)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Letter Animation')

    pygame.mixer.init()
    pygame.mixer.music.load("D:\\Last Project in\\intro_music.mp3")  
    pygame.mixer.music.play(-1)  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(black)
        print_word(word)
        running = False

    pygame.mixer.music.stop()
    pygame.quit()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def open_notepad():
    os.startfile("notepad.exe")

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'intro' in query:
            run_intro_animation()
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("www.github.com")
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')
        elif 'open camera' in query:
            open_camera()
        elif "volume up" in query or "increase volume" in query:
            pyautogui.press("volumeup")
            speak('Volume increased')
        elif "volume down" in query or "decrease volume" in query:
            pyautogui.press("volumedown")
            speak('Volume decreased')
        elif "volume mute" in query or "mute the sound" in query:
            pyautogui.press("volumemute")
            speak('Volume muted')
        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')
        elif 'open notepad' in query:
            open_notepad()
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        elif "advice" in query:
            speak("Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)
        elif "who" in query or "who are you" in query:
            speak("I am Jack a Voice Assitant")
        elif "like girls" in query or "girls" in query:
            speak("Girls, girls, girls! I don't like! I avoid! But girls like me, I can't avoid!")
        elif "love you" in query or "like you" in query:
            speak("Don't have menace! Study first and take care of your family")
        elif "send a whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_command().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)
        elif "shutdown" in query or "turn off" in query:
            speak("Shutting down the system, sir")
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            speak("Restarting the system, sir")
            os.system("shutdown /r /t 1")
        elif 'exit' in query:
            speak("Goodbye, sir!")
            break
