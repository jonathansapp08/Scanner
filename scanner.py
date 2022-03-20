import speech_recognition as sr
import alert


def read_words(file):
    alert_file = open(file, 'r')
    words = alert_file.read().split('\n')
    return words

def record_audio(r):
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)

        with open("output.wav", "wb") as file:
            file.write(audio_data.get_wav_data())

    return audio_data

def recognize_speech(r, audio_data):
    try:
        text = r.recognize_google(audio_data)
        print(text)
        return text
    except:
        pass

def alert_check(text, alert_words):
    if any(word in text for word in alert_words):
            print("Alert detected")
            alert.send_text(email="EMAIL@gmail.com", pas="PASSWORD", sms_gateway='PHONE_NUMBER@CARRIER')


if __name__ == "__main__":
    r = sr.Recognizer()
    alert_words = read_words('alert_words.txt')

    while True:
        audio_data = record_audio(r)
        text = recognize_speech(r, audio_data)
        if text is not None:
            alert_check(text, alert_words)
