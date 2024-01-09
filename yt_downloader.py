import os
from pytube import YouTube

USER_PATH = os.path.expanduser('~')
SAVE_PATH = os.path.join(os.path.join(USER_PATH, "Desktop"), "yt-downscript-videos")

try:
	os.mkdir(SAVE_PATH)
except:
	pass

def download_video(yt_video_link):

	try:
		yt = YouTube(yt_video_link)
	except:
		print("Connection Error")
		return
		
	mp4_files = yt.streams.filter(file_extension='mp4')
	highest_res_vid = mp4_files.get_highest_resolution()

	try:
		highest_res_vid.download(SAVE_PATH)
	except Exception as e:
		print(e)
		return

try:
	while True:
		get_yt_video_link = str(input("Enter YouTube Video Link: "))
		download_video(get_yt_video_link)
except KeyboardInterrupt:
    print('Process Completed!')

