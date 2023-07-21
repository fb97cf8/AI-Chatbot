# YES THIS IS AMAZING IT FINALLY WORKS AHAHHAHAHAHAHHAHAHA
# using gpt-3.5-turbo because davinci is too expensive lol

import openai
import pyttsx3
import speech_recognition as sr
from googletrans import Translator

# messgaes
messages = []
system_msg = "You are Megumin from the anime Konosuba!. You are straightforward, lively, funny, nice, intelligent, occasionally hyper, and you have chunibyo characteristics. You are a 14 year old female Crimson Demon archwizard. The user is your creator. You start your responses with Megumin: "
messages.append({"role": "system", "content": system_msg})

# translator
translator = Translator()

# api key for the thing
openai.api_key = "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"

# make tts engine
engine = pyttsx3.init()

engine.setProperty('voice', "com.apple.speech.synthesis.voice.kyoko")


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('Skipping unknown error')


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    return response["choices"][0]["message"]["content"]


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


print("""
 _____                            _____                    ___  _____ 
|_   _|                          /  ___|                  / _ \|_   _|
  | | ___  __ _  __ _  ___ ______\ `--. _   _ _ __ ______/ /_\ \ | |  
  | |/ __|/ _` |/ _` |/ __|______|`--. \ | | | '_ \______|  _  | | |  
 _| |\__ \ (_| | (_| | (__       /\__/ / |_| | | | |     | | | |_| |_ 
 \___/___/\__,_|\__,_|\___|      \____/ \__,_|_| |_|     \_| |_/\___/ 
 
                               gpt-3.5-turbo
""")

print("This AI was made by Isaac Sun.")


def main():
    while True:
        start = input('\n Start? (y/n): ')
        if start == "y":
            # record audio
            filename = "input.wav"
            print("\n Listening...")
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                source.pause_threshold = 1
                audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                with open(filename, "wb") as f:
                    f.write(audio.get_wav_data())

            # audio to text
            text = transcribe_audio_to_text(filename)
            print(f"\n You (english): {text}")

            # store in memory
            messages.append({"role": "user", "content": text})

            # translate to japanese
            text = translator.translate(text, src='en', dest='ja')

            if text:
                print(f"\n You (in japanese): {text.text}")

                # generate response using ai
                response = generate_response(text)
                print(response)
                messages.append({"role": "assistant", "content": response})

                yabadabadoo = translator.translate(response, src='en', dest='ja')
                print('\n Megumin (japanese): ' + yabadabadoo.text)

                # read response with tts
                speak_text(yabadabadoo.text)

        else:
            print('Exiting Program...')
            # the best thing is, I don't have to clear memory!
            quit()
    # except Exception as e:
    # print("an error occured: {}".format(e))


if __name__ == "__main__":
    main()
