import os
import re
import streamlit as st
import yt_dlp

_VALID_URL = r'''(?x:
    https?://
        (?:\w+\.)?
        (?:
            youtube(?:kids)?\.com|
            %(invidious)s
        )/
        (?:
            (?P<channel_type>channel|c|user|browse)/|
            (?P<not_channel>
                feed/|hashtag/|
                (?:playlist|watch)\?.*?\blist=
            )|
            (?!(?:%(reserved_names)s)\b)  # Direct URLs
        )
        (?P<id>[^/?\#&]+)
)'''


st.title("music.Youtube Downloader")

old_url = ""
url = st.text_input("Youtube URL") # max_chars=43

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


ydl_opts = dict(format='bestaudio', progress_hooks=[my_hook], writethumbnail=write_thumbnail, postprocessors=[
    {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': quality},
    {'key': 'FFmpegMetadata', 'add_metadata': add_metadata},
    {'key': 'EmbedThumbnail'}
])


btn = st.button("Start downloading.")

placeholder = st.empty()


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        placeholder.success("Yay! Finally done converting.")
        st.markdown("""---""")
        # st.balloons()

        mp3_path = str(os.path.splitext(xx)[0]) + ".mp3"

        st.info(os.path.basename(mp3_path))
        audio_file = open(mp3_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mpeg')

        with open(mp3_path, "rb") as file:
            st.download_button(
                label="Download MP3",
                data=file,
                file_name=os.path.basename(mp3_path),
                mime='audio/mpeg',
            )

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

if url != old_url or btn:
    if re.match(_VALID_URL, url):
        old_url = url
        downloader()
