import subprocess
range_num=5
for i in range(2069):
    try:
        subprocess.run(['git', 'add', 'done/negative-text'+str(i)+'.png'],
                       check=True, shell=True)
    except:
        print("not")
    if i%20==0:
            range_num+=1
            try:
                subprocess.run(['git', 'commit', '-m', 'batch '+str(range_num)],
                               check=True, shell=True)
            except:
                print("not")
            try:
                subprocess.run(['git', 'push'], check=True, shell=True)
            except:
                print("not")
