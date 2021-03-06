try:
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from time import sleep
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.common.exceptions import TimeoutException
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.select import Select 



	chrome_options = Options()
	chrome_options.add_argument("--use-fake-ui-for-media-stream")
	# chrome_options.add_argument("--headless")

	driver = webdriver.Chrome(options = chrome_options)

	
#driver.get("https://teams.microsoft.com/l/meetup-join/19%3a0d2df390fa234f5a9a5bb49b469a51bd%40thread.tacv2/1617343574130?context=%7b%22Tid%22%3a%220eb94f32-b0f4-49a2-b2ff-7076d8269975%22%2c%22Oid%22%3a%228a16410b-111b-4034-be41-8666102dbaff%22%7d")

	# 
driver.get("https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_ZWQzMWQ2YmUtODQ0Ni00ZjFhLWFjZjEtZDA5YjQzY2JmZThl%40thread.v2%2F0%3Fcontext%3D%257B%2522Tid%2522%3A%25220eb94f32-b0f4-49a2-b2ff-7076d8269975%2522%2C%2522Oid%2522%3A%25221d9fdd7e-9d89-4323-94e5-bf5fc0123e8d%2522%257Dhttps%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%3Ameeting_ZWQzMWQ2YmUtODQ0Ni00ZjFhLWFjZjEtZDA5YjQzY2JmZThl%40thread.v2%2F0%3Fcontext%3D%257B%2522Tid%2522%3A%25220eb94f32-b0f4-49a2-b2ff-7076d8269975%2522%2C%2522Oid%2522%3A%25221d9fdd7e-9d89-4323-94e5-bf5fc0123e8d%2522%257D&type=meetup-join&deeplinkId=ded2bcd4-b5d7-4ac9-9096-9c8788f842f7&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true")

	# 
driver.get("https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3A681e3cecf70a46fc8be07fe92127fd9e%40thread.tacv2%2F1617427763885%3Fcontext%3D%257b%2522Tid%2522%253a%25220eb94f32-b0f4-49a2-b2ff-7076d8269975%2522%252c%2522Oid%2522%253a%252242341697-6cdc-4c93-91eb-2d17e278198f%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=74e67fa6-60e7-4d9c-bc25-0a2bb8962eb9&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true")


	driver.get("")
	driver.find_element_by_css_selector("button[data-tid=joinOnWeb]").click()

	try:
	    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
	    print("got")
	except TimeoutException:
	    print ("Loading took too much time!")

	driver.find_elements(By.CSS_SELECTOR,"input[name=username]")[0].send_keys("Trojan Horse")



	toggle_camera = driver.find_elements(By.CSS_SELECTOR, "button[ng-disabled=isDisabled]" )[0]

	print(f"Camera is ON: { toggle_camera.get_attribute('aria-pressed') }")

	if toggle_camera.get_attribute("aria-pressed") == "true":
		toggle_camera.click()

	toggle_mic = driver.find_elements(By.CSS_SELECTOR, "button[ng-disabled=isDisabled]" )[1]

	print(f"Mic is ON: { toggle_mic.get_attribute('aria-pressed') }")

	if toggle_mic.get_attribute("aria-pressed") == "true":
		toggle_mic.click()

	sleep(1)


	print(f"Camera is ON: { toggle_camera.get_attribute('aria-pressed') }")
	print(f"Mic is ON: { toggle_mic.get_attribute('aria-pressed') }")


	driver.find_elements(By.CSS_SELECTOR, "button[data-tid=prejoin-join-button]" )[0].click()


	sleep(30)


	driver.close()
except:
	print("closing")
	driver.close()
