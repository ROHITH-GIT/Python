import pymysql
connection = pymysql.connect(
    host = "34.30.24.162", # this is the cloud-sql public ip address
    user = "root",
    #password = "hani",
    database = "MYSQLDB",
    port=3306
)

# Perform database operations
try:
    with connection.cursor() as cursor:
        # Execute SQL query
        sql = "SELECT * FROM TABLE_GCP"
        cursor.execute(sql)

        # Fetch all rows and print them
        rows = cursor.fetchall()
        for row in rows:
            print(row)
finally:
    # Close the database connection
    connection.close()