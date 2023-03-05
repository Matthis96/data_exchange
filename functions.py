import time
import datetime

def check_if_midnight():
    while True:
        cur_time = datetime.datetime.now().replace(
            microsecond=0,
            second=0
        )
        cur_time = cur_time.strftime('%H:%M:%S')
        print(cur_time)
        if str(cur_time) == "00:00:00":
            print("tracking starts")
            break
        else:
            time.sleep(30)
