from BaseAdvertising import BaseAdvertising
from Advertiser import Advertiser
from Ad import Ad

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser("name1")
advertiser2 = Advertiser('name2')

ad1 = Ad('title1', 'img1','link1', advertiser1)
ad2 = Ad('title2', 'img2','link2', advertiser2)

print(baseAdvertising.describeMe())
print(ad2.describeMe())
print(advertiser1.describeMe())

ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad2.incViews()
ad1.incClicks()
ad1.incClicks()
ad2.incClicks()
print(advertiser2.getName())
advertiser2.setName("new name")
print(advertiser2.getName())
print(ad1.getClicks())
print(advertiser2.getClicks())
print("Advertisers Total clicks: ", Advertiser.getTotalClicks())
print(Advertiser.help())