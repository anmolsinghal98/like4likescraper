import requests
import ConfigParser
import re
import datetime
import contextlib
from bs4 import BeautifulSoup

setting_file="config/config.txt"
configs=ConfigParser.ConfigParser()
configs.readfp(open(setting_file))

payload = {
	
	'username': configs.get('Credentials','username'),
	'password': configs.get('Credentials','password')
}

print("****** LIKE4LIKE PARSER ******")

fw =  open('likes/likes_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv','a+')

print('Using Credentials:' + str(payload))

Session=requests.session()
r=Session.post('https://www.like4like.org/api/login.php',data=payload)

print(r)

tweetCounter=0

likesPageContent = Session.get("https://www.like4like.org/user/earn-twitter-favorites.php").content

tweetPoints=re.findall('<span id="value-credits.*</span>',likesPageContent)

for x in tweetPoints:
	print(x)

