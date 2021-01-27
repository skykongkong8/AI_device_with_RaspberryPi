from ears_universal import listen
from mouth_kr import talk
import csv

def find_highest_temp(year, direction):
    f = open('kma_climate_data.csv','r') #encoding = 'cp949'-한글일때!
    data = csv.reader(f)
    header = next(data)
    max_temp = -999
    if direction == '이후':
        for row in data:
            try:
                if int(row[0][:4]) <= year:
                    max_temp = max(max_temp, float(row[-1]))
            except:
                pass  

    elif direction == '이전':
        for row in data:
            try:
                 if int(row[0][:4]) > year:
                    max_temp = max(max_temp, float(row[-1]))
            except:
                pass
    return max_temp

def find_lowest_temp(year, direction):
    f = open('kma_climate_data.csv','r') #encoding = 'cp949'-한글일때!
    data = csv.reader(f)
    header = next(data)
    min_temp = 999
    if direction == '이후':
        for row in data:
            try:
                if int(row[0][:4]) <= year:
                    min_temp = min(min_temp, float(row[-2]))
            except:
                pass  

    elif direction == '이전':
        for row in data:
            try:
                 if int(row[0][:4]) > year:
                    min_temp = min(min_temp, float(row[-2]))
            except:
                pass
    return min_temp

"""실행 부분"""
msg = listen()[1]
print('혹시 안되면 :"XXXX년 이후/이전 서울의 최고/최저 기온은?" 이라고 말하세요')

try:
    year = int(msg[:4])
    direction = msg[6:8]
    min_max = msg[13:15]
    if min_max == '최고':
        talk('{0}년 {1} 서울의 {2} 기온은 {3} 도 입니다아.'.format(year, direction, min_max, find_highest_temp(year, direction)))

    elif min_max == '최저':
        talk('{0}년 {1} 서울의 {2} 기온은 {3} 도 입니다아.'.format(year, direction, min_max, find_lowest_temp(year, direction)))
    else:
        talk('죄송해요, 최고/최저를 잘 모르겠습니다.')
except:
    print('잘못된 입력입니다!')