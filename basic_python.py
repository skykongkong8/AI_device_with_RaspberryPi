import urllib.parse
import requests
import matplotlib.pyplot as plt

servicekey = "A%2FE1M5JtX4S60k6oQ5Es6fRclxobTZqXFE3YjgWiWcqH4O6888F9UclbkgxgwEEDTfhOzL8%2BFRgmmVX0hRPAxg%3D%3D"
decoded_key = urllib.parse.unquote(servicekey)
print(decoded_key)

service_url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"

params = {
    "ServiceKey" : decoded_key,
    "pageNo" : "1",
    "numOfRows" : "10",
    "startCreateDt" : "20210116",
    "endCreateDt" : "20210125"
}
resp = requests.get(service_url, params = params)
print(resp.content)
mport xml.etree.ElementTree as ET

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
clearCnt = []
deathCnt = []
stateDt = []

for item in items:
    for item_tag in item:
        print(item_tag.tag)
        if item_tag.tag == 'decideCnt':
            decideCnt.append(int(item_tag.text))
        elif item_tag.tag == 'clearCnt':
            clearCnt.append(int(item_tag.text))
        elif item_tag.tag == 'deathCnt':
            deathCnt.append(int(item_tag.text))
        elif item_tag.tag == 'stateDt':
            stateDt.append(item_tag.text[4:])
decideCnt.reverse()
deathCnt.reverse()
clearCnt.reverse()
stateDt.reverse()
daily_cnt =[]
daily_Dt = stateDt[1:]

for i in range(1,len(decideCnt)):
    daily_cnt.append(decideCnt[i]-decideCnt[i-1])
fig,ax1 = plt.subplots()

ax1.plot(daily_Dt, daily_cnt,'r')
ax1.set_ylabel('daily_patients')
ax2 = ax1.twinx()
ax2.plot(daily_Dt, decideCnt[1:],'b')
ax2.set_ylabel('acc_patients')
plt.show()