package com.joelgoddard.weatheraware;

import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.text.DateFormat;
import java.util.List;

/**
 * Created by Joel Goddard on 29/07/2015.
 */
public class AlarmListAdapter extends ArrayAdapter{

    private Context context;
    private boolean useList = true;

    public AlarmListAdapter(Context context, List items) {
        super(context, R.layout.alarm_list_item, items);
        this.context = context;
    }

    /**
     * Holder for the list items.
     */
    private class ViewHolder{
        TextView alarmName;
        TextView clockDisplay;
    }

    /**
     *
     * @param position
     * @param convertView
     * @param parent
     * @return
     */
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder holder = null;
        AlarmData item = (AlarmData)getItem(position);
        View viewToUse = null;

        // This block exists to inflate the settings list item conditionally based on whether
        // we want to support a grid or list view.
        LayoutInflater mInflater = (LayoutInflater) context
                .getSystemService(Activity.LAYOUT_INFLATER_SERVICE);
        if (convertView == null) {
            if(useList){
                viewToUse = mInflater.inflate(R.layout.alarm_list_item, null);
            } else {
                viewToUse = mInflater.inflate(R.layout.alarm_grid_item, null);
            }

            holder = new ViewHolder();
            holder.alarmName = (TextView)viewToUse.findViewById(R.id.alarm_name);
            holder.clockDisplay = (TextView)viewToUse.findViewById(R.id.clock_display);
            viewToUse.setTag(holder);
        } else {
            viewToUse = convertView;
            holder = (ViewHolder) viewToUse.getTag();
        }

        holder.alarmName.setText(item.getName());
        DateFormat df = DateFormat.getTimeInstance(DateFormat.SHORT);
        holder.clockDisplay.setText(df.format(item.getNextAlarm().getTime()));
        return viewToUse;
    }
}
