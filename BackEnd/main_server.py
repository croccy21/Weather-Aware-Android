import lib.parse as parse
import lib.tools as tools

def main(conditions,conditionsList):
    ##for condition in conditionsList:
    ##    print(condition['number'])
    ##    print(condition['condid'])
    ##    print(condition['start'])
    ##    print(condition['end'])
    ##    print()
    weather = parse.parseWeather("2015","07","28","12","06","00","37.8267","-122.423")
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
        precipStatus = False
        status = False
        testOffset = 0
        if float(weatherDay['precipIntensity']) != 0 and (weatherDay['precipType'] == 'rain' or weatherDay['precipType'] == 'hail'):
            if float(weatherDay['precipIntensity']) >= 10.16:
                if float(weatherDay['precipProbability']) >= 40 - testOffset:
                    status = True
                else:
                    status = False
            elif float(weatherDay['precipIntensity']) >= 2.54:
                if float(weatherDay['precipProbability']) >= 50 - testOffset:
                    status = True
                else:
                    status = False
            elif float(weatherDay['precipIntensity']) >= 0.4318:
                if float(weatherDay['precipProbability']) >= 60 - testOffset:
                    status = True
                else:
                    status = False
            elif float(weatherDay['precipIntensity']) >= 0.0508:
                if float(weatherDay['precipProbability']) >= 70 - testOffset:
                    status = True
                else:
                    status = False
        else:
            status = False
        precipStatus = status
        hourStatus.append(status)
        #####
        status = False
        testOffset = 0
        if float(weatherDay['precipIntensity']) != 0 and (weatherDay['precipType'] == 'snow' or weatherDay['precipType'] == 'sleet'):
            if float(weatherDay['precipIntensity']) >= 10.16:
                if float(weatherDay['precipProbability']) >= 30 - testOffset:
                    status = True
                else:
                    status = False
            elif float(weatherDay['precipIntensity']) >= 2.54:
                if float(weatherDay['precipProbability']) >= 40 - testOffset:
                    status = True
                else:
                    status = False
            elif float(weatherDay['precipIntensity']) >= 0.4318:
                if float(weatherDay['precipProbability']) >= 50 - testOffset:
                    status = True
                else:
                    status = False
            elif float(weatherDay['precipIntensity']) >= 0.0508:
                if float(weatherDay['precipProbability']) >= 60 - testOffset:
                    status = True
                else:
                    status = False
        else:
            status = False
        if status == True and precipStatus == False:
            precipStatus = True
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
        hourStatus.append(precipStatus)
        #statuses[weatherDay['time'].split(' ')[1]] = hourStatus
        statuses[weatherDay['unixtime']] = hourStatus
    #print(statuses)
    returnJSONkey = []
    returnJSONvalue = []
    for condition in conditionsList:
        time = int(condition['start'])
        found = False
        while found == False and time < int(condition['end']):
            #print(time)
            if statuses[str(time)][int(condition['condid']) - 1]:
                found = True
            time += 3600
        returnJSONkey.append(condition['number'])
        returnJSONvalue.append(found)
        returnJSON = tools.jsonConstructor(returnJSONkey,returnJSONvalue,False)
    return returnJSON

conditions, conditionsList = parse.parseURL("www.server.co.uk/?no=1&condid=1&start=1438178400&end=1438182000&no=2&condid=3&start=1438178400&end=1438185600")
json = main(conditions, conditionsList)
print(json)
