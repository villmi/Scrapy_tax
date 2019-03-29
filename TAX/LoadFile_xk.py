import mysql.connector

conn = mysql.connector.connect(host="47.96.140.226", user="user", passwd="yuanshen", database="warning_system")
cursor = conn.cursor()

with open("/Users/vill/Desktop/研一_part2/TAX/TAX/NJ/雨花台区-1320114.data", "r", encoding="gbk") as f:
    a = f.readline()
    print(a)
