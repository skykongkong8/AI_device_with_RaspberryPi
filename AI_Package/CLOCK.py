"""현재 시각을 알려주는 함수 clock"""
from datetime import datetime
def clock():
    now = datetime.now()
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    return [month, day, hour, minute]