from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import moviepy.config as mpconfig
import os

def editVideo():
    mpconfig.FFMPEG_BINARY = "ffmpeg"  # Ensure ffmpeg is in the system PATH  # Set ffmpeg path in MoviePy config

    mpconfig.IMAGEMAGICK_BINARY = r"E:\ImageMagick-7.1.1-Q16\magick.exe"  # Update this path # Set ImageMagick path in MoviePy config

    path = os.listdir(r"src\video")[0]
    video = VideoFileClip('src\\video\\' + path)
    videoLen = min(video.duration, 60)
    print("video_len: ", videoLen)
    video = video.subclip(0, videoLen)
    quote = ""
    data = ""
    last_index = 0

    with open('src/quotes.txt', 'r') as f:
        data = f.readlines()
        for i, line in enumerate(data):
            if i == 0:
                last_index = int(data[i])
            elif i == last_index+1:
                quote = data[i]
                data[0] = str(last_index+1)+'\n'

        if quote == '':
            data[0] = "1\n"
            quote = data[1]

    with open('src/quotes.txt', 'w') as file: 
        file.writelines(data)

    print("quote: ", quote)

    txt_clip = (TextClip(quote, font ="Arial-Bold", size='large', fontsize=100, color='black', method='caption').set_position('center').set_duration(60 if videoLen > 60 else videoLen))

    result = CompositeVideoClip([video, txt_clip])
    result.write_videofile("src\\video\\" + path, fps=30)