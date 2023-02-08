import datetime


def get_date_time_n_secs_ago(sec: int):
    uct_time = datetime.datetime.utcnow() - datetime.timedelta(seconds=sec)
    return uct_time.isoformat("T")+'Z'
