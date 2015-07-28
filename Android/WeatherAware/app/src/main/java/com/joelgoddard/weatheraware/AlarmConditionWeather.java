package com.joelgoddard.weatheraware;

import java.text.MessageFormat;
import java.util.Calendar;

/**
 * Created by Joel Goddard on 28/07/2015.
 */
public class AlarmConditionWeather extends AlarmCondition {
    protected int startTime = -1;
    protected int endTime = -1;
    protected int weatherID;
    protected int conditionID;

    public AlarmConditionWeather(AlarmData parent, int conditionID) {
        super(parent, conditionID);
    }

    public int getStartTime() {
        return startTime;
    }

    public boolean setStartTime(int startTime) {
        if(startTime>=0 && startTime<=24) {
            if(startTime<=endTime || endTime<0) {
                this.startTime = startTime;
                return true;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }

    public int getEndTime() {
        return endTime;
    }

    public boolean setEndTime(int endTime) {
        if(endTime>=0 && endTime<=24) {
            if(endTime>=startTime || startTime<0) {
                this.endTime = endTime;
                return true;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }

    public int getWeatherID() {
        return weatherID;
    }

    public void setWeatherID(int weatherID) {
        this.weatherID = weatherID;
    }

    @Override
    public String getURL() {
        Calendar start = (Calendar)parent.getDay().clone();
        start.add(Calendar.HOUR, startTime);
        Calendar end = (Calendar)parent.getDay().clone();
        end.add(Calendar.HOUR, endTime);
        return MessageFormat.format("no={}&condid={}&start={}&end={}", conditionID, weatherID, start.getTimeInMillis()/1000, end.getTimeInMillis()/1000);
    }



    
}
