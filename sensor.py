#import RPi.GPIO as GPIO
from multiprocessing import connection
import time,os
import mysql.connector
from datetime import datetime

TRIG = 23
ECHO = 24


def insert_variables(distance, timestamp):
    try:
        connection = mysql.connector.connect(
            database="level",
            host="localhost",
            user="root"
        )

        cursor = connection.cursor()
        mysql_insert_query = f"INSERT INTO `level_log`(`level`, `timestamp`) VALUES ({distance},{timestamp})"
        cursor.execute(mysql_insert_query)
        connection.commit()
        print("Data added to the db")

    except mysql.connector.Error as error:
        print("Fail to insert into table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection is closed")


print ('Distance measurement in progress')
#GPIO.setup(TRIG,GPIO.OUT)
#GPIO.setup(ECHO,GPIO.IN)

#GPIO.output(TRIG,False)
#time.sleep(2)

#GPIO.output(TRIG,True)
#time.sleep(0.00001)
#GPIO.output(TRIG,False)

#while GPIO.input(ECHO)==0:
#    pulse_start = time.time()

#while GPIO.input(ECHO)==1:
#    pulse_end = time.time()

pulse_start = 0.1
pulse_end = 0.2
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)
print ('Distance:',distance,'cm')



now = datetime.now()
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)
now = now.strftime("%Y/%m/%d %H:%M:%S")
print(now)

insert_variables(distance, timestamp)

#GPIO.cleanup()



#https://pynative.com/python-timestamp/
#https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
#https://github.com/jiteshsaini/Smart-Water-Tank
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
#https://medium.com/analytics-vidhya/install-pyodbc-on-centos-rhel-ae5062830a2b
#https://pynative.com/python-mysql-insert-data-into-database-table/