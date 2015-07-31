import urllib.request
import json
import re
import time
import datetime

def parseWeather(year,month,day,hour,latitude,longitude):
    """Get the data from the weather API and return it in a useful format"""
    now = datetime.datetime.now()
    
    ########################################################################
    # Use The URL for the weather Data
    #
    url = 'https://api.forecast.io/forecast/94f336d8e9a37828d0cf3639f474c531/%s,%s,%s-%s-%sT%s:00:00+01:00?units=si&exclude=currently,minutely,daily,alerts,flags' % (str(latitude),str(longitude),str(year),str(month).zfill(2),str(day).zfill(2),str(hour).zfill(2))
    response = urllib.request.urlopen(url)
    str_response = response.readall().decode('utf-8')
    #
    ########################################################################
    # Use dummy weather Data to test things
    #
##    file = open("sample data.txt")
##    str_response = file.read()
##    file.close()
    #
    ########################################################################

    # Convert JSON response from the weather API into a python dictionary object
    obj = json.loads(str_response)
    returnList = []
    for i in list(obj['hourly']['data']):
        tempDictionary = {}
        for x in list(i):
            # Create a new dictionary strictly containing the hourly data for ONE day using the attributes
            # time
            # unixtime
            # summary
            # icon
            # precipIntensity
            # precipProbability
            # precipType
            # temperature
            # apparentTemperature
            # dewPoint
            # humidity
            # windSpeed
            # windBearing
            # visibility
            # cloudCover
            # pressure
            # ozone
            if x != "time":
                tempDictionary[x] = str(i[str(x)])
            else:
                tempDictionary["unixtime"] = str(i[str(x)])
                tempDictionary["time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[str(x)]))
        returnList.append(tempDictionary)
    return returnList

def parseURL(data):
    """Scrape the information from the request URL and return in a useful format"""
    # Regex pattern to scrape the one off information at the beginning of the URL
    pattern = "count=\d+&lat=-*\d+\.*\d*&long=-*\d+\.*\d*"
    alarmData = re.findall(pattern, data, re.IGNORECASE)
    try:
        params = alarmData[0].split("&")
    except:
        return None, None
    for index in range(len(params)):
        params[index] = params[index].split("=")[1]
    # Assign the scraped information to the below attributes within a dictionary
    alarmDataDict = {}
    alarmDataDict['count'] = params[0]
    alarmDataDict['lat'] = params[1]
    alarmDataDict['long'] = params[2]
    
    # Regex pattern to scrape the condition information
    pattern = "no=\d+&condid=\d+&start=\d+&end=\d+"
    conditions = re.findall(pattern, data, re.IGNORECASE)
    conditionsList = []
    # ConditionID = ListIndex = Name
    # 1 = 0 = Wind
    # 2 = 1 = Snow
    # 3 = 2 = Rain
    # 4 = 3 = Visibility
    # 5 = 4 = Precipitation
    # Assign the scraped information to the below attributes within a dictionary within a list
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
    return conditionsList, alarmDataDict
