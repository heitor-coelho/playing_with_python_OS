import os 


cwd = os.getcwd()

full_list = os.listdir(cwd)

files_list = [f for f in full_list if os.path.isfile(f) and '.py' not in f]
types = set([f.split('.')[-1] for f in files_list])

for t in types:
    os.mkdir(t)

for f in files_list:
    from_path = os.path.join(cwd, f)
    to_path = os.path.join(cwd, f.split('.')[-1], f)

    os.replace(from_path, to_path)


