package com.joelgoddard.weatheraware;

/**
 * Created by Joel Goddard on 28/07/2015.
 */
public class AlarmCondition {
    protected int deltaTime;//minuets
    protected boolean conditionMet;
    protected int priority;
    protected AlarmData parent;
    protected int conditionID;
    protected boolean inverse;

    public AlarmCondition(AlarmData parent, int conditionID) {
        this.parent = parent;
        this.conditionID = conditionID;
        deltaTime = 0;
        conditionMet = false;
        inverse = false;
    }

    /**
     *
     * @return time difference in minuets
     */
    public int getDeltaTime() {
        return deltaTime;
    }

    /**
     * Sets the time difference between this and the main alarm in minuets
     * @param deltaTime
     */
    public void setDeltaTime(int deltaTime) {
        this.deltaTime = deltaTime;
    }

    public boolean isConditionMet() {
        return conditionMet;
    }

    public void setConditionMet(boolean conditionMet) {
        this.conditionMet = conditionMet;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public int getConditionID() {
        return conditionID;
    }

    public void setConditionID(int conditionID) {
        this.conditionID = conditionID;
    }

    public boolean isInverse() {
        return inverse;
    }

    public void setInverse(boolean inverse) {
        this.inverse = inverse;
    }

    public String getURL(){
        return "false";
    }
}
