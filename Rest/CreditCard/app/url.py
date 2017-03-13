class Urls(object):

    safeUrls = [
        '/usuarios/auth/'
    ]

    def __init__(self, url):
        self.url = url

    @property
    def isSafe(self):
        if self.url in self.safeUrls:
            return True

        return False
