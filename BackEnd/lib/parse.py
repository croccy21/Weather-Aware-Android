import urllib.request
import json
import re
import time
import datetime

def parseWeather(year,month,day,hour,minute,second,latitude,longitude):
    now = datetime.datetime.now()
    #url = 'https://api.forecast.io/forecast/94f336d8e9a37828d0cf3639f474c531/latitude,longitude,%s-%s-%sT%s:%s:%s+01:00?units=si&exclude=currently,minutely,daily,alerts,flags' % (str(year),str(month).zfill(2),str(day).zfill(2),str(hour).zfill(2),str(minute).zfill(2),str(second).zfill(2))
    #response = urllib.request.urlopen(url)
    #str_response = response.readall().decode('utf-8')
    file = open("sample data.txt")
    str_response = file.read()
    file.close()
    obj = json.loads(str_response)
    ##print('%s-%s-%s %s:%s:%s' % (now.year,str(now.month).zfill(2),str(now.day).zfill(2),str(now.hour).zfill(2),str(now.minute).zfill(2),str(now.second).zfill(2)))
    ##for i in list(obj['currently']):
    ##    print("   " + i)
    returnList = []
    for i in list(obj['hourly']['data']):
        tempDictionary = {}
        for x in list(i):
            if x != "time":
                tempDictionary[x] = str(i[str(x)])
            else:
                tempDictionary["unixtime"] = str(i[str(x)])
                tempDictionary["time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[str(x)]))
        returnList.append(tempDictionary)
    return returnList

def parseURL(data):
    pattern = "no\d+=\d+&condid\d+=\d+&start\d+=\d+&end\d+=\d+"
    conditions = re.findall(pattern, data, re.IGNORECASE)
    conditionsList = []
    # 1 = 0 = Wind
    # 2 = 1 = Snow
    # 3 = 2 = Rain
    # 4 = 3 = Visibility
    # 5 = 4 = Precipitation
    for i in conditions:
        tempDictionary = {}
        params = i.split("&")
        for index in range(len(params)):
            params[index] = params[index].split("=")[1]
        tempDictionary['number'] = params[0]
        tempDictionary['condid'] = params[1]
        tempDictionary['start'] = params[2]
        tempDictionary['end'] = params[3]
        conditionsList.append(tempDictionary)
    return conditions, conditionsList
