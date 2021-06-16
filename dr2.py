try:
	
    import sys
    from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from time import sleep
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.common.exceptions import TimeoutException
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.select import Select 

    try:
        link = sys.argv[1]
    except:
        link = "https://teams.microsoft.com/l/meetup-join/19:681e3cecf70a46fc8be07fe92127fd9e@thread.tacv2/1620712621454?context=%7B%22Tid%22:%220eb94f32-b0f4-49a2-b2ff-7076d8269975%22,%22Oid%22:%2242341697-6cdc-4c93-91eb-2d17e278198f%22%7D"

	chrome_options = Options()
	chrome_options.add_argument("--use-fake-ui-for-media-stream")
	chrome_options.add_argument("--headless")

	driver = webdriver.Chrome(options = chrome_options)

	

	driver.get(link)


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
