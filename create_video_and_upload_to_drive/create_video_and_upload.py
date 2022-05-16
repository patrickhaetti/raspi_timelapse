# create videos with ffmpeg and upload them to google drive

import schedule
import time
import datetime

import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

PICTURE_PATH = ''
VIDEO_PATH = ''


# google drive setup
gauth = GoogleAuth()

# load credentials for authentication automatization
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

#gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

# create videos and load them up to google drive
def create_video_and_upload():
	# get date time for filenames
	ct = datetime.datetime.now()
	file_extension = str(ct.year)+str(ct.month).zfill(2)+str(ct.day).zfill(2)+"_"+str(ct.hour).zfill(2)+str(ct.minute).zfill(2)

	# run video creation with ffmpeg, make videos with 3 different fps
	os.system('cd '+PICTURE_PATH+' && ffmpeg -framerate 30 -pattern_type glob -i "*.jpg" -c:v libx264 -r 30 -pix_fmt yuv420p '+VIDEO_PATH+'output_30fps.mp4 -y')
	os.system('cd '+PICTURE_PATH+' && ffmpeg -framerate 60 -pattern_type glob -i "*.jpg" -c:v libx264 -r 30 -pix_fmt yuv420p '+VIDEO_PATH+'output_60fps.mp4 -y')
	os.system('cd '+PICTURE_PATH+' && ffmpeg -framerate 120 -pattern_type glob -i "*.jpg" -c:v libx264 -r 30 -pix_fmt yuv420p '+VIDEO_PATH+'output_120fps.mp4 -y')
	print("...videos created...")

	# files to upload
	upload_file_list = [
		VIDEO_PATH+'output_30fps.mp4', 
		VIDEO_PATH+'output_60fps.mp4', 
		VIDEO_PATH+'output_120fps.mp4', 
	]

	# file names for google drive
	file_names_for_gdrive = [
		file_extension+'_zeitraffervideo_30fps.mp4',
		file_extension+'_zeitraffervideo_60fps.mp4',
		file_extension+'_zeitraffervideo_120fps.mp4'
	]

	# upload files to google drive
	for i in range(len(upload_file_list)):
	        gfile = drive.CreateFile({
	        	'title': file_names_for_gdrive[i], 
	        	'parents': [{'id': '14t2JasXhJcuKHWKSz78ou_AQOrk6pwEf'}]})
	        # Read file and set it as the content of this instance.
	        gfile.SetContentFile(upload_file_list[i])
	        gfile.Upload() # Upload the file.

	print("...files uploaded...")

# twice-daily video creation and upload by scheduling function
schedule.every().day.at("14:00").do(create_video_and_upload)
schedule.every().day.at("22:00").do(create_video_and_upload)

# Loop so that the scheduling task
# keeps on running all time.
while True:

	# Checks whether a scheduled task
	# is pending to run or not
	schedule.run_pending()
	time.sleep(1)