class WeatherData:
    def __init__(self,tm, minTa, maxTa):
        self.tm = tm
        self.minTa = minTa
        self.maxTa = maxTa

def weather():
    import urllib.parse
    import requests
    from datetime import datetime, timedelta

    servicekey = "A%2FE1M5JtX4S60k6oQ5Es6fRclxobTZqXFE3YjgWiWcqH4O6888F9UclbkgxgwEEDTfhOzL8%2BFRgmmVX0hRPAxg%3D%3D"
    decoded_key = urllib.parse.unquote(servicekey)
    #print(decoded_key)
    
    yesterday = datetime.now()-timedelta(days=1)
    past = datetime.now()-timedelta(days=4)

    service_url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
    #딕셔너리 저장할 때 사이트에 있는 파라미터 '그대로' 적을 것
    params = {
        "ServiceKey" : decoded_key,
        "pageNo" : "1",
        "dataCd" : "ASOS",
        "dateCd" : "DAY",
        "StartDt" : "{}{}{}".format(str(past.year), str(past.month).zfill(2), str(past.day).zfill(2)),
        "endDr" : "{}{}{}".format(str(yesterday.year), str(yesterday.month).zfill(2), str(yesterday.day).zfill(2)),
        "stnlds" : "108"
    }
    resp = requests.get(service_url, params = params)
    #print(resp.content)

    import xml.etree.ElementTree as ET

    resp = requests.get(service_url, params = params)
    root = ET.fromstring(resp.content)

    for element in root:
        print(element.tag, element.attrib)
        if element.tag == 'header':
            header = list(element)
        elif element.tag == 'body':
            body = list(element)


    items = 1
    data_list = []
    for i in range(len(body[items])):
        data_list.append(WeatherData(body[items][i][2].text,body[items][i][4].text,body[items][i][6].text))
    return data_list

print(weather()[0].minTa)