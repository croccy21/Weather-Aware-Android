import parse
import re
data = "www.server.co.uk/?no=1&condid=1&start=09&end=10&no=2&condid=3&start=10&end=11"
pattern = "no=\d+&condid=\d+&start=\d\d&end=\d\d"
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
    conditionsList.append(tempDictionary)
for condition in conditionsList:
    print(condition['number'])
    print(condition['condid'])
    print(condition['start'])
    print(condition['end'])
    print()
weather = parse.main("2015","07","28","12","06","00")
statuses = {}
for weatherDay in weather:
    #for weatherType in weatherDay:
        #print(weatherType + ': ' + str(weatherDay[weatherType]))
##    print(weatherDay['time'])
##    print(weatherDay['unixtime'])
##    print(weatherDay['precipProbability'] + '%')
##    print(weatherDay['visibility'] + 'km')
##    print(weatherDay['windSpeed'] + ' m/s')
##    print(weatherDay['precipIntensity'] + ' inches')
##    if float(weatherDay['precipIntensity']) != 0:
##        print(weatherDay['precipType'])
##    print()
    hourStatus = []
    status = False
    if float(weatherDay['precipIntensity']) != 0 and (weatherDay['precipType'] == 'rain' or weatherDay['precipType'] == 'hail'):
        if float(weatherDay['precipIntensity']) >= 10.16:
            if float(weatherDay['precipProbability']) >= 40:
                status = True
            else:
                status = False
        elif float(weatherDay['precipIntensity']) >= 2.54:
            if float(weatherDay['precipProbability']) >= 50:
                status = True
            else:
                status = False
        elif float(weatherDay['precipIntensity']) >= 0.4318:
            if float(weatherDay['precipProbability']) >= 60:
                status = True
            else:
                status = False
        elif float(weatherDay['precipIntensity']) >= 0.0508:
            if float(weatherDay['precipProbability']) >= 70:
                status = True
            else:
                status = False
    else:
        status = False
    hourStatus.append(status)
    #####
    status = False
    if float(weatherDay['precipIntensity']) != 0 and (weatherDay['precipType'] == 'snow' or weatherDay['precipType'] == 'sleet'):
        if float(weatherDay['precipIntensity']) >= 10.16:
            if float(weatherDay['precipProbability']) >= 30:
                status = True
            else:
                status = False
        elif float(weatherDay['precipIntensity']) >= 2.54:
            if float(weatherDay['precipProbability']) >= 40:
                status = True
            else:
                status = False
        elif float(weatherDay['precipIntensity']) >= 0.4318:
            if float(weatherDay['precipProbability']) >= 50:
                status = True
            else:
                status = False
        elif float(weatherDay['precipIntensity']) >= 0.0508:
            if float(weatherDay['precipProbability']) >= 60:
                status = True
            else:
                status = False
    else:
        status = False
    hourStatus.append(status)
    #####
    status = False
    if float(weatherDay['visibility']) <= 2:
        status = True
    else:
        status = False
    hourStatus.append(status)
    #####
    status = False
    if float(weatherDay['windSpeed']) >= 13.4112:
        status = True
    else:
        status = False  
    hourStatus.append(status)
    #statuses[weatherDay['time'].split(' ')[1]] = hourStatus
    statuses[weatherDay['time']] = hourStatus
print(statuses)
