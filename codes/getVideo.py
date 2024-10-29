import time
import random
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

# Find all <article> elements
articles = driver.find_elements(By.TAG_NAME, "article")

# Loop through each <article> and get the first child's href
for article in articles:
    print("article: ",article)
    try:
        # Get the first child element that contains an <a> tag
        first_child = article.find_element(By.CSS_SELECTOR, ":scope > * a")
        
        # Get the href attribute
        href = first_child.get_attribute("href")
        
        if href:
            print(f"Opening link: {href}")
            driver.get(href)  # Open the link in the same tab
            time.sleep(random.randint(1,6))  # Optional: wait a bit before moving to the next link
            
            # Go back to the main page to continue with the next link
            #driver.back()
            #time.sleep(2)  # Optional: wait a bit before finding the next article
    except Exception as e:
        print(f"Error accessing first child link: {e}")
    

# driver.quit()
time.sleep(20)