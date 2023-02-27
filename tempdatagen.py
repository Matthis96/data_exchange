import time
from signal import signal, SIGTERM, SIGHUP, pause
from w1thermsensor import W1ThermSensor
import xlsxwriter
import datetime

time.sleep(30)

sensor = W1ThermSensor()
workbook = xlsxwriter.Workbook('data.xlsx')
datatable = workbook.add_worksheet()

def safe_exit(signum, safe_exit):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

i = 0

while i <= 1440:
    i = i + 1
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%H:%M:%S")
    try:
        temperature = sensor.get_temperature()
        temp = str(temperature)
        print(f'{i} The temperature is {temperature} celsius')
        index = str(i)
        datatable.write(i,0,index)
        datatable.write(i,1,temperature)
        datatable.write(i,2,current_time)
        datatable.write(i,3,current_time_str)
    except:
        print("Sensor has crashed!")
        sensor = W1ThermSensor()
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
    time.sleep(60)

print("while loop verlassen")
workbook.close()
