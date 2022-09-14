import streamlit as st

params = st.experimental_get_query_params()


ydl_opts = dict(
    format='bestaudio',
#     paths='./mp3_folder/',
    outtmpl='%(title)s - %(id)s.%(ext)s',
    progress_hooks=[my_hook],
    writethumbnail=write_thumbnail,
    windowsfilenames=True,
    postprocessors=[
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': quality},
        {'key': 'FFmpegMetadata', 'add_metadata': add_metadata},
        {'key': 'EmbedThumbnail'}
    ])


def downloader(_url = ""):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(MyCustomPP(), when='post_process')
            ydl.download([_url])
    except yt_dlp.utils.DownloadError:
        st.error("DownloadError")

if len(params) > 0:
    downloader(params['v'][0])
