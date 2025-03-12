# Auto-NatureVideoCreator

This Project is designed, to retireve calming videos of the nature from pexels.com,
then add some motivation-subtitles and upload this to TikTok (maybe more later).

<!-- You will use you TikTok Session Cookies to rejoin the session, for that you need it as cookies.txt file,
you can get it with an extension like "Get cookies.txt LOCALLY" -->
# Setup

>pip install requirements -r

>save your cookies as cookies.txt in the src folder

>install ImageMagick and FFMPEG

>update edit_video.py and set your Paths for FFMPEG and ImageMagick

>start main.py
 
# More

You need to have Google Chrome installed.
Also https://github.com/Zulko/moviepy needs to be installed.
And ImageMagick-7.1.1-39-Q16-x64-dll.exe (download and install, add to system path) from https://imagemagick.org/script/download.php
And ffmpeg-master-latest-win64-gpl.zip (download, extract and move to your desired folder, add to system path) from https://github.com/BtbN/FFmpeg-Builds/releases

Training data and script for the image classification model is available, contact me.

# Technicals
The script downloads a randomly selected video from the top 20 vertical "nature" videos on Pexels. It then adds subtitles using text from a file containing motivational quotes, overlays background music, and uploads the final video to TikTok using the account credentials specified in the cookies.txt file.

used.txt: Keeps track of all previously used videos to prevent duplicates.
quotes.txt: Contains a collection of motivational quotes. The first line stores the index of the last used quote; to reset and start from the beginning, set this value to 0.
image_classifier_model.h5: A pre-trained CNN model for image classification, used to adjust the accompanying audio.
