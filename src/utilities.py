from model import *
import logging
import os

def save_image(image):
    if not image:
        logging.info('null image')
        return None, None
    img =  Image.save(db.Blob(image))
    img.put()
    id = img.key().id()
    link = db.Link("http://"+ os.environ['HTTP_HOST'] + "/img/" + str(id))
    logging.info("Image: " + image)
    logging.info(link)
    return link, img


SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)

def to_dict(model):
    output = {}

    for key, prop in model.properties().iteritems():
        value = getattr(model, key)

        if value is None or isinstance(value, SIMPLE_TYPES):
            output[key] = value
        elif isinstance(value, datetime.date):
            # Convert date/datetime to MILLISECONDS-since-epoch (JS "new Date()").
            ms = time.mktime(value.utctimetuple()) * 1000
            ms += getattr(value, 'microseconds', 0) / 1000
            output[key] = int(ms)
        elif isinstance(value, db.GeoPt):
            output[key] = {'lat': value.lat, 'lon': value.lon}
        elif isinstance(value, db.Model):
            output[key] = to_dict(value)
        else:
            raise ValueError('cannot encode ' + repr(prop))

    return output