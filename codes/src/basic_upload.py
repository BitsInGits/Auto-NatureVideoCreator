from urllib import request
import urllib
import sys
import os

# Get the directory where the current script is located, Construct the path to the target directory dynamically
module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tiktok-uploader", "src")
#Add the constructed path to sys.path if it's not already there
if module_path not in sys.path:
    sys.path.append(module_path)

# Now import your modules from that directory
from tiktok_uploader.upload import upload_video # type: ignore

##################################'MAIN'##################################                          

URL = "https://raw.githubusercontent.com/wkaisertexas/wkaisertexas.github.io/main/upload.mp4"
FILENAME = "upload.mp4"

if __name__ == "__main__":
    # download random video
    urllib.request.urlretrieve(URL, FILENAME)

    # upload video to TikTok
    upload_video(FILENAME, description="Stop It. DO SOMETHING. Videos provided by Pexel", cookies="cookies.txt") 