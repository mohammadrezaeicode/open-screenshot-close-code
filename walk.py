from os import walk

f = []
layer = 1
w = walk("done")
file = open("fileInDone.txt", "w")
for (dirpath, dirnames, filenames) in w:
    for i in filenames:
        print(dirpath+"\\"+i)
        file.write(dirpath+"\\"+i+"\n")
        f.append(dirpath+"\\"+i)
    # if layer == 2:
    #     f.extend(dirnames)
    #     break
    # layer += 1



file.close()
