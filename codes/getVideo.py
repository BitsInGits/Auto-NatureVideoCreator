from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL to open
url = "https://www.pexels.com/search/videos/nature/?size=large&orientation=portrait"

# Open the webpage
driver.get(url)

# Optional: Wait for the page to fully load
driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to load

# Closing the driver after your actions
# Uncomment if you want to close the browser after some time
# driver.quit()
