import pandas as pd

#http://stackoverflow.com/questions/24980437/pandas-groupby-and-then-merge-on-original-table
#http://stackoverflow.com/questions/13854476/pandas-transform-doesnt-work-sorting-groupby-output/13854901#13854901
#
dir_path = "/home/h/Desktop/talking_data/csv/"
def app_label_feature():
    app_labels = pd.read_csv(dir_path + "app_labels.csv")
    grouped_labels = app_labels.groupby("app_id", as_index=False)
    app_label_info = grouped_labels.agg(lambda x: ",".join(list(x['label_id'].apply(str))))
    return app_label_info

def events_group_stat(single_group_df):
    #group_df[]
    single_group_df.ap
    pass

def app_events_cat_info(app_label_feature):
    app_events = pd.read_csv(dir_path + "app_events.csv")
    merged_envents = pd.merge(app_events,app_label_info, how = 'outer', on = 'app_id')
    merged_events[['event_id','app_id', 'is_installed', 'is_active']] = merged_events[['event_id','app_id', 'is_installed', 'is_active']].astype(int)
    grouped_events = merged_events.groupby("event_id", as_index=False)
    app_event_info = grouped_events.apply(events_group_stat)
    return app_event_info
