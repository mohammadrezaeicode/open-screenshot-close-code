import subprocess

file_path = ''

try:
    subprocess.run(['open', file_path], check=True)
except FileNotFoundError:
    try:
        subprocess.run(['start', file_path], check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Error: Unable to open the file with the default program.")
