# import flask
from flask import Flask,request,render_template,redirect,url_for,make_response,jsonify,json,session
# import requests
# import mechanize 
# from bs4 import BeautifulSoup 
# import csv
# import numpy as np
# import json
# import http.cookiejar
# import datetime
# import os
# import os
from scraper.scrape import Attendance
# from c import make_celery
# from celery import Celery


app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "asdsad890asdashdlahdlj1n2j3bjk4bhkbj12n3jl1"

# @app.route('/broken')
# def broken():
# 	return "broken_celery"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/info')
def info():
	return redirect("https://snip-engine.herokuapp.com/info.php")

@app.route('/dblog')
def dblog():
	return redirect("https://snip-engine.herokuapp.com/dblog.php")

@app.route('/login',methods=['POST','GET'])
def login():
	# print("reached here")
	if request.method == 'POST':
		username = request.form['username'].upper()
		# print(username)
		password = request.form['password']

		# adding user to session
		session["username"] = request.form['username']

		# if username == "SCS/7026/16":
		# 	# for i in range(100000000000):
		# 	# 	print(0)
		# 	payload = [{'name_of_user': 'VISHNU  RAMESH', 'subject': 'Data Mining and Ware Housing', 'total_class': '32', 'atten_class': '27', 'percentage': '84.38'}, {'name_of_user': 'VISHNU  RAMESH', 'subject': 'Embedded Systems', 'total_class': '32', 'atten_class': '23', 'percentage': '71.88'}, {'name_of_user': 'VISHNU  RAMESH', 'subject': 'Data Science', 'total_class': '27', 'atten_class': '20', 'percentage': '74.07'}, {'name_of_user': 'VISHNU  RAMESH', 'subject': 'Project', 'total_class': '144', 'atten_class': '112', 'percentage': '77.78'}, {'name_of_user': 'VISHNU  RAMESH', 'subject': 'Disaster Management', 'total_class': '27', 'atten_class': '17', 'percentage': '62.96'}]
		# 	return render_template("1.html",error = "0",data=payload,username=username)

		return data_page(username,password)
	else:
		print("user not logged in, hence redirected")
		return redirect('/',302)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/',302)

# # udayip 101
# info=None

# @app.route('/loading',methods = ['POST', 'GET'])
# def loading():
# 	form_data = {}
# 	form_data['username'] = request.form['username']
# 	# print(form_data)
# 	form_data['password'] = request.form['password']
# 	global info
# 	info = form_data
# 	return render_template('loading.html', form_data=form_data)

# @app.route('/data_page',methods = ['POST', 'GET'])
def data_page(username,password):
	# global info
	# print(info)
	# for i in range(10):
	# 	print()
	# try:
	# username  = info["username"].upper()
	# password = info["password"]


	
		
	payload = []

	# checking if username or password is wrong
	data = None
	try:
		data, name_of_user = Attendance(username,password)
	except Exception as e:
		pass

	if data is None:
		print("+++++++++++++++")
		print("data is None!")
		print("+++++++++++++++")
		return render_template("1.html",error = "1",data=payload,username=username)

	
	try:
	    # print(data)
	    for i in data:
	        v_data={}
	        ##name of the user
	        v_data['name_of_user'] = name_of_user
	        v_data['subject'] = i[0]
	        v_data['total_class'] = i[1]
	        v_data['atten_class'] = i[4]
	        v_data['percentage'] = i[5]

	        payload.append(v_data)

	except Exception as e:
		print(e)

	# print(payload)
	# payload = json.dumps(payload)
	print("==================")
	print("everythin worked fine!")
	# return render_template("index.html")
	return render_template("1.html",error = "0",data=payload,username=username)


if __name__ == '__main__':
   # app.run("127.0.0.1",1111,debug = True)
   app.run()