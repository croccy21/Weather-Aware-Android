import urllib.request
import json
import time
import datetime

def main():
    now = datetime.datetime.now()
    url = 'https://api.forecast.io/forecast/94f336d8e9a37828d0cf3639f474c531/37.8267,-122.423,%s-%s-%sT%s:00:00+01:00?units=si' % (now.year,str(now.month).zfill(2),str(now.day).zfill(2),str(now.hour).zfill(2))
    response = urllib.request.urlopen(url)
    str_response = response.readall().decode('utf-8')
    obj = json.loads(str_response)
    ##print('%s-%s-%s %s:%s:%s' % (now.year,str(now.month).zfill(2),str(now.day).zfill(2),str(now.hour).zfill(2),str(now.minute).zfill(2),str(now.second).zfill(2)))
    ##for i in list(obj['currently']):
    ##    print("   " + i)
    for i in list(obj['hourly']['data']):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['time'])))
        for x in list(i):
            print("   " + x + ": " + str(i[str(x)]))
