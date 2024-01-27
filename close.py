import psutil


def close_program_by_name(program_name):
    for process in psutil.process_iter(attrs=['pid', 'name']):
        print(process.info['name'])
        if process.info['name'] == program_name:
            try:
                process.terminate()  
                print(f"Closed {program_name} (PID: {process.info['pid']})")
            except psutil.NoSuchProcess:
                pass


if __name__ == "__main__":
    program_to_close = "notepad.exe"
    close_program_by_name(program_to_close)
