# Auto-NatureVideoCreator

This Project is designed, to retireve calming videos of the nature from pexels.com,
then add some motivation-subtitles and upload this to TikTok (maybe more later).

https://github.com/wkaisertexas/tiktok-uploader

You will use you TikTok Session Cookies to rejoin the session, for that you need it as cookies.txt file,
you can get it with an extension like "Get cookies.txt LOCALLY"
# Setup

>pip install requirements -r

>save your cookies as cookies.txt in the src folder

>install ImageMagick and FFMPEG

>update edit_video.py and set your Paths for FFMPEG and ImageMagick

>start main.py

# More

You need to have Google Chrome installed.
Also https://github.com/Zulko/moviepy needs to be installed.
And https://github.com/wkaisertexas/tiktok-uploader also.
And ImageMagick-7.1.1-39-Q16-x64-dll.exe (download and install, add to system path) from https://imagemagick.org/script/download.php
And ffmpeg-master-latest-win64-gpl.zip (download, extract and move to your desired folder, add to system path) from https://github.com/BtbN/FFmpeg-Builds/releases

# TODO
-explain setup better

# Technicals
It will download randome one of the 20 Top Videos on Pexel with the tag nature thats vertical.
Then add Subtitles from a txt full motivational texts and music
Then upload this to tiktok on your profile given in the cookies.txt file

used.txt is a list of all already used videos

quotes.txt is a list of many quotes, where one gets added to the video. in the first line it says wich line index was the last one use,
so to restart from the top write just a 0 in the first line