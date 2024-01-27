import subprocess
import platform
import time
from PIL import ImageGrab


base_file_path=''
base_store_screenshot_path=''


def open_file(name):
    file_path = base_file_path+name
    try:
        subprocess.run(['start', file_path], check=True)
    except FileNotFoundError:
        try:
            subprocess.run(['start', file_path], check=True, shell=True)
        except subprocess.CalledProcessError:
            print("Error: Unable to open the file with the default program.")

def close_program_by_name(program_name):
    try:
        if platform.system() == "Windows":
            tasklist_output = subprocess.check_output(["tasklist"], text=True)
            for line in tasklist_output.splitlines():
                print(line.lower())
                if program_name.lower() in line.lower():
                    process_info = line.split()
                    pid = int(process_info[1])
                    subprocess.run(["taskkill", "/F", "/PID", str(pid)])
                    print(f"Closed {program_name} (PID: {pid})")
    except subprocess.CalledProcessError:
        pass

def screen_shot(name):
    screenshot = ImageGrab.grab()
    print(screenshot.size)
    left = 695  
    top = 300  
    right = 1450  
    bottom = 700  
    cropped_region = screenshot.crop((left, top, right, bottom))
    cropped_region.save(base_store_screenshot_path+name)
if __name__ == "__main__":
    for i in range(1986, 2068):
            name = 'negative-text'+str(i)
            name1 = 'black-white-text'+str(i)
            open_file(name+'.xlsx')
            time.sleep(2)
            screen_shot(name+'.png')
            time.sleep(1)
            close_program_by_name("excel.exe")
            open_file(name1+'.xlsx')
            time.sleep(1)
            screen_shot(name1+'.png')
            time.sleep(1)
            close_program_by_name("excel.exe")
            if i%100==0:
                time.sleep(5)
            if i % 50 == 0:
                time.sleep(5)
            if i % 20 == 0:
                time.sleep(5)
