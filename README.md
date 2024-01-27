# Open -> Capture Screenshot -> Close

In this repository, we provide a script that automates the process of opening an Excel file, capturing a screenshot of a specific Excel section, and then closing the Excel application. The results of running the `open-screenshot-close.py` script can be found in the "done" folder.

## Installing Dependencies

Before running the `open-screenshot-close.py` script, you need to install the `Pillow` library. Please note that the closing part of the script is currently designed for Windows OS. To enable program closure on Linux and macOS, you should also install `psutil` as follows:

```bash
pip install psutil
pip install Pillow
```

## Steps for Running the Program

Follow these steps to run the program:

* **Install Dependencies**: If you are using Linux or macOS, replace the `close_program_by_name` function in `open-screenshot-close.py` with the code provided in `close.py`.

* **Configure File Paths**: Set the values of `base_file_path` and `base_store_screenshot_path` in `open-screenshot-close.py`.

* **Specify the Area for Screenshots**: Define the region of the screen that you want to capture.

* **Execute the Script**: Run the script using the following command:

```bash
python open-screenshot-close.py
```

This script simplifies the process of opening, capturing, and closing an Excel file, streamlining your workflow for taking screenshots of specific Excel sections.
