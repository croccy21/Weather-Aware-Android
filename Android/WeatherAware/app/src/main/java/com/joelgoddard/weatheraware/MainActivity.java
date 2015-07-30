package com.joelgoddard.weatheraware;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.TimePicker;


public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void alarmNameClick(View view) {
        switchName(view);
    }

    public void switchName(View v){
        TextView name = (TextView) findViewById(R.id.alarm_name);
        EditText nameEdit = (EditText) findViewById(R.id.alarm_name_edit);
        RelativeLayout holder = (RelativeLayout) findViewById(R.id.alarm_name_holder);
        if(name.getVisibility()==View.VISIBLE){
            name.setVisibility(View.GONE);
            nameEdit.setText(name.getText());
            holder.setVisibility(View.VISIBLE);
        }
        else{
            holder.setVisibility(View.GONE);
            name.setText(nameEdit.getText());
            name.setVisibility(View.VISIBLE);
        }
    }

    public void timeClick(View view) {
        switchClock();
    }

    public void switchClock(){
        TextView clock = (TextView) findViewById(R.id.clock_display);
        TimePicker timePicker = (TimePicker) findViewById(R.id.time_picker);
        LinearLayout holder = (LinearLayout) findViewById(R.id.time_holder);
        if(clock.getVisibility()==View.VISIBLE){
            clock.setVisibility(View.GONE);
            Log.d("Test", ((String) clock.getText()).substring(0, 2));
            timePicker.setIs24HourView(true);
            timePicker.setCurrentHour  (Integer.parseInt(((String) clock.getText()).substring(0, 2)));
            timePicker.setCurrentMinute(Integer.parseInt(((String)clock.getText()).substring(3, 5)));
            holder.setVisibility(View.VISIBLE);
        }
        else{
            holder.setVisibility(View.GONE);
            clock.setText(String.format("%02d",timePicker.getCurrentHour())
                    + ":" + String.format("%02d", timePicker.getCurrentMinute()));
            clock.setVisibility(View.VISIBLE);
        }
    }

    public void repeatCheckClicked(View view) {
        TextView dateSelector = (TextView) findViewById(R.id.date_selctor);
        LinearLayout daySelector = (LinearLayout) findViewById(R.id.day_selector);
        CheckBox repeat = (CheckBox) view;

        if (repeat.isChecked()){
            dateSelector.setVisibility(View.GONE);
            daySelector.setVisibility(View.VISIBLE);
        }
        else{
            dateSelector.setVisibility(View.VISIBLE);
            daySelector.setVisibility(View.GONE);
        }

    }
}
