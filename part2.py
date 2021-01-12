from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
base_url="https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=b0d461c3-71ea-458e-b150-134678037221"
driver = webdriver.Chrome()

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

driver.close()

# retrieve session_id and executor_url from part1.py, saved in saved.txt
file = open('saved.txt', 'r')
filelines = file.readlines()
session_id = filelines[0].strip()
executor_url = filelines[1]

driver2 = create_driver_session(session_id, executor_url)
# browser should be loaded in maximized window
driver2.implicitly_wait(10) #10 is in seconds
# to load a given URL in browser window
driver2.get(base_url)

#click on the sign up initial
# FILL IN HERE

# "no" to covid buttons

buttons = driver.find_element_by_css_selector('input#rbtnNo')

for button in buttons:
    button.click

# submit

driver.find_element_by_css_selector('button.btn.btn-primary').click()

# submit covid waiver

driver.find_element_by_id('btnAccept').click()


# https://warrior.uwaterloo.ca/CustomPromptsAddon/GetCustomPrompts?relatedRegistrationId=f1edc478-6a13-42d0-ac50-26dfcf5273d0&productType=00000000-0000-0000-0000-000000003502
# https://warrior.uwaterloo.ca/Waiver?productId=cc2a16d7-f148-461e-831d-7d4659726dd1&entityTypeId=00000000-0000-0000-0000-000000003586&partyId=a9a83df3-431f-49a9-96c5-f308fb1b26b1&relatedEntityId=00000000-0000-0000-0000-000000000000
