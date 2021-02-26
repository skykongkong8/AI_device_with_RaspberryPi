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
    if check_item(my_list, '날씨'):
#         weather = True
        return 0
    elif check_item(my_list, '코로나'):
#         COVID = True
        return 1
    elif check_item(my_list, '몇'):
        if check_item(my_list, '시') or check_item(my_list, '시야') or check_item(my_list, '분') or check_item(my_list, '분이야'):
#             clock = True
            return 2
    elif check_item(my_list, '랩'):
        if check_item(my_list, '해') or check_item(my_list, '줘') or check_item(my_list, '해줘'):
#             Rap = True
            return 3
    elif check_item(my_list, '타이머'):
#         Timer = True
        return 4
    elif check_item(my_list, '재미있는') or check_item(my_list, '재밌는') or check_item(my_list, '웃긴') or check_item(my_list,'재미'):
        if check_item(my_list, '이야기') or check_item(my_list, '얘기') or check_item(my_list, '농담') or check_item(my_list, '말'):
#             Jokes = True
            return 5
    elif (check_item(my_list, '미세') and check_item(my_list, '먼지')) or check_item(my_list, '미세먼지'):
        return 6
    elif check_item(my_list, '할') and (check_item(my_list, '있어') or check_item(my_list, '알아') or check_item(my_list, '뭐')):
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
                talk('죄송해요, 오늘, 어제, 그저께에 대한 정보만 지원하고 있습니다. 더 자세한 정보는 보건복지부 홈페이지를 참조하여 주세요.')
            elif msg_handle(what_said)[1] == 1:
                talk('오늘 코로나19 확진자 수는 {}명입니다아.'.format(Daily_Patient()[-1]))
            elif msg_handle(what_said)[1] == 2:
                talk('어제 코로나19 확진자 수는 {}명입니다아.'.format(Daily_Patient()[-2]))
            elif msg_handle(what_said)[1] == 3:
                talk('그저께 코로나19 확진자 수는 {}명입니다아.'.format(Daily_Patient()[-3]))
        else:
            talk('죄송해요, 코로나 확진자 수 알림 기능만을 지원하고 있습니다. 다른 답변은 드릴 수가 없네요오.')

    except KeyboardInterrupt:
        print('Goodbye.')

def timer_talk(string):
    from TIMER import timer
    T = timer(master)
    if T >=0:
        talk('타이머가 설정되었습니다. 시간이 끝나면 세 번 알려드려요오!')
        sleep(T)
        for _ in range(3):
            talk('타이머가 끝났습니다!')
            sleep(0.5)
    elif T == -1:
        talk('죄송해요, 타이머 설정 시간을 잘 이해하지 못했습니다아.')
    elif T == -2:
        talk('죄송해요, 타이머를 끄는 설정은 아직 준비되어 있지 않습니다. 다음에는 꼭 도움이 되어드리도록 노력하겠습니다.')

def dust_talk(string):
    from FINE_DUST import DustData
    from FINE_DUST import dust_list
    try:
        talk('기상청 실시간 공개 데이터 확인 결과, 현재')
        for i in range(len(dust_list())):
            talk('{}지역에 {} 발령'.format(dust_list()[i].districtName, dust_list()[i].issueGbn))
        talk('발령 중입니다.')
    except:
        talk('오늘 미세먼지 경보 발령된 지역이 없습니다아.')


"""master_handle의 번호에 맞는 모드를 설정하여주는 함수 mode_selection"""
def mode_selection(mode_number, master):
    if mode_number == -1:
        talk('죄송해요, 무슨 말인지 잘 알아듣지 못했어요오')
        
    elif mode_number == 0:
        import weather #날씨 함수 작성
        talk('죄송합니다, 아직 서비스 준비중입니다!')
        
    elif mode_number == 1:
        covid(master)
        
    elif mode_number == 2:
        from CLOCK import clock
        tik = clock()
        talk('지금은 {}월 {}일 {}시 {}분 입니다아'.format(tik[0], tik[1], tik[2], tik[3]))
        
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
        talk('저는 당신을 도와주는 인공지능 스피커입니다. 시계, 타이머, 실시간 코로나 확진자, 미세먼지 경보 발령 현황 등에 대하여 말씀드릴 수 있습니다. 간단한 농담이나 랩도 할 줄 안답니다. 날씨 기능은 업데이트 준비중이에요.')
        
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