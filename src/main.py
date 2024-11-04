from getVideo import getVideo
from tiktok_uploader.upload import upload_video # type: ignore
import os

getVideo()

#add subtitles

upload_video(("src/video/" + os.listdir("src/video")[0]), description="Stop It. DO SOMETHING. Videos provided by Pexel", cookies="src/cookies.txt")