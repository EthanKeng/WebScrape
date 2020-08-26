from selenium import webdriver
import time

#this is for stopping the popup notification
#-------------------
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
#-------------------
#put the chrom_options in the argument
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/Users/jojo7/xxxx')

#Navigate to the website
driver.get("https://www.facebook.com")




time.sleep(2)
driver.close()
