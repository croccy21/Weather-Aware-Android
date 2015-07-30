from datetime import datetime

def unixToDate(unix):
    return datetime.fromtimestamp(float(unix))

def jsonConstructor(keys,values,readable = False):
    #"1": true,
    json = "{ "
    if readable == True:
        json = "{\n"
    for index in range(len(keys)):
        if readable == True:
            pair = '    "' + str(keys[index]) + '": ' + str(values[index]).lower()
        else:
            pair = '"' + str(keys[index]) + '": ' + str(values[index]).lower()
        if index < len(keys)-1:
            if readable == True:
                pair += ",\n"
            else:
                pair += ", "
        json += pair
    if readable == True:
        json += "\n}"
    else:
        json += " }"
    return json
