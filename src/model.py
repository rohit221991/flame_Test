from google.appengine.ext import db
from constants import *
import logging
import datetime
import time



def image_key(name="default"):
    return db.Key.from_path('images', name)

class Image(db.Model):
    mall_id = db.IntegerProperty()
    image = db.BlobProperty()
    
    @classmethod
    def by_id(cls, uid):
        return cls.get_by_id(uid, parent=image_key()).image
    
    @classmethod
    def save(self , image):
        try:
            return Image(parent=image_key(), image = image)
        except:
            logging.info("Image save failed")
            return
    

def mall_key(name="default"):
    return db.Key.from_path('malls', name)

class Mall(db.Model):
    city = db.StringProperty(required = True, choices=set(cities))
    name = db.StringProperty(required = True)
    lowest_floor = db.IntegerProperty(required = True)
    highest_floor = db.IntegerProperty(required = True)
    image1 = db.LinkProperty(required = True)
    image2 = db.LinkProperty()
    image3 = db.LinkProperty()
    image4 = db.LinkProperty()
    comment = db.TextProperty()
    location = db.GeoPtProperty()
    address = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    
    @classmethod
    def by_id(cls, uid):
        return cls.get_by_id(uid, parent=mall_key())
    
    @classmethod
    def by_name(cls, name):
        return cls.all().filter("name =", name) 
        
    @classmethod
    def save(self, city, name, lowest_floor, highest_floor, address,
             image1,image2 = None, image3 = None, image4=None, comment=None):
        return Mall(parent=mall_key(), city = city, 
                    name = name, lowest_floor = lowest_floor, 
                    highest_floor = highest_floor, address= address, 
                    image1 = image1, 
                    image2 = image2, image3 = image3, image4 = image4,
                    comment = comment)