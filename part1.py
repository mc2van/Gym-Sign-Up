from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

your_email = 'FILL IN'
your_password = 'FILL IN'

base_url="https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=b0d461c3-71ea-458e-b150-134678037221"
driver=webdriver.Chrome(executable_path="chromedriver")

# browser should be loaded in maximized window
driver.maximize_window()
# driver should wait implicitly for a given duration, for the element under consideration to load.
# to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
driver.implicitly_wait(10) #10 is in seconds
# to load a given URL in browser window
driver.get(base_url)
# test whether correct URL/ Web Site has been loaded or not
assert "Waterloo" in driver.title
# driver.close()
driver.find_element_by_id("loginLink").click()

driver.find_element_by_css_selector(".loginOption.btn.btn-lg.btn-block.btn-social.btn-soundcloud").click()

login = driver.find_element_by_id("userNameInput")
login.clear()
login.send_keys(your_email)
login.send_keys(Keys.RETURN)

password = driver.find_element_by_id("passwordInput")
password.clear()
password.send_keys(your_password)
password.send_keys(Keys.RETURN)

print(driver.session_id)
print(driver.command_executor._url)

file = open('saved.txt', 'w')
file.write("{}\n".format(driver.session_id))
file.write(driver.command_executor._url)