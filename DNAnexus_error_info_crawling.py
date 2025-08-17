from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

path = '/Users/jeonghyein/chromedriver-mac-arm64'
service = Service(executable_path=path)
browser = webdriver.Chrome(service=service)
url = 'https://ukbiobank.dnanexus.com/projects/GfX9fx8JF433z4FFqGb0X7Bx/monitor'
browser.get(url)


button_xpath = '/html/body/div[2]/div/section/div/div[1]/div/div[2]/div[3]/button[2]'
login = browser.find_element(By.XPATH,button_xpath)
login.click()


email_xpath = '/html/body/div[2]/div/div[1]/div/div/div[3]/div[1]/form/div[1]/div[2]/input'
email_field = browser.find_element(By.XPATH, email_xpath)
user_email = 'Hyein'
email_field.send_keys(user_email)
next = browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[3]/div[1]/form/div[2]/button').click()

password_field = browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[3]/div[1]/form/div[1]/div[3]/input')
password = 'XOXOmcmc0617!'
password_field.send_keys(password)
browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[3]/div[1]/form/div[2]/button').click()


name = '/html/body/div[2]/div/div[1]/div/div/div/div/section/div[2]/div/div/ul[1]/li[3]/div[1]/div[1]'
browser.find_element(By.XPATH,name).click()





########
for i in chr1_error:
  name = '/html/body/div[2]/div/div[1]/div/div/div/div/section/div[2]/div/div/ul[1]/li[3]/div[1]/div[1]'
	browser.find_element(By.XPATH,name).click()
	time.sleep(3)
	s = "/chr1_extract_pgen_b" + str(i) + "$/"
	inp = '/html/body/div[2]/div/div[1]/div/div/div/div/section/div[2]/div/div/ul[1]/li[3]/div[2]/div[1]/div/div[2]/div/ul/li[2]/input'
	browser.find_element(By.XPATH,inp).send_keys(s)
	browser.find_element(By.XPATH,inp).send_keys(Keys.ENTER)
	time.sleep(20)
	job_state='/html/body/div[2]/div/div[1]/div/div/div/div/section/div[3]/div[1]/div[2]/table/tbody/tr/td[1]/span'
	job_state_string = browser.find_element(By.XPATH,job_state)
	state = job_state_string.text
	if (state == 'Done'):
		next
	else:
		jobs_path = '/html/body/div[2]/div/div[1]/div/div/div/div/section/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a[1]'
		job = browser.find_element(By.XPATH,jobs_path)
		file_path = dir + '/' + job.text + '_error.txt'
		href = job.get_attribute('href')
		browser.execute_script("window.open(arguments[0]);", href)
		time.sleep(20)
		log = '/html/body/main/div/article/section/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/button'
		original_window = browser.window_handles[0]
		window_handle = browser.window_handles[1]
		browser.switch_to.window(window_handle)
		browser.find_element(By.XPATH,log).click()
		time.sleep(10)
		info_checkbox = '/html/body/main/div/article/section/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/label[3]/input'
		info_checkboxes = browser.find_elements(By.XPATH,info_checkbox)
		if len(info_checkboxes)>0:
			stdout_checkbox = '/html/body/main/div/article/section/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/label[1]/input'
			browser.find_element(By.XPATH,info_checkbox).click()
			time.sleep(3)
			browser.find_element(By.XPATH,stdout_checkbox).click()
			time.sleep(3)
			ele = browser.find_element(By.XPATH,'/html/body/main/div/article/section/div[1]/div[2]/div/div[2]/div')
			with open(file_path,'w') as file:
				file.write(ele.text)
				print(ele.text)
			browser.close()
			browser.switch_to.window(original_window)
		
		else:
			with open(file_path,'w') as file:
				file.write("No log")
			browser.close()
			browser.switch_to.window(original_window)
		
