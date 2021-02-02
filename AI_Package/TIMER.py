"""시간을 재주는 모듈 TIMER"""
#시간을 설정하는 것은 sleep으로 HOME코드에서 구현하고, 여기서는 시간 부분을 얻어내는 자연어 처리를 해보자.
import re
def timer(master):
    p = re.compile('(\d)+')
    q = re.compile('분|초|시간|중지|정지|그만')
    m = p.search(master)
    n = q.search(master)
    try:
        t = float(m.group())
        s = n.group()
        if s == '초':
            pass
        elif s == '분':
            t*=60
        elif s == '시간':
            t*=3600
        elif s == '중지' or '정지' or '그만':
            t = -2
    except:
        t = -1
    return t     