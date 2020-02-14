import mysql.connector
from mysql.connector import Error
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
from datetime import datetime

db_host = 'arfo8ynm6olw6vpn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_database = 's0c8nimyeq16ttuu'
db_user = 'c743p4yjsqmow8m8'
db_password = 'f1cnrykplyr5x4fm'

sensor_bmp = BMP085.BMP085()
sensor_dht = Adafruit_DHT.DHT22

h, t = Adafruit_DHT.read_retry(sensor_dht, 26)

temp = (sensor_bmp.read_temperature() + t)/2
pressure = sensor_bmp.read_pressure()

time = datetime.now(tz=None)

print('Temp = {0:0.1f}*C Humidity = {1:0.1f}% Pressure = {2:0.2f} Pa'.format(temp,h,pressure))

print(time)

try:
    connection = mysql.connector.connect(host= db_host,
                                         database= db_database,
                                         user= db_user,
                                         password= db_password)
    cursor = connection.cursor()

    insert_query = """ INSERT INTO datalog (transactTime, temp, humi, pres)
    VALUES (%s, %s, %s, %s)"""

    record_tuple = ( time , temp , h , pressure )

    cursor.execute(insert_query, record_tuple)

    connection.commit()

    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
