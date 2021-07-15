# AI_device_with_RaspberryPi
## Codes needed for making a tangible artificial intelligence speaker
* #1 with Google assistant
* #2 on my own - data with Open API from data.go.kr
> **Hardware configuration** 
> * RaspberryPi 3B+
> * USB Speaker
> * Microphone with SoundCard 2.0
> * 3D modeled body represented [here](https://skykongkong8.wixsite.com/skykongkong8/post/tangible-%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5-%EC%8A%A4%ED%94%BC%EC%BB%A4-2)
## Brief Description
### EARS.py
Hear user's voice and return it into list containing strings, with Korean, English, Spanish.
### MOUTH.py
Make an mp3 file of the pronounced sound of predefined string, and play it with os / pygame
* if using USB speaker, you **SHOULD** use pygame since os does not support USB speaker output anymore.
### TOUCH_HOME.py
Activate listening mode by touching the sensor, and operate super simple NLP algorithm to understand what function is being asked.
Set specific mode for implementing the required function and return with valid value.


## Google Assistant
### Provides basic functions that is almost identical to Google Home Mini
> functions that have issues regarding license problems are excluded from this project.

## On my own
### Provides following functions with Korean, English, and Espanol(T.B.A.)
* LIVE COVID19 patient information with syntax: today, yesterday, and day before yesterday
* Daily fine dust alarm from weather forecast
* Clock
* Timer
* Random rap verses
* Random jokes
* Weather forecast (T.B.A.)

#### TTS STT algorithm with: SpeechRecognition, gTTS
