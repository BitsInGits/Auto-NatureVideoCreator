from src.getVideo import getVideo
from src.edit_video import editVideo
from src.delete_temp_files import delete_all_temp_files
from src.upload_video import uploadVideo
import time

print("get video")
getVideo()

time.sleep(1);
print("editing")
editVideo()

time.sleep(1)
print("uploading")
uploadVideo()

time.sleep(1)
print("deleting files")
delete_all_temp_files() # delete temp files