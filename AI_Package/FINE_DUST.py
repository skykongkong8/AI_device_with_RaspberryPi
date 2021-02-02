class DustData:
    def __init__(self, districtName, issueGbn):
        self.districtName = districtName
        self.issueGbn = issueGbn
def dust_list():
    import urllib.parse
    import requests
    from datetime import datetime

    servicekey = "A%2FE1M5JtX4S60k6oQ5Es6fRclxobTZqXFE3YjgWiWcqH4O6888F9UclbkgxgwEEDTfhOzL8%2BFRgmmVX0hRPAxg%3D%3D"
    decoded_key = urllib.parse.unquote(servicekey)
    #print(decoded_key)

    service_url = "http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo"
    #딕셔너리 저장할 때 사이트에 있는 파라미터 '그대로' 적을 것
    params = {
        "ServiceKey" : decoded_key,
        "pageNo" : "1",
        "numOfRows" : "10",
        "year" : "2021",
        "itemCode" : "PM10"
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


    items = 0
    data_list = []
    now = datetime.now()
    for i in range(len(body[items])):
        if body[items][i][0].tag == '{}-{}-{}'.format(now.year, str(now.month).zfill(2), str(now.day).zfill(2)):
            data_list.append(DustData(body[items][i][2].text,body[items][i][7].text))
    return data_list