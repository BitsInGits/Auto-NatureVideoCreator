import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def in_file(filename, substring):
    with open(filename, 'r') as fp:
        for line in fp:
            if substring in line:
                return True
            else: 
                pass

def getVideo():
    download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video") # Define the download folder path, assuming "videos" is in the same directory as the script

    chrome_options = Options()     # Set up Chrome options to specify the download folder
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,   # Set the custom download folder
        "download.prompt_for_download": False,           # Disable the download prompt
        "download.directory_upgrade": True,              # Allow changing the download directory
        "safebrowsing.enabled": True                     # Enable safe browsing to avoid security prompts
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) # Initialize the Chrome WebDriver 

    driver.get("https://www.pexels.com/search/videos/nature/?size=large&orientation=portrait") # Open the webpage
    driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to load
    articles = driver.find_elements(By.TAG_NAME, "article") # Find all <article> elements

    i = 0
    while i<1000:
        href = articles[i].find_element(By.CSS_SELECTOR, ":scope > * a").get_attribute("href")
        i+=1

        if in_file("src/used.txt", href) != True:
            break

    if href:
        print(f"Opening link: {href}")
        driver.get(href)  # Open the link in the same tab
        time.sleep(random.randint(1,3))  # Optional: wait a bit before moving to the next link
        
        f = open("src/used.txt", "a")
        f.write(href)
        f.write("\n")
        f.close()

    while any(file.endswith(".crdownload") for file in os.listdir(download_folder)): #while there are crdownload files, it should wait (means thje file is still donwloading)
        print("Waiting for downloads")
        time.sleep(1)

    print("Download finished")
    driver.quit()