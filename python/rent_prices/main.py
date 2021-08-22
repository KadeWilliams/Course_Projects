from DataScraper import DataScraper
from DataEntryBot import DataEntryBot

LINK = 'https://www.zillow.com/seattle-wa/rentals/1-_beds/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.65550259228516%2C%22east%22%3A-122.03408840771485%2C%22south%22%3A47.47365318155366%2C%22north%22%3A47.7523131081386%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A913943%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22sort%22%3A%7B%22value%22%3A%22featured%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22seattle%22%2C%22customRegionId%22%3A%2269dbe60897X1-CRa2hqhj4nal4u_xmttn%22%2C%22pagination%22%3A%7B%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A16037%2C%22regionType%22%3A6%7D%5D%7D'

ds = DataScraper(LINK)
housing_data = ds.find_housing_data()

deb = DataEntryBot()
deb.enter_data(housing_data)
