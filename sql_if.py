import pymysql
import pandas as pd 
import math
#read data from csv
data=pd.read_csv('Journal Impact factor_2017.csv')
data=data.iloc[1:10]
#connect to mysql
conn=pymysql.connect(user='root')
cur=conn.cursor()
#create database
#cur.execute('CREATE DATABASE IF NOT EXISTS citationMap')
cur.execute('use citationMap')
#remove table
cur.execute('DROP TABLE IF EXISTS impactFactor_')
#create table
cur.execute('CREATE TABLE IF NOT EXISTS impactFactor_(FullJournalTitle varchar(200),ImpactFactor varchar(20),primary key (FullJournalTitle))')

for idx,row in data.iterrows():
	if not type(row[1])==float and not cur.execute('select 1 from impactFactor_ where FullJournalTitle=%s',row[1]) :
		print row[1]
		cur.execute('INSERT INTO impactFactor_(FullJournalTitle,ImpactFactor) values(%s,%s)',(row[1],row[3]))
conn.commit()
cur.close()
conn.close()