import requests
from bs4 import BeautifulSoup
import ConfigParser
import re
import datetime

setting_file="config/config.txt"
configs=ConfigParser.ConfigParser()
configs.readfp(open(setting_file))

payload = {
	
	'username': 'dinomorea123',
	'password': 'Aa0@Aa0@',
	'recaptcha': 0,
	'?':None
}

print("****** LIKE4LIKE PARSER ******")

fw =  open('retweets/retweets_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv','a+')

print('Using Credentials:' + str(payload))

session=requests.Session()
headers = {
	'authority': 'www.like4like.org',
	'method': 'POST',
	'accept': 'application/json, text/javascript, */*; q=0.01',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	'content-length': '52',
	'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'origin': 'https://www.like4like.org',
	'referer': 'https://www.like4like.org/login/',
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest'
}

r=session.post('https://www.like4like.org/api/login.php', data=payload, headers=headers)
print(r.content)
# headers={"authority":"www.like4like.org",
# 		 "method":"GET",
# 		 "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# 		 "accept-encoding":"gzip",
# 		 "upgrade-insecure-requests": "1",
# 		 "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
# print(r.json())

# headers = {
# 			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#            'X-Requested-With': 'XMLHttpRequest',
#            'Authority': 'www.like4like.org',
#            'Referer': 'https://www.like4like.org/user/earn-twitter-retweet.php',
#            }
# cookies = dict(cookies_are='working')
# params={'feature': 'twitterret'}
# userProfile = session.get("http://www.like4like.org/api/get-tasks.php", params=params, headers=headers)
# print(userProfile.json())


# soup = BeautifulSoup(r.content, 'html.parser')
# rtDiv = soup.find_all("table", {"id": "facebook-earn-table-01"})

# print(rtDiv)

