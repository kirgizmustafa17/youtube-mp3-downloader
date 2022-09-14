import os
import re
import streamlit as st
import yt_dlp
from _VALID_URL import _VALID_URL
import time

# files = [f for f in os.listdir('.') if os.path.isfile(f)]
# print(files)

st.title("music.Youtube Downloader")

old_url = ""  # https://youtu.be/JcR7QUmEEGU
url = st.text_input("Youtube URL")  # max_chars=43

quality = st.select_slider('MP3 Quality (Lower is better; but higher file size)', options=range(10))
cover = st.checkbox('Write thumbnail as album cover?')
metadata = st.checkbox('Edit MP3 metadatas (album, artist etc.)?')

add_metadata = True if metadata else False
write_thumbnail = True if cover else False
my_bar = st.progress(0)


def my_hook(d):
    global xx
    xx = os.path.abspath(d['filename'])

    if d['status'] == 'finished':
        placeholder.info("Done downloading, now post-processing....")

    if d['status'] == 'downloading':
        my_bar.progress(int(float(d['_percent_str'].split('%')[0])))


ydl_opts = dict(
    format='bestaudio',
#     paths='./mp3_folder/',
    outtmpl='./mp3_folder/%(title)s - %(id)s.%(ext)s',
    progress_hooks=[my_hook],
    writethumbnail=write_thumbnail,
    windowsfilenames=True,
    postprocessors=[
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': quality},
        {'key': 'FFmpegMetadata', 'add_metadata': add_metadata},
        {'key': 'EmbedThumbnail'}
    ])


# No need that button, script will track entry box changes (url).
# btn = st.button("Start downloading.")

placeholder = st.empty()


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        placeholder.success("Yay! Finally done converting.")
        # st.balloons()

        mp3_path = str(os.path.splitext(xx)[0]) + ".mp3"

#         Player
        st.info(os.path.basename(mp3_path))
        audio_file = open(mp3_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mpeg')

#         Downloader
        with open(mp3_path, "rb") as file:
            st.download_button(
                label="Download MP3",
                data=file,
                file_name=os.path.basename(mp3_path),
                mime='audio/mpeg',
            )

        st.markdown("""---""")


        return [], info


def downloader():
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(MyCustomPP(), when='post_process')
            ydl.download([url])
    except yt_dlp.utils.DownloadError:
        st.error("DownloadError")

# class MyLogger:
#     def debug(self, msg):
#         # For compatibility with youtube-dl, both debug and info are passed into debug
#         # You can distinguish them by the prefix '[debug] '
#         if msg.startswith('[debug] '):
#             pass
#         else:
#             self.info(msg)
#
#     def info(self, msg):
#         pass
#
#     def warning(self, msg):
#         pass
#
#     def error(self, msg):
#         print(msg)

if url != old_url:  # or btn
    now = time.time()

    for f in os.listdir("./mp3_folder/"):
        print(f)
        if os.stat(f).st_mtime < now - 3600:
            os.remove(os.path.join("./mp3_folder/", f))
            print(f"REMOVED {f}")

    if re.match(_VALID_URL, url):
        old_url = url
        downloader()
