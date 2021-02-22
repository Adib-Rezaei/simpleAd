from BaseAdvertising import BaseAdvertising
from Advertiser import Advertiser

class Ad(BaseAdvertising):
    'Ad class'
    id = 1

    def __init__(self, title, imgUrl, link, advertiser):
        super().__init__()
        self.__id = Ad.id
        self.__title = title 
        self.__imgUrl = imgUrl 
        self.__link = link 
        self.__advertiser = advertiser
        Ad.id += 1

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getImgUrl(self):
        return self.__imgUrl
    
    def setImgUrl(self, img):
        self.__imgUrl = img

    def getLink(self):
        return self.__link

    def setLink(self, link):
        self.__link = link 

    def setAdvertiser(self, advertiser):
        self.__advertiser = advertiser


    # override
    def incClicks(self):
        super().incClicks()
        self.__advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.__advertiser.incViews()

    def describeMe(self):
        return self.__doc__