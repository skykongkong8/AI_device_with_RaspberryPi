"""mouth 모듈"""

from gtts import gTTS
import os
def talk(words):
        tts = gTTS(text = words, lang = 'en')
        tts.save('sample_1.mp3')
        os.system('omxplayer sample_1.mp3')

#text = 'Buenos dias! me llamo Natalia. soy tu amiga de intelligente que he hec$
#tts = gTTS(text = text, lang='es') #korean : 'ko' #espanol : 'es'
#tts.save('hello.mp3')
#os.system('omxplayer hello.mp3')
