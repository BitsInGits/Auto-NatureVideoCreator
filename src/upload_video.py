def uploadVideo():
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    import time
    import os

    # Path to your cookies.txt file
    cookies_file = "src/cookies.txt"

    # Define the folder containing the video file
    video_folder = "src/video_output"

    # Get the first file in the folder
    video_files = sorted(os.listdir(video_folder))
    if not video_files:
        print("No video files found in the folder!")
        return

    video_path = os.path.abspath(os.path.join(video_folder, video_files[0]))

    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open TikTok to set cookies
        driver.get("https://www.tiktok.com")
        time.sleep(5)  # Allow page to load

        # Load cookies from the text file
        if os.path.exists(cookies_file):
            with open(cookies_file, "r") as file:
                for line in file:
                    # Skip comments and blank lines
                    if line.startswith("#") or not line.strip():
                        continue

                    # Parse each line of the cookies.txt file
                    # Expected format: domain \t flag \t path \t secure \t expiry \t name \t value
                    parts = line.strip().split("\t")
                    if len(parts) >= 7:
                        cookie = {
                            "domain": parts[0],
                            "name": parts[5],
                            "value": parts[6],
                            "path": parts[2],
                            "secure": parts[3].lower() == "true",
                        }
                        # Add expiry if present and valid
                        if parts[4].isdigit():
                            cookie["expiry"] = int(parts[4])

                        driver.add_cookie(cookie)

        # Navigate to the TikTok Studio Upload page
        driver.get("https://www.tiktok.com/tiktokstudio/upload")

        time.sleep(5)  # Allow page to load

        # Locate the "Select video" button
        select_video_button = driver.find_element(
            By.XPATH, "//div[contains(@class, 'upload-stage-btn')]/button[1]"
        )

        # Click on the "Select video" button
        select_video_button.click()

        time.sleep(5)

        # Simulate the file upload
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(video_path)

        time.sleep(5)

        # Modify the inner HTML of the specified element
        # Locate the parent element
        editor_content = driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")

        # Traverse to the child span element and modify its HTML
        driver.execute_script(
            """
            const editorContent = arguments[0];
            const targetElement = editorContent.querySelector('[data-offset-key]');
            if (targetElement) {
                targetElement.innerHTML = '<span data-offset-key="f6qol-0-0"><span data-text="true">Stop it, do something!</span></span>';
            }
            """,
            editor_content
        )

        print("Inner HTML modified to 'Stop it, do something!'")

        time.sleep(20)

        # Wait until the button with `aria-disabled="false"` is available
        wait = WebDriverWait(driver, 100)  # Timeout after 20 seconds
        button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'button-group')]/button[1][@aria-disabled='false']",
                )
            )
        )

        button.click()

        print("done uploading")

        time.sleep(5)
    finally:
        # Close the browser
        driver.quit()