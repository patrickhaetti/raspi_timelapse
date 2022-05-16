## Creating time lapse videos with RaspberryPi and upload automatically to google drive

### Requirements:
1. RaspberryPi with Camera
2. FFmpeg: On Linux enter ```sudo apt install ffmpeg```
3. Gogle drive and authentication, see more here https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf
4. Python 3.9 with pipenv installed

### Instructions to shoot pictures:
1. Download this repository and go to folder get_pictures
2. Create pipenv and install requirements.txt
3. Open python file and set path for saving pictures
4. Run pyhon file in pipenv environment

### Instructions to automatically create time lapse videos and upload them to google drive:
1. Go to folder create_video_and_upload_to_drive
2. Create pipenv and install requirements.txt
3. Open python file and set path for saving pictures + path for saving videos
4. Run pyhon file in pipenv environment
5. When uploading first time a browser window will show up for authentication. Credentials will then be saved in mycreds.txt for later use, auhentication won't be required afterwards
