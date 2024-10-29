from urllib import request
import urllib

import os
import sys


def add_module_to_path(relative_path):
    """Add the specified relative path to sys.path if it's not already included."""
    module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
    if module_path not in sys.path:
        sys.path.append(module_path)

# Add specific modules
add_module_to_path("pexels-api")

# Import modules from that directory
import pexels                       

#URL = "https://raw.githubusercontent.com/wkaisertexas/wkaisertexas.github.io/main/upload.mp4"
#FILENAME = "upload.mp4"

##################################'MAIN'##################################   
if __name__ == "__main__":
    # download random video
    #urllib.request.urlretrieve(URL, FILENAME)

    # upload video to TikTok
    #upload_video(FILENAME, description="Stop It. DO SOMETHING. Videos provided by Pexel", cookies="cookies.txt") 