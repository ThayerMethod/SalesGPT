import speech_recognition as sr

def listen_and_transcribe(settings):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        transcription = recognizer.recognize_google(audio)
        print("Transcription:", transcription)
        return transcription
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Error with the API")
        return ""
