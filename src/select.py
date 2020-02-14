import mysql.connector
import datetime
from mysql.connector import Error

db_host = 'arfo8ynm6olw6vpn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_database = 's0c8nimyeq16ttuu'
db_user = 'c743p4yjsqmow8m8'
db_password = 'f1cnrykplyr5x4fm'

try:
    connection = mysql.connector.connect(host= db_host,
                                         database= db_database,
                                         user= db_user,
                                         password= db_password)
    cursor = connection.cursor(buffered=True)


    connection.commit()

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

    print("\n\n Transaction Id |     Transaction Time     | Temperature | Humidity |  Pressure \n"
          "------------------------------------------------------------------------------------")

    select_query = """ SELECT * FROM datalog """

    cursor.execute(select_query)

    for row in cursor.fetchall():

        db_ID = row[0]

        db_time = str(row[1])

        db_temp = str(row[2])

        db_humi = str(row[3])

        db_pres = str(row[4])

        print_string = '        {0}       |    {1}   |    {2}*C  |   {3}%  |   {4}Pa'.format( db_ID , db_time , db_temp , db_humi , db_pres )
        
        print( print_string )
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("\nMySQL connection is closed")

