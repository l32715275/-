#coding:utf-8
import json
import sqlite3

# '''创建一个数据库，文件名'''
import sys


class OperationJson:

    def __init__(self,file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = 'C:/Users/AERO/Desktop/test.json'
        self.data = self.read_data()

    def read_data(self):
        with open(self.file_name,'rb') as fp:
            data = json.load(fp)
            return data


    def input_data(self,data):
        con = sqlite3.connect('untitled9/db.sqlite3')
        cur = con.cursor()

        for item in data.keys():
            print(data[item])
            print(type(data[item]))
            if item == 'ID':
                print("ID:  " + data[item])
                id = data[item]
        # print("id:   "+id)
        #if id[12:15] == '336':
        DT = "DeathStatistics"  # DT = DisasterType
        # print(id[12:15])
        for item in data.keys():
            if item == 'ID':
                sql = "INSERT INTO " + DT + " (" + item + ") VALUES(" + str(data[item]) + ")"
                cur.execute(sql)
                id = str(data[item])
            elif item == 'reporting_unit':
                sql = "UPDATE " + DT + " SET " + item + " = " + str(202) + " WHERE ID = " + id
                cur.execute(sql)
            elif data[item] != None:
                sql = "UPDATE " + DT + " SET " + item + " = " + str(data[item]) + " WHERE ID = " + id
                cur.execute(sql)
        con.commit()

    #def sheet(self, data):






if __name__ == '__main__':
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    cur = con.cursor()
    cur.execute("CREATE TABLE MissingStatistics(ID char(19),location char(100),date char(12),number integer (5),reporting char(50))")
    con.commit()
    # cur.execute("select * from CommDisaster WHERE id=1234564000003360022")
    # print(cur.fetchall())
    # cur.execute("PRAGMA table_info(CommDisaster)")
    # col_names = cur.fetchall()
    # print(col_names)
    # col_name = []
    # col_name = [x[1] for x in col_names]
    # print(col_name)
    # print(col_name[3])
    #allsheet=cur.fetchall()
    #print(allsheet)
    #print(allsheet[0][1])


