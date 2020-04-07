from gazpacho import Soup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url = "http://localhost:5000/protected"

options = Options()
options.headless = True
browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
browser.get(url)

# username
username = browser.find_element_by_id("username")
username.clear()
username.send_keys("admin")

# password
password = browser.find_element_by_name("password")
password.clear()
password.send_keys("admin")

# submit
browser.find_element_by_xpath("/html/body/main/form/button").click()

# refetch
browser.get(url)

# gazpacho
html = browser.page_source
soup = Soup(html)
soup.find("blockquote").remove_tags()
