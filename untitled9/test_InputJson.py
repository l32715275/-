import sqlite3
import json
import pytest

class TestClass:


    def read_data(self):
        file_name = 'C:/Users/AERO/Desktop/untitled9/test.json'
        with open(file_name, 'rb') as fp:
            data = json.load(fp)
            return data

    def input_data(self, data):
        con = sqlite3.connect('untitled9/db.sqlite3')
        cur = con.cursor()

        for item in data.keys():
            print(data[item])
            print(type(data[item]))
            if item == 'ID':
                print("ID:  " + data[item])
                id = data[item]
        # print("id:   "+id)
        # if id[12:15] == '336':
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

    def test_readdata(self):
        #self.read_data()
        a=[]
        for item in self.read_data().keys():

            a.append(item)
        print(a)
        assert a[0] == 'ID'

if __name__ == "__main__":
    pytest.main()