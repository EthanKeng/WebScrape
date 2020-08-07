from selenium import webdriver
import time

USERNAME = ""
PASSWORD = ""

#this is for stopping the popup notification
#-------------------
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
#-------------------
#put the chrom_options in the argument
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/Users/jojo7/Desktop/Python/Auto_FB_BirthdayWish/chromedriver')
#Navigate to the website
driver.get("https://www.facebook.com")

#Login
user_name_box = driver.find_element_by_id("email")
user_name_box.send_keys(USERNAME)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(PASSWORD)

login_box = driver.find_element_by_id('loginbutton') 
login_box.click()
print("login successful!!!")
time.sleep(3)

#click the load more btn 
left_buttons = driver.find_elements_by_xpath("//div[@data-pagelet='LeftRail']//*[text()='顯示更多']")
left_buttons[0].click()
time.sleep(1)

#click the EVENT for navigating to birthday contents by USING contains(attributeName, keyValue)
event_btn = driver.find_elements_by_xpath("//*[contains(@data-pagelet,'LeftRail')]//*[text()='活動']")
event_btn[0].click()
birthday_btn = driver.find_elements_by_xpath("//*[contains(@role,'navigation')]//*[text()='壽星']")
birthday_btn[0].click()
#write messages on each birthdayBOXes
birthday_boxes = driver.find_elements_by_xpath("//*[contains(@role,'textbox')]")
count = 0
#For the Keys.ENTER function, import keys
from selenium.webdriver.common.keys import Keys
for els in birthday_boxes:
    try:
        count +=1
        els.send_keys("Happy birthday!")
        els.send_keys(Keys.ENTER) 
        print("Birthday Wish posted for friend" + str(count)) 
    except:
        print("couldn't post")

print("done")
time.sleep(2)
driver.close()
