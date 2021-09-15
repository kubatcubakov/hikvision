from datetime import datetime,timedelta
import time
import requests
import xmltodict

def Dvr_request():

    today = datetime.today()
    today1 = datetime.today() - timedelta(minutes=1)
    d0 = today1.strftime("%Y-%m-%dT%H:%M:%SZ")
    d1 = today.strftime("%Y-%m-%dT%H:%M:%SZ")
    UserName = '';
    IpAddress = '';
    StartDateTime = ''

    url = 'http://192.168.110.51/ISAPI/ContentMgmt/logSearch'
    body = '<?xml version="1.0" encoding="utf-8"?><CMSearchDescription><searchID>C9827E2B-D5B0-0001-9EBE-9863157012FC</searchID><metaId>log.hikvision.com/Operation</metaId><timeSpanList><timeSpan><startTime>' + d0 + '</startTime><endTime>' + d1 + '</endTime></timeSpan></timeSpanList><maxResults>40</maxResults><searchResultPostion>1960</searchResultPostion></CMSearchDescription>'
    Body = '"1.0" encoding="utf-8"?><CMSearchDescription><searchID>C98283D1-90B0-0001-A71D-13FD4B805C10</searchID><metaId>log.hikvision.com/Operation</metaId><timeSpanList><timeSpan><startTime>' + d0 + '</startTime><endTime>' + d1 + '</endTime></timeSpan></timeSpanList><maxResults>40</maxResults></CMSearchDescription>'
    headers = {"Authorization": "Basic YWRtaW46MGY1NmZmMmZlYg=="}
    value = 'Basic YWRtaW46MGY1NmZmMmZlYg=='

    response = requests.post(url, headers=headers, data=Body)
    dict_data = xmltodict.parse(response.content)

    num = int(dict_data["CMSearchResult"]["numOfMatches"])

    f = open('out.log', 'r')
    line = f.read()
    f.close()

    if num > 0:
        StartDateTime = (
        dict_data["CMSearchResult"]["matchList"]["searchMatchItem"][num - 1]["logDescriptor"]["StartDateTime"])

    if num > 0 and StartDateTime != line:
        UserName = (dict_data["CMSearchResult"]["matchList"]["searchMatchItem"][num - 1]["logDescriptor"]["userName"])
        IpAddress = (dict_data["CMSearchResult"]["matchList"]["searchMatchItem"][num - 1]["logDescriptor"]["ipAddress"])
        StartDateTime1 = (dict_data["CMSearchResult"]["matchList"]["searchMatchItem"][num - 1]["logDescriptor"]["StartDateTime"])
        my_file = open("out.log", "w")
        my_file.write(StartDateTime1)
        my_file.close()
    else:
        UserName = '';
        IpAddress = '';
        StartDateTime = ''
    return f"{UserName},{IpAddress},{StartDateTime}"

def send_msg(text):
        token = "1920771375:AAF8sO6dYoeKdh4pADpObqoya9LdPJbcB54"
        chat_id = "852807966"
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
        results = requests.get(url_req)


if __name__ == '__main__':
    while True:
        try:
            a=Dvr_request()
            if a!=',,':
                send_msg(a)
                #print(a)
        except: continue
        time.sleep(10)
