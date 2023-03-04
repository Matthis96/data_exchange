import time
from signal import signal, SIGTERM, SIGHUP, pause
from w1thermsensor import W1ThermSensor
import xlsxwriter
import datetime
import functions

# declare important variables
t = 59


# start program when new day starts
functions.check_if_midnight()

time.sleep(25)

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
        datatable.write(i,0,current_time_str)
        datatable.write(i,1,temperature)
    except:
        print("Sensor has crashed!")
        sensor = W1ThermSensor()
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
    time.sleep(t)

print("while loop verlassen")
workbook.close()
