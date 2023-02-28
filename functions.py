import time
import datetime

def check_if_midnight():
    while True:
        cur_time = datetime.datetime.now().replace(
            microsecond=0,
            second=0
        )
        if cur_time == "00:00:00":
            print("tracking starts")
            break
        else:
            pass
    time.sleep(60)