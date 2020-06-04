import json
# -'- coding: utf-8 -'-
import sqlite3
con=sqlite3.connect('films.db')
cur=con.cursor()
with open('Movie_sessions_parser.json', encoding='UTF-8') as f:
	js = json.load(f)
	for i in js:
		print(i)
		#sqlite_insert_with_param = """INSERT INTO core_fes nam VALUES (?);"""
		data_tuple = []
		data_tuple.append(i)
		print (data_tuple)
		#cur.execute("""INSERT INTO core_fes VALUES ('?')""",data_tuple)
		sqlite_insert_with_param = """INSERT INTO films (nam) VALUES (?);"""
		cur.execute(sqlite_insert_with_param, data_tuple)
		bark=[]
		for j in js[i]:
			js[i][j]=str(js[i][j])
			bark.append(js[i][j])
			print(js[i][j])
		year=[bark[0],i]
		print (year)
		country=[bark[1], i]  
		producer=[bark[2], i] 
		duration=[bark[3], i]  
		rating=[bark[4], i]  
		theaters=[bark[5], i]  
		dates=[bark[6], i]  
		tim=[bark[7], i]  
		descript=[bark[8], i]
		sql_update_query = """UPDATE films SET year = (?) where nam = (?);""" 
		cur.execute(sql_update_query,year)
		sql_update_query = """UPDATE films SET country = (?) where nam = (?);""" 
		cur.execute(sql_update_query,country)
		sql_update_query = """UPDATE films SET producer = (?) where nam = (?);""" 
		cur.execute(sql_update_query,producer)
		sql_update_query = """UPDATE films SET duration = (?) where nam = (?);""" 
		cur.execute(sql_update_query,duration)
		sql_update_query = """UPDATE films SET rating = (?) where nam = (?);""" 
		cur.execute(sql_update_query,rating)
		sql_update_query = """UPDATE films SET theaters = (?) where nam = (?);""" 
		cur.execute(sql_update_query,theaters)
		sql_update_query = """UPDATE films SET dates = (?) where nam = (?);""" 
		cur.execute(sql_update_query,dates)
		sql_update_query = """UPDATE films SET tim = (?) where nam = (?);""" 
		cur.execute(sql_update_query,tim)
		sql_update_query = """UPDATE films SET descript = (?) where nam = (?);""" 
		cur.execute(sql_update_query,descript)		

con.commit()
cur.close()
con.close()