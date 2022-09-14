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

def my_hook(d):
    global xx
    xx = os.path.abspath(d['filename'])

    if d['status'] == 'finished':
        placeholder.info("Done downloading, now post-processing....")

    if d['status'] == 'downloading':
        my_bar.progress(int(float(d['_percent_str'].split('%')[0])))


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


def downloader(_url = ""):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(MyCustomPP(), when='post_process')
            ydl.download([_url])
    except yt_dlp.utils.DownloadError:
        st.error("DownloadError")

if len(params) > 0:
    downloader(params['v'][0])
