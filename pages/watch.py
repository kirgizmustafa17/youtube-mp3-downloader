import streamlit as st
from .. import st_youtube_mp3

ydl_opts = st_youtube_mp3.ydl_opts

params = st.experimental_get_query_params()

def downloader(_url = ""):
    if _url != "":
        url = _url

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(MyCustomPP(), when='post_process')
            ydl.download([url])
    except yt_dlp.utils.DownloadError:
        st.error("DownloadError")

if len(params) > 0:
    downloader(params['v'][0])
