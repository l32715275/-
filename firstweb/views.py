import sys,re,os
import random
#ms, infile, outfile = sys.argv

from django.http import HttpResponse
from django.shortcuts import render
from firstweb.models import Cal
from untitled9.InputJson import OperationJson
from firstweb import models
# Create your views here.
import sqlite3
import sys,re,os
import requests

def index(request):
    return render(request,'index.html')
def cal(request):
    a=request.POST['a']
    b=request.POST['b']
    c=a+b
    Cal.objects.create(a=c)
    return render(request,'index.html',context={'data':c})
    print(a,b)


def klvchen(req):
    print("前端数据: ", req.POST)

    print("file:", req.FILES)

    for item in req.FILES:
        print(item)
        obj = req.FILES.get(item)  # 获取要写入的文件
        filename = obj.name  # 获取文件名
        print(filename)
        data=OperationJson(filename).read_data()
        print(data)
        OperationJson(filename).input_data(data)
        print(filename)
        f = open(filename, 'wb')
        for line in obj.chunks():  # 分块写入
            f.write(line)
        print(f)
        f.close()
    return render(req, "input.html")

def sheet(req,id):
    con = sqlite3.connect('untitled9/db.sqlite3')

    cur = con.cursor()
    cur.execute("PRAGMA table_info(DeathStatistics)")
    col_names = cur.fetchall()
    print(col_names)
    col_name = []
    col_name = [x[1] for x in col_names]
    cur.execute("select * from DeathStatistics")
    data=cur.fetchall()
    con.commit()
    return render(req,"sheet.html",context={'data':data,'col_name':col_name,'id':id})


def DisasterType(req):
    return render(req, "forms.html")


def DeleteSheet(req,delete_id,id):
    con = sqlite3.connect('untitled9/db.sqlite3')
    cur = con.cursor()
    cur.execute("DELETE FROM DeathStatistics WHERE ID="+delete_id)
    con.commit()
    num=-10
    return ditu(req,num)
def AddSheet(req,id):
    con = sqlite3.connect('untitled9/db.sqlite3')
    cur = con.cursor()
    add = req.POST.getlist('add_data', [])
    print(add)
    strr = ""
    if str(add[1])=="tianjin":
        strr += "120000000000111455,'tianjin',"
    if str(add[1])=="beijing":
        strr += "110112031242221762,'beijing',"
    if str(add[1])=="chengdu":
        strr += "510107024645645111,'chengdu',"
    if str(add[1])=="hefei":
        strr += "340121031245784121,'hefei',"
    if str(add[1])=="wuhan":
        strr += "420106324325517625,'wuhan',"
    if str(add[1]) == "shanghai":
        strr += "310105464587878454,'shanghai',"
    if str(add[1]) == "xianggang":
        strr += "394725355174456454,'xianggang',"
    num=0
    if str(add[1])=="shanghai":
        num=1
    elif str(add[1])=="xianggang":
        num=2
    elif str(add[1])=="guangzhou":
        num=3
    elif str(add[1])=="shenzhen":
        num=4
    for x in add[2:]:
        strr += (str(x) + ',')
    strr = strr[:-1]
    sql = "INSERT INTO DeathStatistics  VALUES(" + strr + ")"
    print(sql)
    # sql = "UPDATE CommDisaster SET " + item + " = " + str(data[item]) + " WHERE ID = " + id
    cur.execute(sql)
    con.commit()
    return ditu(req,num)


def ditu(req,num):
    var1 = '{position:{x:121.13333,y:32.50000},content:\'<h2><a href="http://news.163.com/13/0709/18/93C35A8A0001124J.html" target="_blank">上海</a></h2><p></p>\'},'
    var2 = '{position:{x:114.10000,y:24.20000},content:\'<h2><a href="http://news.163.com/13/0709/18/93C35A8A0001124J.html" target="_blank">香港</a></h2><p></p>\'},'
    var3 = '{position:{x:113.3333,y:25.16667},content:\'<h2><a href="http://news.163.com/13/0709/18/93C35A8A0001124J.html" target="_blank">广州</a></h2><p></p>\'},'
    var4 = '{position:{x:114.06667,y:22.61667},content:\'<h2><a href="http://news.163.com/13/0709/18/93C35A8A0001124J.html" target="_blank">深圳</a></h2><p></p>\'},'

    city = [var1, var2, var3, var4]
    i = num-1

    with open("result.html", 'w', encoding='utf-8') as o:
        with open("C:/Users/AERO/Desktop/untitled9/templates/sheet.html", encoding='utf-8') as f:
            f = f.read()
            pos = f.find("var data=[")
            if pos != -1:
                # result = f[:pos] + "bbb" + f[pos:]  # bbbtable3 [前]
                # result = f[:pos] + "bbb" + f[(pos+6):]  # bbb [
                result = f[:(pos + 10)] + city[i] + f[(pos + 10):]  # table3bbb [后]
                o.write(result)
            else:
                print("error: there is no this table3")
    os.rename('C:/Users/AERO/Desktop/untitled9/templates/sheet.html', str(random.randint(0, 1000)) + '.html')
    os.rename('result.html', 'C:/Users/AERO/Desktop/untitled9/templates/sheet.html')
    con = sqlite3.connect('untitled9/db.sqlite3')

    cur = con.cursor()
    cur.execute("PRAGMA table_info(DeathStatistics)")
    col_names = cur.fetchall()
    print(col_names)
    col_name = []
    col_name = [x[1] for x in col_names]
    cur.execute("select * from DeathStatistics")
    data=cur.fetchall()
    con.commit()
    return render(req,"sheet.html",context={'data':data,'col_name':col_name,'id':id})

def transmit(req):
    con = sqlite3.connect('untitled9/db.sqlite3')

    cur = con.cursor()
    cur.execute("PRAGMA table_info(DisasterRequest)")
    col_names = cur.fetchall()
    print(col_names)
    col_name = []
    col_name = [x[1] for x in col_names]
    cur.execute("select * from DisasterRequest")

    data = cur.fetchall()
    return render(req,"transmit.html",context={'data':data,'col_name':col_name,'id':id})

def index(req):
    return render(req,"index.html")


def tables(req):
    con = sqlite3.connect('untitled9/db.sqlite3')

    cur = con.cursor()
    cur.execute("PRAGMA table_info(CommDisaster)")
    col_names = cur.fetchall()
    print(col_names)
    col_name = []
    col_name = [x[1] for x in col_names]
    cur.execute("select * from CommDisaster")
    data = cur.fetchall()
    cur.execute("PRAGMA table_info(DeathStatistics)")
    col_namesa = cur.fetchall()
    print(col_names)
    col_namea = []
    col_namea = [x[1] for x in col_namesa]
    cur.execute("select * from DeathStatistics")
    dataa = cur.fetchall()
    return render(req, "tables.html", context={'data': data, 'col_name': col_name,'dataa': dataa, 'col_namea': col_namea})

