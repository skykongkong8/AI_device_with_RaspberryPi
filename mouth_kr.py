"""mouth_kr 모듈"""

from gtts import gTTS
import os
def talk(words):
        tts = gTTS(text = words, lang = 'kr')
        tts.save('sample_1.mp3')
        os.system('omxplayer sample_1.mp3')