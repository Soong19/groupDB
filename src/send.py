import json
import pickle
from socket import *
import time
import pandas as pd

# 1.创建套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 2.准备连接服务器，建立连接
serve_ip = "127.0.0.1"
serve_port = 9999  # 端口，比如8000
tcp_socket.connect((serve_ip, serve_port))  # 连接服务器，建立连接,参数是元组形式

# 准备需要传送的数据
# 最后一定要加 \n 来确保有效
send_data = "select * from dep,stuff where dep.name=stuff.depart;\n"
send_data = "select * from stuff,dep where stuff.depart=dep.name and dep.name=ds;\n"
# send_data="select * from table1,table2 where table1.name=table2.name;\n"
# send_data = "create table stuff(sid int *,name varchar,depart varchar);\n"
# send_data = "create table dep(did int *,name varchar,n_num int);\n"
# send_data="insert into stuff(sid,name,depart) values(1,q,ds);\n"
# send_data="insert into stuff(sid,name,depart) values(2,w,ds);\n"
# send_data="insert into dep values(1,ds,2);\n"
# send_data="insert into dep values(3,cs,3);\n"
print('sending')
tcp_socket.send(send_data.encode('ASCII'))
print('success send')
# 从服务器接收数据
# 注意这个1024byte，大小根据需求自己设置

data = ''
print('receiving')
while True:
    msg = tcp_socket.recv(4096).decode('UTF-8')
    if msg[-3:] == '[O]':
        data = data + msg[:-3]
        # do other things. do not break;
        break
    data = data + msg

print('success receive')
print('load json')
data_json = json.loads(data)
print(data_json)

count=data_json['count']
countFieldName=data_json['countFieldName']
fieldNames = data_json['fieldNames']
data = data_json['data']
df=pd.DataFrame(data,columns=fieldNames)
print(count,countFieldName)
print(pd.DataFrame(data))


time.sleep(100)

# 关闭连接
tcp_socket.close()
