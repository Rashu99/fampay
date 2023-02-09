import datetime


def get_date_time_n_secs_ago(sec: int):
    """
        This function is used to calculate the time n secs ago

        input -> sec : Number of seconds ago time needed
        output -> datetime in iso format
    """
    uct_time = datetime.datetime.utcnow() - datetime.timedelta(seconds=sec)
    return uct_time.isoformat("T")+'Z'
