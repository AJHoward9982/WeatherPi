import mysql.connector
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

    u = raw_input("Clear row [r]  or all [a] ?   ")

    if u == 'r':

        u_row = input("Enter transaction number:   ")
        delete_query = " DELETE FROM datalog WHERE transactID = " + str(u_row) + " "
        cursor.execute(delete_query)
        connection.commit()
        
    elif u == 'a':
        delete_query = """ DELETE FROM datalog """
        cursor.execute(delete_query)
        connection.commit()

    else:
        print("Error")
    
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("\nMySQL connection is closed")

