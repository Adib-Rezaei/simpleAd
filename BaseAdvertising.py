

class BaseAdvertising:
    'Base Advertising class'
    def __init__(self):
        self.clicks = 0
        self.views = 0

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incClicks(self):
        self.clicks += 1

    def incViews(self):
        self.views += 1

    def describeMe(self):
        return self.__doc__