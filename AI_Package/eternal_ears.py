"""eternal_ears 모듈"""
import speech_recognition as sr
def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    eng = r.recognize_google(audio)
    kor = r.recognize_google(audio, language = 'ko-KR')
    esp = r.recognize_google(audio, language = 'es-ES')

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + eng + '\n or ' + kor +'\n or '+ esp)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return [eng, kor, esp]