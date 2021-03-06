"""그저께, 어제, 오늘 확진자 수를 알려주는 프로그램"""

"""#0 기타 사용 함수들"""
def check_item(my_list, word):
  result = False
  for token in my_list:
    if word in token:
      result = True
  return result

def msg_handle(string):
    isit_covid = False
    day = 0 #(0: default, 1: 오늘, 2:어제, 3:그저께)
    my_list = list(string.lower().split(' '))
    print(string)
    #0 기본 언어 : 코로나, 확진자, 몇, 명
    if check_item(my_list, '코로나'):
        if check_item(my_list, '명') or check_item(my_list, '확진자') or check_item(my_list, '수'):
            isit_covid = True
    #1 오늘
    if check_item(my_list, '오늘'):
        day = 1
    #2 어제
    elif check_item(my_list, '어제'):
        day = 2
    #3 그저께
    elif check_item(my_list, '그저께'):
        day = 3
    else:
        print('무슨 말인지 알아들을 수 없습니다!')
    return [isit_covid, day]

            

"""#1 Open API 정보를 받아오는 부분"""
import urllib.parse
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


yesterday = datetime.now()-timedelta(days=1)
past = datetime.now()-timedelta(days=4)

servicekey = "YOUR_KEY"
decoded_key = urllib.parse.unquote(servicekey)
print(decoded_key)

service_url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
#딕셔너리 저장할 때 사이트에 있는 파라미터 '그대로' 적을 것
params = {
    "ServiceKey" : decoded_key,
    "pageNo" : "1",
    "numOfRows" : "10",
    "startCreateDt" : "{}{}{}".format(str(past.year), str(past.month).zfill(2), str(past.day)),# 날짜를 잘 조절할 것! --오늘이 3일이하면 :(
    "endCreateDt" : "{}{}{}".format(str(yesterday.year), str(yesterday.month).zfill(2), str(yesterday.day)) #날짜를 if문으로 조절하기
}
resp = requests.get(service_url, params = params)
# print(resp.content)

import xml.etree.ElementTree as ET

resp = requests.get(service_url, params = params)
root = ET.fromstring(resp.content)

for element in root:
    print(element.tag, element.attrib)
    if element.tag == 'header':
        header = list(element)
    elif element.tag == 'body':
        body = list(element)

items = body[0]
decideCnt = []

for item in items:
    for item_tag in item:
        print(item_tag.tag)
        if item_tag.tag == 'decideCnt':
            decideCnt.append(int(item_tag.text))
decideCnt.reverse()
daily_patient = []
for i in range(1,len(decideCnt)):
    daily_patient.append(decideCnt[i]-decideCnt[i-1])
# print(decideCnt)
# print(daily_patient)



"""#2 터치센서를 통해 작동을 시작하고, 실제 작동하는 코드"""
import RPi.GPIO as g
from time import sleep
from ears_universal import listen
from mouth_kr import talk

g.setmode(g.BCM)
sensor = 26

g.setup(26, g.IN)
print('Press ctrl+C to quit')

try:
    while True:
        value = g.input(26)
        if value == True:
            print('sensor detected')
            what_said = listen()[1]
            if msg_handle(what_said)[0]:
                if msg_handle(what_said)[1] == 0:
                    talk('죄송해요, 오늘, 어제, 그저께에 대한 정보만 지원하고 있습니다. 더 자세한 정보는 보건복지부 홈페이지를 참조하여 주세요.')
                elif msg_handle(what_said)[1] == 1:
                    talk('오늘 코로나19 확진자 수는 {}명입니다아.'.format(daily_patient[-1]))
                elif msg_handle(what_said)[1] == 2:
                    talk('어제 코로나19 확진자 수는 {}명입니다아.'.format(daily_patient[-2]))
                elif msg_handle(what_said)[1] == 3:
                    talk('그저께 코로나19 확진자 수는 {}명입니다아.'.format(daily_patient[-3]))
            else:
                talk('죄송해요, 코로나 확진자 수 알림 기능만을 지원하고 있습니다. 다른 답변은 드릴 수가 없네요오.')
        else:
            #print('no detection')
            pass
except KeyboardInterrupt:
    g.cleanup()
    print('Goodbye.')


