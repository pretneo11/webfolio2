
from flask import Flask, render_template, request, redirect
import csv 
from robohasher import create_robot
import random
from movies import main_func 

app=Flask(__name__)
# print(__name__) --> main

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def render_page(page_name):
	if page_name =='robots.html':
		return render_template(page_name, quote='\"Create Life, Don\'t Consume It.\"', author='Oliviero Toscani')
	else:
		return render_template(page_name)

def write_to_csv(data):
	with open('database.csv', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])  # has to be a list!!

def random_quote():
	with open('quotes.txt', 'r') as file:
		quotes_list = file.readlines()
		selected_quote = random.choice(quotes_list)
		return selected_quote		


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')

		except:	
			return 'Could not save to database.'
	else:
		return "Something went wrong."		

@app.route('/submit_text', methods=['GET', 'POST'])
def submit_robot():
	if request.method == 'POST':
		try:
			hash = request.form['hash_text']
			quote_now = random_quote().split('-') #get the list, separate quote from author
			quote_text = quote_now[0].strip()
			quote_author = quote_now[1].strip()
			create_robot(hash)
			return render_template('/robots.html', quote=quote_text, author=quote_author)

		except:	
			return 'Could not generate the robot.'
	else:
		return "Something went wrong."			

	
@app.route('/next_movie', methods=['GET', 'POST'])
def find_movie():
	if request.method == 'POST':
		try:
			movie_desc, image_link, opis1 = main_func()
			return render_template('/movies.html', movie=movie_desc, image1=image_link, opis_filma=opis1)
		except:
			return "Couldn't find a movie."
	else:
		return "Something went wrong."			





