from BaseAdvertising import BaseAdvertising

class Advertiser(BaseAdvertising):
    'This is Advertiser class'
    id = 1
    totalClicks = 0
    
    def __init__(self, name):
        super().__init__()
        self.__name = name 
        self.__id = Advertiser.id
        Advertiser.id += 1

    def getName(self):
        return self.__name 

    def setName(self, name):
        self.__name = name

    def incClicks(self):
        Advertiser.totalClicks += 1
        super().incClicks()

    @staticmethod
    def help():
        return 'This class has some fields'

    def describeMe(self):
        return self.__doc__

    @staticmethod
    def getTotalClicks():
        return Advertiser.totalClicks


