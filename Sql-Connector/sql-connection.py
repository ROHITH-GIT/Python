import mysql.connector
conn = mysql.connector.connect(read_default_file='my.cnf.txt')
print("Connection Successful!!!!")
cursor=conn.cursor()
query="""select * from oscarval_sql_course.imdb_movies limit 10"""
cursor.execute(query)
data = cursor.fetchall()
for i in data:
    print(i)
conn.close()
