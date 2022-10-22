import shutil, sys, os, re

dir_name = sys.argv[1]
digits = int(sys.argv[2])

for filename in os.listdir(sys.argv[1]):
    pattern = re.compile(r"(\d+)")
    matched = pattern.search(filename)
    if matched == None:
        continue

    original = matched.group(1)
    zfilled = original.zfill(digits)

    if original != zfilled:
        
        dir_path = os.path.abspath(dir_name)
        original_file_path = os.path.join(dir_path, filename)
        renamed_filename = filename.replace(original, zfilled)
        renamed_file_path = os.path.join(dir_path, renamed_filename)
        print('rename {before} to {after}'.format(before=filename, after=renamed_filename))
        shutil.move(original_file_path, renamed_file_path)
