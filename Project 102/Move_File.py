import os
import shutil
fromdir="./source"
todir="./destination"

listoffiles=os.listdir(fromdir)
for filename in listoffiles:
    name,extension=os.path.splitext(filename)
    if extension=="":
        continue
    if extension in ['.gif','.jpg']:
        path1=fromdir+"/"+filename
        path2=todir+"/"+"imagefiles"
        path3=todir+"/"+"imagefiles"+"/"+filename

        if os.path.exists(path2):
            print("creating")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)  