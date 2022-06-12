# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pause
import datetime
import multiprocessing
from seleniumwire import webdriver

def loginNike(usemail,uspasswd):
	login = driver.find_element_by_xpath("//button[contains(text(), 'Join/Log In')]")
	driver.execute_script("arguments[0].click();", login)

	email = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[2]/input')
	passwd = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[3]/input')
	email.send_keys(usemail)
	passwd.send_keys(uspasswd+Keys.RETURN)

	try:
		while wait2.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div'))) :
			if EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div')) :
				driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[2]/input').click()
				passwd = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[3]/input')
				passwd.send_keys('Passnikewise23'+Keys.RETURN)
				print('inside loop')
	except:
		print('logged in')

def clickSize(sizerun):
	try:
		size = driver.find_element_by_xpath('//*[contains(text(),"US '+sizerun+'") and @class="size-grid-dropdown size-grid-button"]')
		driver.execute_script("arguments[0].click();", size)
	except:
		print("No size")

def addToBag():
	try:
		# newaddbag = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section/div[2]/aside/div/div[2]/div/button')
		newaddbag = driver.find_element_by_xpath("//button[contains(text(), 'Buy')]")
		newaddbag.click()
	except:
		print('some addbag fail')

def checkOut(cr):
	cardno = cr[0]
	mmyy = cr[1]
	cvv = cr[2]
	act = ActionChains(driver)
	tab = 4

	wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/esw-root/div/section/esw-checkout/div/esw-payment-details/div/div[1]/div[1]/div')))
	print('inserting CC')
	iframe = driver.find_element_by_xpath('/html/body/esw-root/div/section/esw-checkout/div/esw-payment-details/div/div[2]/div[1]/esw-stored-cards-list/div/div/esw-new-card/div/div/esw-payment-iframe/div/iframe')
	driver.switch_to.frame(iframe)
	wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/body/div/app-new-payment-card-form/div/form/div/div[1]/input')))
	driver.switch_to.default_content()

	act.send_keys(Keys.TAB * tab)
	act.send_keys(cardno + Keys.TAB)
	act.send_keys(mmyy + Keys.TAB)
	act.send_keys(cvv)
	act.perform()

	driver.find_element_by_class_name('button-continue').send_keys(Keys.RETURN)

	print('checkout ready')
	#pause.until(datetime.datetime(2021,1,22,9,59,58))
	try:
		while EC.presence_of_element_located((By.CLASS_NAME, 'button-submit')) :
			submit = driver.find_element_by_class_name('button-submit')
			driver.execute_script("arguments[0].click();", submit)
	except:
		print('Submitted')

def interceptor(request):
    del request.headers['Referer']  # Delete the header first
    request.headers['Referer'] = 'some_referer'


def newProc(usr,psswrd,sizerun,cr):
	global driver, wait, wait2

	driver = webdriver.Chrome(executable_path='./chromedriver.exe')
	driver.request_interceptor = interceptor
	driver.minimize_window()
	wait = WebDriverWait(driver, 60)
	wait2 = WebDriverWait(driver, 5)

	driver.get(url)
	loginNike(usr,psswrd)

	pause.until(datetime.datetime(2021,2,4,9,59,58))

	wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"US '+sizerun+'") and @class="size-grid-dropdown size-grid-button"]')))
	clickSize(sizerun)

	wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Buy')]")))
	addToBag()

	wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/esw-root/div/section/esw-checkout/div/esw-payment-details/div/div[1]/div[1]/div')))
	print('Entering Checkout Page')
	checkOut(cr)


credit = [
 	["4242424242424242", "4242", "424"],
 	["4242424242424242", "4242", "424"],
]

user = [
	"youremailhere@gmail.com",
	"youremailhere@gmail.com",
	"youremailhere@gmail.com",
]

sz = [
	"9",
	"9",
	"9",
]

crchoice = [
	credit[1],
	credit[2],
	credit[3],

]

password = "YourPasswordHere"

# tab = int(input("Input How Many Tab: "))
# url = input("Input URL: ")
url = "https://www.nike.com/id/launch/t/cosmic-unity-floral"

processes = []

for x in range(3):
	p = multiprocessing.Process(target=newProc,args=[user[x],password, sz[x], crchoice[x]])
	if __name__ == "__main__":
		p.start()
		processes.append(p)

for p in processes:
	p.join()
