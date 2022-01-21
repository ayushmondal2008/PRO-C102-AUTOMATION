import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
     number=random.randinit(0,400)
     videoCaptureObject=cv2.VideoCapture(0)
     result=True
     while(result):
        ret,frame=videoCaptureObject.read()
        #read the fram while camera is on
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        #imwrite function is used to save an image to any storage device
        start_time=time.time
        result=False
     return img_name
     print("picture is taken")
     videoCaptureObject.release()
     # it will release the camera
     # close all windows that got openewd

     cv2.destroyAllWindows()

def upload_file(img_name):
         access_token = "YOUR ACCES TOKEN" 
         file =img_name 
         file_from = file 
         file_to="/testFolder/"+(img_name) 
         dbx = dropbox.Dropbox(access_token)
         with open(file_from, 'rb') as f:
             dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite) 
             print("file uploaded") 
def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot() 
            upload_file(name)
main()





def upload_file(img_name):
   access_token = ""
   file =img_name
   file_from = file
   file_to="/testFolder/"+(img_name)
   dbx = dropbox.Dropbox(access_token)
   with open(file_from, 'rb') as f:
       dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
       print("file uploaded")
       
def main():
   while(True): 
       if ((time.time() - start_time) >= 5): 
          name = take_snapshot() 
          upload_file(name)
main()


