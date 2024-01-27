import os
import shutil
start=0
end=2069
folder_name=''
# os.mkdir('done/n1600-1600/')
for i in range(start,end+1):
    if folder_name=='' or i%400==0:
        folder_name = 'done/bw'+str(i)+'-'+str(i+401)
        try:
            os.mkdir(folder_name)
        except:
            print("exist")
    os.replace(f"done/black-white-text{i}.png",
            f"{folder_name}/black-white-text{i}.png")
# os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
