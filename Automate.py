import os
import shutil

from_dir= "C:/Users/user/Downloads" 

to_dir="C:/Users/user/Transfer images"
listoffiles=os.listdir(from_dir)
#print(os.listdir(from_dir))

for file_name in listoffiles:
    name,extension=os.path.splitext(file_name)
    
    if extension=="":
        continue
    if extension in[".txt",".doc",".docx",".pdf"]:
        path1 = from_dir + '/' + file_name # Example path1 : Downloads/ImageName1.jpg 
        path2 = to_dir + '/' + "Image_Files" # Example path2 : D:/My Files/Image_Files
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name
    
        if os.path.exists(path2):
            print("moving "+ file_name)
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)  
            print("moving "+ file_name)
            shutil.move(path1,path3)  
