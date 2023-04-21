import pandas as pd
import mysql.connector
#Importing CSV data
data = pd.read_csv ('reader.csv') 
x = data['EmpCode'].tolist() #Converting data frame to list
resultString = ','.join(map(str, x)) #Converting list to comma seperated values as string
#Connectin to mysql 
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="@123"
)
mycursor = mydb.cursor()
#Querying the Database to fetch results
sql_query =mycursor.execute("select * from rohith_migration.employee where EmpCode in ( {})".format(resultString))
myresult = mycursor.fetchall()  
colnames = [desc[0] for desc in mycursor.description]  #Iteration to get column names   
df = pd.DataFrame(myresult)
#Converting dataframes to CSV
df.to_csv (r'C:\Users\Rohith Thadem\OneDrive\Desktop\New folder\exported_data.csv', index = False, header=colnames) # place 'r' before the path name
mydb.close()