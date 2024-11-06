from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import moviepy.config as mpconfig
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore
import os
import numpy as np

# Define image dimensions
IMG_HEIGHT = 288
IMG_WIDTH = 228
IMG_CHANNELS = 3

model = load_model('src/final_model.keras')  # Load the model saved from the first script

def classify_image(image_path):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize the image

    # Make prediction
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)[0]
    
    # Class names corresponding to the output layer's index
    class_names = ['forest', 'mountain', 'sea']
    
    # Return the predicted class name
    return class_names[class_idx]

def editVideo():
    mpconfig.FFMPEG_BINARY = "ffmpeg"  # Ensure ffmpeg is in the system PATH  # Set ffmpeg path in MoviePy config

    mpconfig.IMAGEMAGICK_BINARY = r"E:\ImageMagick-7.1.1-Q16\magick.exe"  # Update this path # Set ImageMagick path in MoviePy config

    path = os.listdir(r"src\video")[0]
    video = VideoFileClip('src\\video\\' + path)
    videoLen = min(video.duration, 60)
    print("video_len: ", videoLen)
    video = video.subclip(0, int(videoLen))
    quote = ""
    data = ""
    last_index = 0

    with open('src/quotes.txt', 'r', encoding='UTF-8') as f:
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

    with open('src/quotes.txt', 'w', encoding='UTF-8') as file: 
        file.writelines(data)

    print("quote: ", quote)

    txt_clip = (TextClip(quote, font ="Arial-Bold", size='large', fontsize=100, color='black', method='caption').set_position('center').set_duration(60 if videoLen > 60 else videoLen))

    result = CompositeVideoClip([video, txt_clip])
    result.write_videofile("src\\video\\" + path, fps=30)