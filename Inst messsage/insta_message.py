# python -m pip install selenium
# python.exe -m pip install --upgrade pip
from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

# Username and password of your instagram account:
my_username = 'username'
my_password = 'password'

# Instagram username list for DM:
usernames = ['user1', 'user2', 'user3']

# Messages:
messages = ['Hey! Pls follow my page', 'Hey, how you doing?', 'Hey']

# Delay time between messages in sec:
between_messages = 2000

#browser = webdriver.Chrome('chromedriver')
#driver = webdriver.Chrome('chromedriver')
driver = webdriver.Chrome(executable_path="C:\\Users\Abhishek Sharma\\OneDrive\Desktop\\ICT Sem 3\\Programming with Python\\Project\\Program\\chromedriver")
#driver = webdriver.Edge(executable_path="C:\\Users\Abhishek Sharma\\OneDrive\Desktop\\ICT Sem 3\\Programming with Python\\Project\\Program\\msedgedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\Abhishek Sharma\\OneDrive\Desktop\\ICT Sem 3\\Programming with Python\\Project\\Program\\geckodriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\Abhishek Sharma\\OneDrive\Desktop\\ICT Sem 3\\Programming with Python\\Project\\Program\\setup-stub.exe")

# Authorization:
def auth(username, password):
	try:
		driver.get('http://instagram.com')
		time.sleep(random.randrange(1,2))
		#sleep(10000)

		input_username = driver.find_element_by_name('username')
		input_password = driver.find_element_by_name('password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		#driver.quit()
  
auth(my_username, my_password)