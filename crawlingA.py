from bs4 import BeautifulSoup
import time
import selenium
from selenium import webdriver
import sys
import requests

i = sys.argv[1]

options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver',options=options)


header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

url = 'https://www.mayoclinic.org/'


driver.get(url)
time.sleep(3)
driver.find_element("xpath",'/html/body/form/div[6]/article/div[1]/div[1]/div/div/div/div/section/div[2]/div/div/a[3]/span').click()
time.sleep(3)
driver.find_element("xpath",'/html/body/form/div[6]/div[1]/nav[3]/ul/li[2]/a').click()
time.sleep(3)
driver.find_element("xpath",'/html/body/form/div[6]/div[2]/div[4]/div[1]/div/div/ol/li[1]/a').click()
time.sleep(3)

# A click
driver.find_element("xpath",'/html/body/form/div[6]/div[2]/div[4]/div[1]/div/div/ol/li[1]/div/span/div/ol/li[1]/a/span[2]').click()
time.sleep(3)

xpth = '/html/body/form/div[6]/div[2]/div[4]/div[2]/ol/li['+i+']/a'
#A disease click
driver.find_element("xpath",xpth).click()

#data parsing

new_url = driver.current_url
response = requests.get(new_url,headers=header)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html,'html.parser')



check = soup.select("#main-content > div:nth-child(1) > div.content > div:nth-child(2) > h2:nth-child(1)")


if(len(check) == 1):
	all = soup.select("#main-content > div:nth-child(1) > div.content > div:nth-child(2) > :nth-child(n)")
	ind = 2
else:
	all = soup.select("#main-content > div:nth-child(1) > div.content > div:nth-child(3) > :nth-child(n)")
	ind = 3

for i in range(len(all)):
	if(all[i].name == 'h2'or all[i].name == 'p'or all[i].name=='h3' or all[i].name=='h4'):
		print(all[i].get_text())
		print()
	elif(all[i].name == 'ul'):
		n = i+1
		n = str(n)
		ind = str(ind)
		ul_css = '#main-content > div:nth-child(1) > div.content > div:nth-child('+ind+') > ul:nth-child('+n+') > li:nth-child(n)'
		li = soup.select(ul_css)
		for l in li:
			print()
			print(l.get_text())	
			print()
	
	else:
		next
	

#for i in info:
#	print(i.string)	
#print("\n")

#print(title.get_text().strip())
#'/html/body/form/div[6]/div[2]/div[4]/div[2]/ol/li[i]/a'
#print(driver.find_element("xpath",'/html/body/form/div[6]/header/div/h1/a').text)
#print(driver.find_element("xpath",'/html/body/form/div[6]/article/div[1]/div[1]').text)


driver.quit()
