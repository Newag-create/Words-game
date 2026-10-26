import sounddevice as sd
import time
import random
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

words_by_level = {
    "łatwy": ["kot", "pies", "jabłko", "mleko", "słońce", "chmura", "noga", "ząb","deszcz"],
    "średni": ["banan", "szkoła", "przyjaciel", "okno", "żółty", "czerwony", "zielony","trawa"],
    "trudny": ["technologia", "uniwersytet", "informacja", "wymowa", "wyobraźnia","kreacja","nagły wypadek"]
}
bugs = 0
score = 0
words_num = 0
duration = 5  # sekundy nagrania
sample_rate = 44100

print('''Witaj!👋 Miło mi Cię widzieć!
Jesteś w grze "correct speak". Instrukcja obsługi:
1️⃣. Wybierasz pozim trudności - łatwy/średni/trudny,
2️⃣. Widzisz słowo i mówisz je po angielsku,
3️⃣. Czekasz na wynik.
Proste, nie?''')
time.sleep(5)
print('Zaczynamy!')
time.sleep(1)
print('Wybierz poziom trudności(łatwy/średni/trudny)')
level = input('>').strip().lower()
time.sleep(2)
while level not in words_by_level:
    print('Ten poziom nie istnieje🤔. Spróbuj ponownie')
    level = input('>')

if level == "łatwy":
    while words_num < 5 and bugs < 3:
        word = random.choice(words_by_level["łatwy"])
        print('Słowo:', word)
        time.sleep(2)
        print('🎙Mów teraz')
        recording = sd.rec(
        int(duration * sample_rate), # liczba próbek do nagrania
        samplerate=sample_rate,      # częstotliwość próbek
        channels=1,                  # 1 znaczy mono nagranie
        dtype="int16")               # typ danych dla nagranych próbek
        sd.wait()  # czekanie na zakończenie nagrywania

        wav.write("output.wav", sample_rate, recording)
        print("🔚Nagrywanie zakończone, trwa rozpoznawanie...")
        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)
        time.sleep(2)
        try:
            text = recognizer.recognize_google(audio, language="en-US").lower()
            translator = Translator()
            translated_word = translator.translate(word, src ='pl', dest="en").text.lower()
            print("Powiedziałeś/aś:", text)
            if text == translated_word:
                print('Gratulacje, to jest poprawna odpowiedź!👏')
                time.sleep(2)
                score +=1
                print('Dostajesz punkt. Twój wynik:', score)
            else:
                bugs += 1
                print('❌Źle. Poprawna odpowiedź to', word, '. Liczba błędów:', bugs)
        except sr.RequestError as e:             # - jeśli nie ma połączenia z Internetem lub API jest niedostępne
            print(f"Błąd usługi: {e}")
        words_num += 1
        if words_num == 5 or bugs == 3:
            print('''Podsumowanie!
            Zdobyte punkty:''', score, '''Gratulacje!''')
elif level == "średni":
    while words_num < 5 and bugs < 3:
        word = random.choice(words_by_level["średni"])
        print('Słowo:', word)
        time.sleep(2)
        print('🎙Mów teraz')
        recording = sd.rec(
        int(duration * sample_rate), # liczba próbek do nagrania
        samplerate=sample_rate,      # częstotliwość próbek
        channels=1,                  # 1 znaczy mono nagranie
        dtype="int16")               # typ danych dla nagranych próbek
        sd.wait()  # czekanie na zakończenie nagrywania

        wav.write("output.wav", sample_rate, recording)
        print("🔚Nagrywanie zakończone, trwa rozpoznawanie...")
        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)
        time.sleep(2)
        try:
            text = recognizer.recognize_google(audio, language="en-US").lower()
            translator = Translator()
            translated_word = translator.translate(word, src ='pl', dest="en").text.lower()
            print("Powiedziałeś/aś:", text)
            if text == translated_word:
                print('Gratulacje, to jest poprawna odpowiedź!👏')
                time.sleep(2)
                score +=1
                print('Dostajesz punkt. Twój wynik:', score)
            else:
                bugs += 1
                print('❌Źle. Poprawna odpowiedź to', word, '. Liczba błędów:', bugs)
        except sr.RequestError as e:             # - jeśli nie ma połączenia z Internetem lub API jest niedostępne
            print(f"Błąd usługi: {e}")
        words_num += 1
        if words_num == 5 or bugs == 3:
            print('''Podsumowanie!
            Zdobyte punkty:''', score, '''Gratulacje!''')
elif level == "trudny":
    while words_num < 5 and bugs < 3:
        word = random.choice(words_by_level["trudny"])
        print('Słowo:', word)
        time.sleep(2)
        print('🎙Mów teraz')
        recording = sd.rec(
         int(duration * sample_rate), # liczba próbek do nagrania
         samplerate=sample_rate,      # częstotliwość próbek
         channels=1,                  # 1 znaczy mono nagranie
         dtype="int16")               # typ danych dla nagranych próbek
        sd.wait()  # czekanie na zakończenie nagrywania

        wav.write("output.wav", sample_rate, recording)
        print("🔚Nagrywanie zakończone, trwa rozpoznawanie...")
        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)
        time.sleep(2)
        try:
            text = recognizer.recognize_google(audio, language="en-US").lower()
            translator = Translator()
            translated_word = translator.translate(word, src ='pl', dest="en").text.lower()
            print("Powiedziałeś/aś:", text)
            if text == translated_word:
                print('Gratulacje, to jest poprawna odpowiedź!👏')
                time.sleep(2)
                score +=1
                print('Dostajesz punkt. Twój wynik:', score)
            else:
                bugs += 1
                print('❌Źle. Poprawna odpowiedź to', word, '. Liczba błędów:', bugs)
        except sr.RequestError as e:             # - jeśli nie ma połączenia z Internetem lub API jest niedostępne
            print(f"Błąd usługi: {e}")
        words_num += 1
        if words_num == 5 or bugs == 3:
            print('''Podsumowanie!
            Zdobyte punkty''', score, '''Gratulacje!''')
