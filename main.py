from src.getVideo import getVideo
from src.edit_video import editVideo
from src.delete_temp_files import delete_all_temp_files
from tiktok_uploader.upload import upload_video
import os
import time

print("get video")
getVideo()

time.sleep(1);
print("editing")
editVideo()

time.sleep(1)
print("uploading")
upload_video(("src/video_output/" + os.listdir("src/video_output")[0]), description="Stop It. DO SOMETHING. Videos provided by Pexel", cookies="src/cookies.txt")

time.sleep(1)
print("deleting files")
delete_all_temp_files() # delete temp files