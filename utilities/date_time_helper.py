from datetime import datetime


def time_log() -> str:
    return datetime.now().strftime("%H:%M:%S:%f")[:-3]


def timestamp_to_time(timestamp: float) -> str:
    """Convert timestamp like `1726665714.2191246`
    to the human-readable time format like '14:22:06.630'
    """
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object.strftime("%H:%M:%S.%f")[:-3]
