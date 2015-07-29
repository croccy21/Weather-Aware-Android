package com.joelgoddard.weatheraware;

import java.text.DateFormat;
import android.util.Log;

import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;

/**
 * Created by Joel Goddard on 28/07/2015.
 */
public class AlarmData {
    protected String name;
    protected int baseTime;//minutes
    protected int earliestTime;
    protected boolean[] repeats = new boolean[7];
    protected boolean repeat;
    protected boolean enabled;
    protected Calendar day;
    protected Calendar nextAlarm;
    protected ArrayList<AlarmCondition> conditions = new ArrayList<AlarmCondition>();
    protected AlarmCondition defaultAlarm;

    public AlarmData() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getBaseTime() {
        return baseTime;
    }

    public void setBaseTime(int baseTime) {
        this.baseTime = baseTime;
    }

    public int getEarliestTime() {
        return earliestTime;
    }

    public boolean[] getRepeats() {
        return repeats;
    }

    public void setRepeats(boolean[] repeats) {
        this.repeats = repeats;
        boolean repeat=false;
        for (boolean b:repeats){
            if (b= true){
                repeat = true;
            }
        }
    }

    public boolean isEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

    public Calendar getDay() {
        return day;
    }

    public void setDay(Calendar day) {
        this.day = day;
    }

    public ArrayList<AlarmCondition> getConditions() {
        return conditions;
    }

    public void setConditions(ArrayList<AlarmCondition> conditions) {
        this.conditions = conditions;
    }

    public void addCondition(AlarmCondition condition){
        conditions.add(condition);
    }

    public AlarmCondition getDefaultAlarm() {
        return defaultAlarm;
    }

    public void setDefaultAlarm(AlarmCondition defaultAlarm) {
        this.defaultAlarm = defaultAlarm;
    }

    public String getURL(){
        String url = "www.server.co.uk/?";
        for(AlarmCondition condition:conditions){
            String next = condition.getURL();
            if(!next.equals("false")) {
                url += next;
            }
        }
        return url;
    }

    public void calculateNextAlarm(){
        Calendar today = Calendar.getInstance();
        today.set(Calendar.SECOND, 0);
        today.set(Calendar.MILLISECOND, 0);
        Calendar alarmTime = (Calendar)today.clone();
        alarmTime.set(Calendar.HOUR_OF_DAY, 0);
        alarmTime.set(Calendar.MINUTE, earliestTime);
        if(alarmTime.before(today)){
            alarmTime.add(Calendar.HOUR, 24);
        }
        if(repeat) {
            for(boolean b:repeats){
                if (repeats[alarmTime.get(Calendar.DAY_OF_WEEK)]){
                    break;
                }
                else{
                    alarmTime.add(Calendar.HOUR, 24);
                }
                Log.e("AlarmData" ,"No Repeat Date Selected");
            }
        }
        nextAlarm = (Calendar)alarmTime.clone();
        alarmTime.set(Calendar.MINUTE, 0);
        alarmTime.set(Calendar.HOUR, 0);
        day = (Calendar)alarmTime.clone();
        DateFormat date = DateFormat.getDateInstance();
        DateFormat time = DateFormat.getTimeInstance();
        Log.d("Debug", MessageFormat.format("Alarm set to {} on {}",
                time.format(nextAlarm.getTime()), date.format(nextAlarm.getTime())));
    }
}
