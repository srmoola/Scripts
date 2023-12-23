from pytube import YouTube

SAVE_PATH = "/Users/satyadev/Desktop/Python Projects/Scripts/videos"

link= str(input("Link of the YouTube Video: "))

try:
	yt = YouTube(link)
except:
	print("Connection Error")
	
mp4_files = yt.streams.filter(file_extension='mp4')
highest_res_vid = mp4_files.get_highest_resolution()

try:
	highest_res_vid.download(SAVE_PATH)
except Exception as e:
	print(e)
	
print('Task Completed!')

