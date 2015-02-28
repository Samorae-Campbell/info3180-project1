from . import db

class User(db.Model):

  id =db.Column(db.Integer, primary_key=True)

  first_name = db.Column(db.String(80))
  
  last_name = db.Column(db.String(80))

  email = db.Column(db.String(120))
  
  sex = db.Column(db.String(20))
  
  age = db.Column(db.Integer)
  
  image = db.Column(db.String(200))
  
  hscore = db.Column(db.Integer)
  
  tdollars = db.Column(db.Integer)

  def __init__(self, first_name, last_name, email, sex, age, image):

    self.first_name = first_name
    
    self.last_name = last_name

    self.email = email
    
    self.sex = sex
    
    self.age = age
    
    self.image = image
    
    self.hscore = 0
    
    self.tdollars =0

  def __repr__(self):

    #return '<User %d %r %r %r %r %d %r %d %d>' % (self.id, str(self.first_name), str(self.last_name), str(self.email), str(self.sex), self.age, str(self.image), self.hscore, self.tdollars)
    
    return '(id=%d, first_name=%r, last_name=%r, email=%r, sex=%r, age=%d, image=%r, hscore=%d. tdollars=%d )' % (self.id, str(self.first_name), str(self.last_name), str(self.email), str(self.sex), self.age, str(self.image), self.hscore, self.tdollars)