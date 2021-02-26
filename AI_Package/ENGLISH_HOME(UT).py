from USB_mouth import talk_kr as talk
from USB_mouth import talk_en
from eternal_ears import listen
from time import sleep

"""기본 생각 : 사용자의 말을 변수에 저장, 어떤 말인지에 따라 그에 맞는 답변을 주자."""
# master = listen()[1] #사용자의 말을 string으로 저장

"""리스트에 특정 글자가 있는지 없는지 판단하는 함수 check_item"""
def check_item(my_list, word):
  result = False 
  for token in my_list:
    if word in token:
      result = True
  return result

#기본 기능: 날씨, 코로나 확진자, 시계, 랩 해줘, 타이머(?), 재미있는 이야기 해줘:1,2,3,  ?????

"""기본적으로 어떤 기능인지만 판별하는 함수 master_handle"""
def master_handle(string):
# 1 기본 기능들 중 무엇을 실행할지, Boolean으로 판단하자-변수 초기화
#     weather = False #0
#     COVID = False #1
#     clock = False #2
#     Rap = False #3
#     Timer = False #4
#     Jokes = False #5
#     micro_dust = False #6
    
    #2 string으로 사용자의 말을 파라미터로 받고, 띄어쓰기 단위로 나눈다.
    my_list = list(string.lower().split(' '))
    
    #3 각각의 상황에 따라 간단한 예상 NLP처리를 해보고, 숫자로 모드를 바꿔보자
    if check_item(my_list, 'weather'):
#         weather = True
        return 0
    elif check_item(my_list, 'COVID') or check_item(my_list, 'corona') or check_item(my_list, 'virus'):
#         COVID = True
        return 1
    elif check_item(my_list, 'time'):
        if check_item(my_list, 'what'):
#             clock = True
            return 2
    elif check_item(my_list, 'rap'):
        if check_item(my_list, 'try') or check_item(my_list, 'give') or check_item(my_list, 'show'):
#             Rap = True
            return 3
    elif check_item(my_list, 'timer'):
#         Timer = True
        return 4
    elif check_item(my_list, 'funny') or check_item(my_list, 'fun') or check_item(my_list, 'joke') or check_item(my_list,'jokes'):
        if check_item(my_list, 'tell') or check_item(my_list, 'say') or check_item(my_list, 'know'):
#             Jokes = True
            return 5
    elif (check_item(my_list, 'fine') or check_item(my_list, 'dust')) or check_item(my_list, 'finedust'):
        return 6
    elif check_item(my_list, 'able') or (check_item(my_list, 'can') or check_item(my_list, 'possible') or check_item(my_list, 'what can you')):
        return 1000
    else:
        return -1


def covid(string):
    import COVID
    from COVID import msg_handle
    from COVID import check_item
    from COVID import Daily_Patient
    print('Press ctrl+C to quit')
    try:
        what_said = string
        if msg_handle(what_said)[0]:
            if msg_handle(what_said)[1] == 0:
                talk_en('Sorry, I only know about today, yesterday, and day before yesterday. Search internet for more detailed information.')
            elif msg_handle(what_said)[1] == 1:
                talk_en('Reported COVID patient number for today is {}.'.format(Daily_Patient()[-1]))
            elif msg_handle(what_said)[1] == 2:
                talk_en('Reported COVID patient number for yesterday is {}.'.format(Daily_Patient()[-2]))
            elif msg_handle(what_said)[1] == 3:
                talk_en('Reported COVID patient number for day before yesterday is {}.'.format(Daily_Patient()[-3]))
        else:
            talk_en('Sorry, I only know about COVID patient number, please search internet for more information.')

    except KeyboardInterrupt:
        print('Goodbye.')

def timer_talk(string):
    from TIMER_en import timer
    T = timer(string)
    if T >=0:
        talk_en('Your timer has set. I will let you know three times when it is over.')
        sleep(T)
        for _ in range(3):
            talk("Times up!")
            sleep(0.5)
    elif T == -1:
        talk('Sorry, could you tell me the exact time range once again?')
    elif T == -2:
        talk('Sorry we are currently on the preparing level for that service. I will strive to be a better assistant for you next time.')

#미세먼지는 지역이름 때문에 영어 변환이 불가?
def dust_talk(string):
    from FINE_DUST import DustData
    from FINE_DUST import dust_list
    try:
        talk('According to National Weather Service,')
        for i in range(len(dust_list())):
            talk('{}지역에 {} 발령'.format(dust_list()[i].districtName, dust_list()[i].issueGbn))
        talk('발령 중입니다.')
    except:
        talk('오늘 미세먼지 경보 발령된 지역이 없습니다아.')




"""master_handle의 번호에 맞는 모드를 설정하여주는 함수 mode_selection"""
def mode_selection(mode_number, master):
    if mode_number == -1:
        talk("Sorry, I could not understand your words")
        
    elif mode_number == 0:
        import weather #날씨 함수 작성
        talk("Sorry, the service haven't prepared yet")
        
    elif mode_number == 1:
        covid(master)
        
    elif mode_number == 2:
        from CLOCK import clock
        tik = clock()
        calender = {
        1 : 'January',
        2:'Feburary',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
        }
        talk('It is {} {}, {} and {}'.format(calender[tik[0]], tik[1], tik[2], tik[3]))
        
    elif mode_number == 3:
        from RAP import rap
        verse = rap()
        if verse[0] == 1 or verse[0] == 2:
            for i in range(len(verse[1])):
                talk(verse[1][i])
                sleep(0.5)
        elif verse[0] == 3:
            talk_en(verse[1][0])
            
    elif mode_number == 4:
        timer_talk(master)
        
    elif mode_number == 5:
        from JOKE import joke
        haha = joke()
        for i in range(len(haha)):
            talk(haha[i])
            sleep(1)
            
    elif mode_number == 6:
        dust_talk(master)
    
    elif mode_number == 1000:
        talk('Hi, my name is Amy, your personal A I assistant. You can ask for the followings: clock, timer, covid patient, jokes, rap. Pleased to meet you and have a wonderful day!')
        
"""작동 코드"""
import RPi.GPIO as g

g.setmode(g.BCM)
sensor = 26
g.setup(sensor, g.IN)
print('Press ctrl+C to abort')

try:
    while True:
        value = g.input(sensor)
        if value == True:
            master = listen()[1]
            print('Sensor Detected')
            MODE = master_handle(master)
            mode_selection(MODE, master)
        else:
            pass
except KeyboardInterrupt:
    g.cleanup()
    print('Goodbye.')
finally:
    g.cleanup()