from django.conf import settings
import jwt, datetime

secsRefresh = 240
secsExpired = 300

class Token(object):

    @staticmethod
    def valToken(token):
        return jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def refresh(token):
        data = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
        limit = datetime.datetime.utcfromtimestamp(data['iat']) + datetime.timedelta(seconds=secsRefresh)
        delta = limit - datetime.datetime.utcnow()
        if delta.days != -1:
            return False
    
        token = jwt.encode({
            'user': data['user'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=secsExpired),
            'iat': datetime.datetime.utcnow()
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

    @staticmethod
    def getToken(user):
        token = jwt.encode({
            'user': user['user'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=secsExpired),
            'iat': datetime.datetime.utcnow()
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
