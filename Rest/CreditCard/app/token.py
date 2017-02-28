from django.conf import settings
import jwt

class Token(object):
    def getToken(self, user):
        token = jwt.encode({'some': 'payload'}, settings.SECRET_KEY, algorithm='HS256')
        print token
