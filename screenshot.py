# importing webdriver from selenium
from selenium import webdriver

from PIL import Image

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 2
options = Options()
# options.headless = True
options.add_argument('--headless')

# Here Chrome will be used
driver = webdriver.Chrome(options=options)

# URL of website
# url = "https://www.geeksforgeeks.org/"
url ="https://git.amala.earth/developers/amala-tech-housekeeping"

# Opening the website
driver.get(url,)

driver.save_screenshot("image.png")

# Loading the image
image = Image.open("image.png")

# Showing the image
image.show()
