import os

files_to_process = [
    r"C:\Users\48530\Desktop\pythonProject\zad23a.py",
    r"C:\Users\48530\Desktop\pythonProject\zad23b.py"
]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)