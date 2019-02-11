from flask import Flask
from flask import render_template

import sqlite3
from sqlite3 import Error

app = Flask(__name__)
db_file = "db.sqlite"


@app.route('/<page_number>')
def home(page_number=0):
	conn = connection(db_file)
	items = select_items(conn,page_number)
	#print(items)
	return render_template('index.html', page_number=page_number,items=items)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/help')
def help():
	return render_template('help.html')


def connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
		return None

def select_items(conn,page_number=0):
	cur = conn.cursor()
	page_items = 10
	max_id = int(page_number) * int(page_items)
	sql ="SELECT * FROM ITEMS where id > {max_id} order by id limit {page_items}".format(max_id=max_id,page_items=page_items) 
	#print(sql)
	cur.execute(sql)
	rows = cur.fetchall()		
	items = []
	for row in rows:
		items.append(row)
	return items
