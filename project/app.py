from flask import Flask, render_template,flash , redirect, url_for,session, logging, request, session
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import sqlite3
import numpy as np
from random import randint 
from functools import wraps



#con=sqlite3.connect('/Users/NONE/flask/venv/project/pars/thea.db')
#cur=con.cursor()

#cur.close()
#con.close()


app = Flask (__name__)

# config MySQL
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="D@nil@2001"
app.config['MYSQL_DB']="myflaskapp"
app.config['MYSQL_CURSORCLASS']="DictCursor"
# init MYSQL
mysql=MySQL(app)

#Articles=Articles()

@app.route('/')
def index():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/articles")
def articles():
	cur = mysql.connection.cursor()

	result=cur.execute("SELECT * FROM articles")

	articles=cur.fetchall()

	if result > 0:
		return render_template('articles.html', articles=articles)
	
	else:
		msg = "No articles Found"
		return render_template('articles.html', msg=msg)

	cur.close()

#get article
@app.route("/article/<string:id>/")
def article(id):
	cur = mysql.connection.cursor()

	result=cur.execute("SELECT * FROM articles WHERE id=%s", [id])

	article=cur.fetchone()

	return render_template("article.html", article=article)


# @app.route("/films")
# def films():
# 	con=sqlite3.connect('films.db')
# 	cur=con.cursor()

# 	result=cur.execute("SELECT * FROM films")

# 	films=cur.fetchall()
# 	print (films[1])
# 	#if films > 0:
# 		#return render_template('films.html', films=films)
# 	return render_template('film.html', films=films)
# 	#else:
# 		#msg = "No films are Found"
# 		#return render_template('films.html', msg=msg)

# 	cur.close()

#get article


# @app.route("/cinema/<string:name>/")
# def cinema(name):
# 	cur = mysql.connection.cursor()

# 	result=cur.execute("SELECT * FROM films WHERE name=%s", [name])

# 	cinema=cur.fetchone()

# 	return render_template("cinema.html", cinema=cinema)





@app.route("/films")
def films():
	con=sqlite3.connect('films.db')
	cur=con.cursor()
	result=cur.execute("SELECT * FROM films")
	films=cur.fetchall()
	print (films[1])
	g=randint(0,18)
	lis=np.array(["https://i1.sndcdn.com/artworks-000176843744-xziit4-t500x500.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTX4LnK6D_5QktwRbYyqlehBwmcZGe7CTPnW48F5i4XIjPrIW5L&usqp=CAU","https://avatars.mds.yandex.net/get-kinopoisk-post-img/1101236/b9d786fdf574c0eecce07dd8b2284dec/960x540","https://memepedia.ru/wp-content/uploads/2019/04/d5un4m5ueaaxcyd.jpg","https://sun1-92.userapi.com/AehpcPXc-CZ9lHQ_cwHtwT1d0gmo_IBOMlkqZQ/RH1GcA74lFg.jpg","https://sun1-20.userapi.com/kjGcNl9x0DIyMulao9iw0SXI3rRM5yvW4CxdOw/19obXHu3a4U.jpg","https://sun9-53.userapi.com/c858432/v858432672/1ebbe1/X4ggLyFPT_c.jpg","https://sun1-91.userapi.com/B83jvYdMAw0wOxtZp0PUnw4k16ThPai7sAzVvA/2En3W5QIBUI.jpg","https://sun9-41.userapi.com/c857220/v857220244/162be8/cc-1wEQTcl0.jpg","https://sun1-85.userapi.com/9QXjsYFAgDCQdZSUnMhMo-q-tKmLkYinnQjzsA/3flv79GieLE.jpg","https://sun9-62.userapi.com/c857036/v857036907/de0c5/lL7niJTt0gg.jpg","https://sun9-6.userapi.com/c540100/v540100747/5bc90/j_j5EQOHXos.jpg","https://sun9-63.userapi.com/c857436/v857436539/16c7a9/okXqYhuqgvI.jpg","https://sun9-46.userapi.com/c857220/v857220795/cdcaa/XeZzrk_zUpY.jpg","https://sun1-20.userapi.com/DSpt6dqNlZ2rNhXDJ7LYNRpW_tK4isLS1qekSg/r-HobLzJMGE.jpg","https://sun9-31.userapi.com/c850624/v850624637/1d282f/P7TAR6Vu1wA.jpg","https://sun9-69.userapi.com/c852016/v852016490/1d0263/LQdHa6f6UxU.jpg","https://sun9-63.userapi.com/c853428/v853428490/f463d/rmNFb2rytCg.jpg","https://sun9-38.userapi.com/c857528/v857528771/23e56/ueRZV7Sb8pI.jpg","https://sun9-8.userapi.com/c849536/v849536085/1c4b81/ynBwqgaIDYI.jpg","https://sun9-53.userapi.com/c849332/v849332598/16e731/9q83GUW2rMM.jpg","https://sun9-31.userapi.com/c851528/v851528691/cf299/_04ZSMLzOXs.jpg","https://sun9-40.userapi.com/c834304/v834304761/14d776/MvKBSNgpBzI.jpg","https://sun9-63.userapi.com/c846420/v846420824/10dbdd/3-bppDTkcw8.jpg","https://sun9-55.userapi.com/c830108/v830108824/1b291c/l6nheUtc3qE.jpg","https://sun9-17.userapi.com/c845323/v845323797/356f6/_zpbb2Iv98I.jpg","https://sun9-31.userapi.com/c841126/v841126861/805dd/djIN3WAMsOY.jpg"])
	for i in range (len (lis)):
		if i==g:
			x=lis[i]
	return render_template('film.html', films=films, x=x )
	cur.close()



@app.route('/film/<film_name>', methods=['GET', 'POST'])
def film_info(film_name):
	# post = Cinema.query.filter_by(name=film_name).first_or_404()
	# form = CommentsForm()
	# users = User
	# user_comment = Comments.query.all()
	# if form.validate_on_submit():
	#     add_comment = Comments(body=form.text.data, user_id=current_user.id)
	#     db.session.add(add_comment)
	#     db.session.commit()
	con=sqlite3.connect('films.db')
	cur=con.cursor()
	nam=film_name
	print (nam)
	print (type(nam))
	result=cur.execute("SELECT * FROM films WHERE nam=?", [nam])
	print (result)
	data= cur.fetchone()
	print ("hello gordon")
	print (data)
	g=randint(0,18)
	lis=np.array(["https://i1.sndcdn.com/artworks-000176843744-xziit4-t500x500.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTX4LnK6D_5QktwRbYyqlehBwmcZGe7CTPnW48F5i4XIjPrIW5L&usqp=CAU","https://avatars.mds.yandex.net/get-kinopoisk-post-img/1101236/b9d786fdf574c0eecce07dd8b2284dec/960x540","https://memepedia.ru/wp-content/uploads/2019/04/d5un4m5ueaaxcyd.jpg","https://sun1-92.userapi.com/AehpcPXc-CZ9lHQ_cwHtwT1d0gmo_IBOMlkqZQ/RH1GcA74lFg.jpg","https://sun1-20.userapi.com/kjGcNl9x0DIyMulao9iw0SXI3rRM5yvW4CxdOw/19obXHu3a4U.jpg","https://sun9-53.userapi.com/c858432/v858432672/1ebbe1/X4ggLyFPT_c.jpg","https://sun1-91.userapi.com/B83jvYdMAw0wOxtZp0PUnw4k16ThPai7sAzVvA/2En3W5QIBUI.jpg","https://sun9-41.userapi.com/c857220/v857220244/162be8/cc-1wEQTcl0.jpg","https://sun1-85.userapi.com/9QXjsYFAgDCQdZSUnMhMo-q-tKmLkYinnQjzsA/3flv79GieLE.jpg","https://sun9-62.userapi.com/c857036/v857036907/de0c5/lL7niJTt0gg.jpg","https://sun9-6.userapi.com/c540100/v540100747/5bc90/j_j5EQOHXos.jpg","https://sun9-63.userapi.com/c857436/v857436539/16c7a9/okXqYhuqgvI.jpg","https://sun9-46.userapi.com/c857220/v857220795/cdcaa/XeZzrk_zUpY.jpg","https://sun1-20.userapi.com/DSpt6dqNlZ2rNhXDJ7LYNRpW_tK4isLS1qekSg/r-HobLzJMGE.jpg","https://sun9-31.userapi.com/c850624/v850624637/1d282f/P7TAR6Vu1wA.jpg","https://sun9-69.userapi.com/c852016/v852016490/1d0263/LQdHa6f6UxU.jpg","https://sun9-63.userapi.com/c853428/v853428490/f463d/rmNFb2rytCg.jpg","https://sun9-38.userapi.com/c857528/v857528771/23e56/ueRZV7Sb8pI.jpg","https://sun9-8.userapi.com/c849536/v849536085/1c4b81/ynBwqgaIDYI.jpg","https://sun9-53.userapi.com/c849332/v849332598/16e731/9q83GUW2rMM.jpg","https://sun9-31.userapi.com/c851528/v851528691/cf299/_04ZSMLzOXs.jpg","https://sun9-40.userapi.com/c834304/v834304761/14d776/MvKBSNgpBzI.jpg","https://sun9-63.userapi.com/c846420/v846420824/10dbdd/3-bppDTkcw8.jpg","https://sun9-55.userapi.com/c830108/v830108824/1b291c/l6nheUtc3qE.jpg","https://sun9-17.userapi.com/c845323/v845323797/356f6/_zpbb2Iv98I.jpg","https://sun9-31.userapi.com/c841126/v841126861/805dd/djIN3WAMsOY.jpg"])
	for i in range (len (lis)):
		if i==g:
			x=lis[i]
	return render_template('film_info.html', file=data , x=x)
	cur.close()




# @app.route('/add_films', methods=['GET','POST'])
# def add_article():
# 	# form=ArticleForm(request.form)
# 	# if request.method=='POST' and form.validate():
# 	# 	title=form.title.data
# 	# 	body=form.body.data

# 	# 	cur=mysql.connection.cursor()

# 	# 	cur.execute("INSERT INTO articles(title,body,author) VALUES(%s,%s,%s)", (title,body,session['username']))

# 	# 	mysql.connection.commit()

# 	# 	cur.close

# 	# 	flash ('Thanks for your review','success')

# 	# 	return redirect(url_for('dashboard'))	

# 	return render_template('add_article.html', form=form)





#@app.route('/film/<film_name>')
#def film_info(film_name):
#    post = thea.query.filter_by(name=film_name).first_or_404()
#    return render_template('film_info.html', post=post)



class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username=StringField('Username', [validators.Length(min=3, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password= PasswordField('Password', [
			validators.DataRequired(),
			validators.EqualTo('confirm', message="Passwords should match each over, bro")
	])
	confirm = PasswordField('Confirm Your Epic Password')


@app.route('/register', methods=['GET','POST'])
def register():
	form=RegisterForm(request.form)
	if request.method=="POST" and form.validate():
		name=form.name.data
		email=form.email.data
		username=form.username.data
		password=sha256_crypt.encrypt(str(form.password.data))

		#cursor
		cur=mysql.connection.cursor()

		cur.execute("INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)", (name, email, username, password))

		#commit to DB
		mysql.connection.commit()

		#close con
		cur.close()

		flash('YOU ARE NOW REGISTERED INTO OUR POWERFUL NETWORK', 'nicely done')
		return redirect (url_for('index'))

	return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
	if request.method=='POST':
		username=request.form['username']
		password_candidate=request.form['password']
		
		cur=mysql.connection.cursor()

		result=cur.execute("SELECT * FROM users WHERE username = %s", [username])
		if result > 0: 
			# get stored hash
			data= cur.fetchone()
			password= data['password']

			# compare passwords

			if sha256_crypt.verify(password_candidate, password):
				#app.logger.info('PASSWORD MATCHED')
				#passes
				session['logged_in']=True
				session['username']=username

				flash ('Welcome , user', 'success')
				return redirect(url_for('dashboard'))		
			else: 
				#app.logger.info('NO USER')
				error='Invalid login'
				return render_template('login.html', error=error)
			#close connection
			cur.close()
		else:
			error='Username not found'
			return render_template('login.html', error=error )


	return render_template('login.html')


def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash ('UwU, you should authorise', 'danger')
			return redirect(url_for('login'))
	return wrap



@app.route('/logout')
@is_logged_in
def logout():
	session.clear()
	flash ("You are logged out", "success")
	return redirect(url_for('login'))



#dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
	cur = mysql.connection.cursor()

	result=cur.execute("SELECT * FROM articles")

	articles=cur.fetchall()

	if result > 0:
		return render_template('dashboard.html', articles=articles)
	
	else:
		msg = "No articles Found"
		return render_template('dashboard.html', msg=msg)

	cur.close()

class ArticleForm(Form):
	title = StringField('Title', [validators.Length(min=1, max=200)])
	body=TextAreaField('Body', [validators.Length(min=30)])


#add article
@app.route('/add_article', methods=['GET','POST'])
@is_logged_in
def add_article():
	form=ArticleForm(request.form)
	if request.method=='POST' and form.validate():
		title=form.title.data
		body=form.body.data

		cur=mysql.connection.cursor()

		cur.execute("INSERT INTO articles(title,body,author) VALUES(%s,%s,%s)", (title,body,session['username']))

		mysql.connection.commit()

		cur.close

		flash ('Thanks for your review','success')

		return redirect(url_for('dashboard'))	

	return render_template('add_article.html', form=form)



#edit article
@app.route('/edit_article/<string:id>', methods=['GET','POST'])
@is_logged_in
def edit_article(id):
	cur=mysql.connection.cursor()

	#get article by id
	result = cur.execute("SELECT * FROM articles WHERE id =%s" , [id])

	article= cur.fetchone()

	#get form

	form=ArticleForm(request.form)


	#populat article from fields

	form.title.data=article['title']
	form.body.data=article['body']

	if request.method=='POST' and form.validate():
		title=request.form['title']
		body=request.form['body']

		cur=mysql.connection.cursor()

		cur.execute("UPDATE articles SET title=%s, body=%s WHERE id=%s" , (title,body,id))
		mysql.connection.commit()

		cur.close



		flash ('Article updated','success')

		return redirect(url_for('dashboard'))	

	return render_template('edit_article.html', form=form)

#delete
@app.route('/delete_article/<string:id>' , methods=['POST'])
@is_logged_in
def delete_article(id):
	cur = mysql.connection.cursor()

	cur.execute("DELETE FROM articles WHERE id=%s", [id])

	mysql.connection.commit()
	cur.close()

	flash ('Article has been deleted !!', 'success')
	return redirect(url_for('dashboard'))





if __name__ =="__main__":
	app.secret_key="D@nil@2001"
	app.run(debug=True)