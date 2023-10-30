import os

cwd = os.getcwd()

folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]

for folder in folder_list:
    for file in os.listdir(folder):
        from_path = os.path.join(cwd, folder, file)
        to_path = os.path.join(cwd, file)

        os.replace(from_path, to_path)

    os.rmdir(os.path.join(cwd, folder))