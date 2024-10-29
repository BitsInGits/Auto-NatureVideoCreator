from urllib import request
import urllib
import sys
import os
from tiktok_uploader.upload import upload_video # type: ignore

# def basicUpload():
URL = "https://raw.githubusercontent.com/wkaisertexas/wkaisertexas.github.io/main/upload.mp4"
FILENAME = "upload.mp4"
# download random video
urllib.request.urlretrieve(URL, FILENAME)
# upload video to TikTok
upload_video(FILENAME, description="Stop It. DO SOMETHING. Videos provided by Pexel", cookies="src/cookies.txt") 