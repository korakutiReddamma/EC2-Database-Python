from flask import Flask,render_template
import boto3,pprint,sqlite3

app=Flask( __name__)

# client = boto3.client('ec2')
# response =client.describe_instances()
# DB =sqlite3.connect('data1.db')
# DB.execute("create table data1( KeyName TEXT NOT NULL, InstanceId TEXT UNIQUE  NOT NULL , InstanceType TEXT NOT NULL)")
# k=response['Reservations']
# if type(k)==list:
#     a=len(k)
#     for i in range(a):
#         b=k[i]
#         c=b['Instances']
#         if len(c)>=1:
#             d=c[0]
#             DB= sqlite3.connect("data1.db")
#             h = DB.cursor()  
#             h.execute("INSERT into data1(KeyName,InstanceId,InstanceType) values (?,?,?)",(d['KeyName'],d['InstanceId'],d['InstanceType']))  
#             DB.commit()        
#             DB.close()   
# z = sqlite3.connect('data1.db')
# z.row_factory = sqlite3.Row
# x = z.cursor()
# x.execute('''SELECT * from data1''')
# result = x.fetchall()
# z.commit()
# z.close()
# @app.route('/Write')
# def write():
#     return(response)
@app.route('/read')
def read():
    z = sqlite3.connect('data1.db')
    z.row_factory = sqlite3.Row
    x = z.cursor()
    x.execute('''SELECT * from data1''')
    rows = x.fetchall()
    return render_template("view.html",rows = rows)
    

