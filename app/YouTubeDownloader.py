import pytubefix
import subprocess
import os
from app.support import copy_current_link


def downloader():

    url = str(copy_current_link())
    yt = pytubefix.YouTube(url=url, use_oauth=True)
    file_name = yt.title.replace(' ', '_')

    print("Select quality, e.g. 1080, 720, 480\n")
    q = str(input("Waiting for quality: "))

    try:
        video_stream = yt.streams.video_stream = yt.streams.filter(
            progressive=False, file_extension="mp4", resolution=f"{q}p").first()
        
    except Exception as ex:
        print("Video stream with the desired quality was not found.")
        return
    
    audio_stream = yt.streams.filter(
        only_audio=True, file_extension="mp4").first()

    if video_stream:

        video_stream.download(
            output_path="/Users/antonbliznuk/Образование/Программирование/Python/Проекты/Hot-Keys/app/video", filename=f"{file_name}.mp4")
        print("Video has been downloaded")

    else:
        print("Video stream with the desired quality was not found.")
        return

    if audio_stream:

        audio_stream.download(
            output_path="/Users/antonbliznuk/Образование/Программирование/Python/Проекты/Hot-Keys/app/audio", filename=f"{file_name}.mp4")
        print("Video has been downloaded")

    else:
        print("Audio stream not found.")
        return

    if video_stream and audio_stream:
        command = [
            'ffmpeg',
            '-i', f'/Users/antonbliznuk/Образование/Программирование/Python/Проекты/Hot-Keys/app/video/{
                file_name}.mp4',
            '-i', f'/Users/antonbliznuk/Образование/Программирование/Python/Проекты/Hot-Keys/app/audio/{
                file_name}.mp4',
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-strict', 'experimental',
            f"/Users/antonbliznuk/Downloads/{file_name}.mp4"
        ]
        subprocess.run(command)

    print(f"The video has been saved to downloads\nName : {file_name}")

    os.system(
        f"rm /Users/antonbliznuk/Образование/Программирование/Python/Проекты/Hot-Keys/app/video/{file_name}.mp4")
    os.system(
        f"rm /Users/antonbliznuk/Образование/Программирование/Python/Проекты/Hot-Keys/app/audio/{file_name}.mp4")
    return


if __name__ == "__main__":
    downloader()
