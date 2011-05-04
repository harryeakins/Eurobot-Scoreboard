from google.appengine.ext import db

class Team(db.Model):
    name = db.StringProperty(multiline=False,required=True)
    user = db.UserProperty()
    regdate = db.DateTimeProperty(auto_now_add=True,required=True)

class Match(db.Model):
    red = db.ReferenceProperty(Team,collection_name='redmatches')
    rednormal = db.IntegerProperty()
    redbonus = db.IntegerProperty()
    blue = db.ReferenceProperty(Team,collection_name='bluematches')
    bluenormal = db.IntegerProperty()
    bluebonus = db.IntegerProperty()
    nulled =db.BooleanProperty()
    regdate = db.DateTimeProperty(auto_now_add=True,required=True)
