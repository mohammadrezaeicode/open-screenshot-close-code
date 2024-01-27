import subprocess
import platform


def close_program_by_name(program_name):
    try:
        if platform.system() == "Windows":
            # List processes using 'tasklist' and filter by program name
            tasklist_output = subprocess.check_output(["tasklist"], text=True)
            for line in tasklist_output.splitlines():
                print(line.lower())
                if program_name.lower() in line.lower():
                    process_info = line.split()
                    pid = int(process_info[1])
                    # Terminate the process using 'taskkill'
                    subprocess.run(["taskkill", "/F", "/PID", str(pid)])
                    print(f"Closed {program_name} (PID: {pid})")
    except subprocess.CalledProcessError:
        pass


if __name__ == "__main__":
    # Replace with the name of the program you want to close
    program_to_close = "excel.exe"
    close_program_by_name(program_to_close)
