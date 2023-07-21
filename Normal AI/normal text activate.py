#YES THIS IS AMAZING IT FINALLY WORKS AHAHHAHAHAHAHHAHAHA

import openai
import pyttsx3
import speech_recognition as sr
from googletrans import Translator

#translator
translator = Translator()

#api key for the thing
openai.api_key = "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"

#make tts engine
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
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]

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
                                                                     
""")

print("This AI was made by Isaac Sun. Finished on 06/07/23")
def main():
    while True:
        start = input('Start? (y/n): ')
        if start == "y":
            #record audio
            filename = "input.wav"
            print("Listening...")
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                source.pause_threshold = 1
                audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                with open(filename, "wb") as f:
                    f.write(audio.get_wav_data())

            #audio to text
            text = transcribe_audio_to_text(filename)
            print(f"You (english): {text}")
            # translate to japanese
            text = translator.translate(text, src='en', dest='ja')

            if text:
                print(f"You (in japanese): {text.text}")

                #generate response using ai
                response = generate_response(text.text)
                print(f"AI (japanese): {response}")
                yabadabadoo = translator.translate(response, src='ja', dest='en')
                print('AI (english): ' + yabadabadoo.text)

                #read response with tts
                speak_text(response)

        else:
            print('Exiting Program...')
            quit()
    #except Exception as e:
        #print("an error occured: {}".format(e))

if __name__ == "__main__":
    main()
