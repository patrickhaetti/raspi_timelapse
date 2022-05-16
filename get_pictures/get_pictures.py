from picamera import PiCamera
from time import sleep
import datetime

PICTURE_PATH = '/../'

camera = PiCamera()

while True:
    
    ct = datetime.datetime.now()

    # pictures are only recorded during daytime
    if 4 <= ct.hour <= 23:
        # set name with timestamp
        name = str(ct.year)+str(ct.month).zfill(2)+str(ct.day).zfill(2)+"_"+str(ct.hour).zfill(2)+str(ct.minute).zfill(2)+'.jpg'
        camera.capture(PICTURE_PATH+'image_'+name)

        # print after recording
        print(str(ct.day)+"."+ str(ct.month)+"."+str(ct.year)+" - "+str(ct.hour).zfill(2)+":"+str(ct.minute).zfill(2)+":"+str(ct.second).zfill(2), end=" | ")
        print("Took picture:"+ PICTURE_PATH+'image_'+name)

        # time between pictures in seconds
        sleep(299.5)
        
