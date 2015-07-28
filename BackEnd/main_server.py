import parse
import re
data = "www.server.co.uk/?no=1&condid=1&start=09:00&end=10:00&offset=5&no=2&condid=2&start=10:00&end=11:00&offset=-10"
pattern = "no=\d+&condid=\d+&start=\d\d:\d\d&end=\d\d:\d\d&offset=-*\d+"
conditions = re.findall(pattern, data, re.IGNORECASE)
conditionsList = []
for i in conditions:
    tempDictionary = {}
    params = i.split("&")
    for index in range(len(params)):
        params[index] = params[index].split("=")[1]
    tempDictionary['number'] = params[0]
    tempDictionary['condid'] = params[1]
    tempDictionary['start'] = params[2]
    tempDictionary['end'] = params[3]
    tempDictionary['offset'] = params[4]
    conditionsList.append(tempDictionary)
for condition in conditionsList:
    print(condition['number'])
    print(condition['condid'])
    print(condition['start'])
    print(condition['end'])
    print(condition['offset'])
    print()
parse.main()
for i in list(obj['hourly']['data']):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['time'])))
    for x in list(i):
        print("   " + x + ": " + str(i[str(x)]))
