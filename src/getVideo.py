import os
import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Function to check if a URL is already in the 'used.txt' file
def in_file(filename, substring):
    with open(filename, 'r') as fp:
        for line in fp:
            if substring in line:
                return True
    return False

# Function to download the image
def download_image(image_url, image_name):
    try:
        # Send a GET request to the image URL
        img_data = requests.get(image_url).content
        with open(image_name, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded image: {image_name}")
    except Exception as e:
        print(f"Error downloading image {image_name}: {e}")

# Function to get the video and image
def getVideo():
    video_download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video") # Folder for video downloads
    image_download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image")  # Folder for image downloads

    # Create the image folder if it doesn't exist
    if not os.path.exists(image_download_folder):
        os.makedirs(image_download_folder)

    chrome_options = Options()  # Set up Chrome options to specify the download folder
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": video_download_folder,   # Set the custom download folder for videos
        "download.prompt_for_download": False,           # Disable the download prompt
        "download.directory_upgrade": True,              # Allow changing the download directory
        "safebrowsing.enabled": True                     # Enable safe browsing to avoid security prompts
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)  # Initialize the Chrome WebDriver 

    driver.get("https://www.pexels.com/search/videos/nature/?size=large&orientation=portrait")  # Open the webpage
    driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to load
    articles = driver.find_elements(By.TAG_NAME, "article")  # Find all <article> elements

    i = 0
    while i < 1000:
        try:
            href = articles[i].find_element(By.CSS_SELECTOR, ":scope > * a").get_attribute("href")
            img_url = articles[i].find_element(By.CSS_SELECTOR, "img").get_attribute("src")  # Extract image URL
        
            i += 1

            # Skip if the video URL is already in the used.txt file
            if in_file("src/used.txt", href) != True:
                break
        except Exception:
            print("error occurred, maybe all pexel videos have been used, restart with old vieos")
            # clear the txt file with all already used links -> reusing already downloaded videos
            with open('src/used.txt', 'w') as file:
                pass  # Nothing to write, file will be emptied

    if i > 999:
        raise ValueError('Looked through over 1000 videos from Pexels, and nothing new is uploaded.')

    if href and img_url:
        print(f"Opening link: {href}")
        driver.get(href)  # Open the link in the same tab
        time.sleep(random.randint(1, 3))  # Optional: wait a bit before moving to the next link

        # Download the image to the 'image' folder
        image_name = os.path.join(image_download_folder, f"image_{i}.jpg")  # Save image with a unique name
        download_image(img_url, image_name)

        # Save the link in 'used.txt' to avoid using the same link again
        with open("src/used.txt", "a") as f:
            f.write(href + "\n")

    # Wait for any active downloads (video)
    while any(file.endswith(".crdownload") for file in os.listdir(video_download_folder)):  # While there are .crdownload files, it should wait
        print("Waiting for downloads")
        time.sleep(1)

    print("Download finished")
    driver.quit()