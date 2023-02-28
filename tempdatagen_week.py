import time
from signal import signal, SIGTERM, SIGHUP, pause
from w1thermsensor import W1ThermSensor
import xlsxwriter
import datetime
import functions

time.sleep(30)

functions.check_if_midnight()

sensor = W1ThermSensor()
workbook = xlsxwriter.Workbook('data.xlsx')

def safe_exit(signum, safe_exit):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

minute = 1
day = 1
week = 0

while day <= 7:
    datatable = workbook.add_worksheet(workbook, "Tag " + str(day))
    while minute <= 1440:
        current_time = datetime.datetime.now().replace(
            microsecond=0,
            second=0
        )
        current_time_str = current_time.strftime("%H:%M:%S")
        try:
            temperature = sensor.get_temperature()
            temp = str(temperature)
            print(f'At {current_time_str}, the temperature is {temperature} celsius')
            datatable.write(minute - 1,0,current_time_str)
            datatable.write(minute - 1,day,temperature)
        except:
            print("Sensor has crashed!")
            sensor = W1ThermSensor()
        time.sleep(60)
        minute = minute + 1
    day = day + 1

workbook.close()

print("while loop verlassen")


