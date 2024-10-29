import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getVideo():
    # Define the download folder path, assuming "videos" is in the same directory as the script
    download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video")

    # Set up Chrome options to specify the download folder
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,   # Set the custom download folder
        "download.prompt_for_download": False,           # Disable the download prompt
        "download.directory_upgrade": True,              # Allow changing the download directory
        "safebrowsing.enabled": True                     # Enable safe browsing to avoid security prompts
    })

    # Initialize the Chrome WebDriver with these options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open the webpage
    driver.get("https://www.pexels.com/search/videos/nature/?size=large&orientation=portrait")

    # Optional: Wait for the page to fully load
    driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to load

    # Find all <article> elements
    articles = driver.find_elements(By.TAG_NAME, "article")

    # Use first acrticle
    article = articles[0]

    # Get the first child element that contains an <a> tag
    first_child = article.find_element(By.CSS_SELECTOR, ":scope > * a")

    # Get the href attribute
    href = first_child.get_attribute("href")

    if href:
        print(f"Opening link: {href}")
        driver.get(href)  # Open the link in the same tab
        time.sleep(random.randint(1,6))  # Optional: wait a bit before moving to the next link

    # driver.quit()
    while any(file.endswith(".crdownload") for file in os.listdir(download_folder)):
        print("Waiting for downloads")
        time.sleep(1)

    print("Download finished")