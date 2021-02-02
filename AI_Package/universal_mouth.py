"""universal_mouth 모듈"""
#mouth_en, mouth_kr, mouth_es : 각각 영어, 한국어, 스페인어를 지원한다

from gtts import gTTS
import os
def talk_en(words):
        tts = gTTS(text = words, lang = 'en')
        tts.save('sample_1.mp3')
        os.system('omxplayer sample_1.mp3')

def talk_kr(words):
        tts = gTTS(text = words, lang = 'ko')
        tts.save('sample_1.mp3')
        os.system('omxplayer sample_1.mp3')

def talk_es(words):
        tts = gTTS(text = words, lang = 'es')
        tts.save('sample_1.mp3')
        os.system('omxplayer sample_1.mp3')
