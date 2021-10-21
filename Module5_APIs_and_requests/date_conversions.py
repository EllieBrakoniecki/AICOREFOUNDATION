#%%
from datetime import datetime, timezone

def get_date_in_epoch_utc_time(date_in_iso_format):
    return datetime(date_in_iso_format.year,date_in_iso_format.month, date_in_iso_format.day, 0, 0).replace(tzinfo=timezone.utc).timestamp()

int(get_date_in_epoch_utc_time(datetime.today().date()))
# %%
