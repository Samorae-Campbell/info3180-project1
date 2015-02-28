"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, Flask, jsonify
from app import db
from app.models import User
import os
import time
from werkzeug import secure_filename
import json

from .forms import EmailPasswordForm

#app.config['SECRET_KEY'] = "mypast"




###
# Routing for your application.
###


@app.route('/jsonify_thing')
def jsonify_thing():
   # print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
    print json.dumps({'username':'username', 'email':'email', 'id':2}, sort_keys=True)
    return "hi"+json.dumps({'username':'username', 'email':'email', 'id':2}, sort_keys=True)

@app.route('/profile', methods=["GET", "POST"])
def add():
  form = EmailPasswordForm(csrf_enabled=False)
  if request.method == "POST":
      filefolder = './app/static/img'
      fname =  str(form.fname.data)
      lname =  str(form.lname.data)
      email =  str(form.email.data)
      age =  form.age.data
      sex =  str(form.sex.data)
      img = request.files['image'];
      image = secure_filename(img.filename)
      image_1 = os.path.join(filefolder, image)
      img.save(image_1)
      Alex = User(fname,lname,email,sex,age,image)
      #allie = User.query.filter_by(first_name='Samorae').first()
      #print allie
      db.session.add(Alex)
      db.session.commit()
      print fname, lname, email, age, sex, image
      #email = request.form['email']
      #print email
      print image
      return render_template('added.html', fname=fname, lname=lname)

  return render_template('profile.html', form=form)



@app.route('/profiles')
def profiles():
  allie = db.session.query(User).all()
  #print allie[2]
  #print len(allie)
  #print jsonify(firstname='hi')
  lst = []
  #a =json.dumps({'username':'%r', 'email':'email', 'id':2}, sort_keys=True) % str(allie[0].first_name)
  #b =json.dumps({'username':'%r', 'email':'email', 'id':2}, sort_keys=True) % str(allie[0].first_name)
  #lst = [a]
  #lst+= [b]
  #print lst
  #lst+= jsonify(first_name=allie[0].first_name)
  #return render_template('show_profiles.html', profile_list=lst)
  if (request.headers['Content-Type'] == 'application/json'):
      for x in range(0, len(allie)):
        temp =json.dumps({'UserID':'%d', 'First Name':'%r', 'Last Name':'%r', 'Email':'%r', 'Sex':'%r', 'Age':'%d', 'Image':'%r', 'Highscore':'%d', 'Tdollars':'%d',}, sort_keys=True) % ( allie[x].age, str(allie[x].email), str(allie[x].first_name), allie[x].hscore, str(allie[x].image), str(allie[x].last_name), str(allie[x].sex), allie[x].tdollars, allie[x].id)
        lst+= [temp]
        
      return render_template('show_profiles_json.html', profile_list=lst)
    
  else:
    
    return render_template('show_profiles.html', profile_list=allie)
    
    
@app.route('/profile/<userid>')
def profile(userid):
  #import pdb;pdb.set_trace()
  allie = User.query.filter_by(id=userid).first()
  
  if (request.headers['Content-Type'] == 'application/json'):
    return jsonify(UserID=allie.id, First_Name=allie.first_name, Last_Name=allie.last_name, Email=allie.email, Sex=allie.sex, Age=allie.age, Image=allie.image, Tdollars=allie.tdollars, Highscores=allie.hscore)
  else:
  
  #print allie.first_name
  #print allie.image
  
  #return "<html><head><title>Sam</title></head> <body><img src=%s/></body></html>" % allie.image
     return render_template('show_profile.html', time = timeinfo(), first_name=allie.first_name, last_name = allie.last_name, email=allie.email, sex=allie.sex, age=allie.age, image=allie.image, id=allie.id, tdollars=allie.tdollars, hscore=allie.hscore)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
  
@app.route('/person')

def person():
  first_user = db.session.query(User).first()
  return "First Name: {} Last Name: {} Email: {} sex: {} Age: {} mage: {}".format(first_user.first_name, first_user.last_name, first_user.email, first_user.sex, first_user.age, first_user.image,)

def timeinfo():
  now = time.strftime("%c")
  # now = "Time: "+time.strftime("%I:%M:%S")+" "+time.strftime("%A %d/%m/%Y")
  now = "Date: "+time.strftime("%A %d/%b/%Y")
  # name = "Samorae"
  # 12-hr time format -- print (time.strftime("%I:%M:%S"))
  # 12-hr time format -- print (time.strftime("%d/%m/%Y"))
  # return render_template('profile.html', name=name)
  return now


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
