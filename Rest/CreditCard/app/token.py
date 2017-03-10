from django.conf import settings
from jwt import DecodeError, ExpiredSignatureError
import jwt, datetime

secsExpired = 300

class Token(object):
    """Clase para obtener token

    Args:
        token (str): Cadena del token
    """
    
    __secsRefresh = int(secsExpired*0.60)

    def __init__(self, token):
        self.__token = token

    @property
    def validate(self):
        """Propiedad para validar si el token ha expirado"""
        try:
            self.__data = jwt.decode(self.__token, settings.SECRET_KEY, algorithm='HS256')
            print self.__data
            return True
        except (DecodeError, ExpiredSignatureError) as e:
            return False

    @property
    def refresh(self):
        """Propiedad para validar si el token se debe refrescar"""
        limit = datetime.datetime.utcfromtimestamp( self.__data['iat'] ) + datetime.timedelta(seconds=self.__secsRefresh)
        delta = limit - datetime.datetime.utcnow()
        if delta.days == -1:
            return True
        return False

    @property
    def new(self):
        """Propiedad que contiene el token refrescado"""
        return Token.getToken(self.__data)

    @staticmethod
    def getToken(user):
        """Metodo para obtener un token valido para cada usuario

        Args:
            user (dict): Datos del usuario que genera el token
        """
        token = jwt.encode({
            'user': user['user'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=secsExpired),
            'iat': datetime.datetime.utcnow()
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
