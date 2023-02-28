import boto3,pprint,sqlite3
client = boto3.client('ec2')
response =client.describe_instances()
DB =sqlite3.connect('data1.db')
DB.execute("create table data1( KeyName TEXT NOT NULL, InstanceId TEXT UNIQUE  NOT NULL , InstanceType TEXT NOT NULL)")
# pprint.pprint(response)
k=response['Reservations']
if type(k)==list:
    a=len(k)
    #print(a)
    for i in range(a):
        b=k[i]
        #pprint.pprint(b)
        c=b['Instances']
        # pprint.pprint(c)
        if len(c)>=1:
            d=c[0]
            # pprint.pprint(d)
            # print(d['VpcId'],d['KeyName'],d['ImageId'])
            DB= sqlite3.connect("data1.db")
            h = DB.cursor()  
            h.execute("INSERT into data1(KeyName,InstanceId,'InstanceType) values (?,?,?)",(d['KeyName'],d['InstanceId'],d['InstanceType']))  
            DB.commit()        
            DB.close()    