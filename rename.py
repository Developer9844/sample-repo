import os       # this will works with the os of our system, file paths and files
import re       # this can help to make changes in the file system

def changed_name(dir_path, rename_rules):

    for filename in os.listdir(dir_path):        # this will iterate the filename in the given dir path till the file found.

        old_file_path = os.path.join(dir_path, filename)

        if os.path.isfile(old_file_path):

            if filename in rename_rules:

                new_file_name = re.sub(rename_rules[filename][0], rename_rules[filename][1], filename)

                new_file_path = os.path.join(dir_path, new_file_name)

                os.rename(old_file_path, new_file_path)

                print(f"Renamed: {filename} to {new_file_name}")



d_p = "sample-repo"

rename_rules = {
    "Exercise.txt": (r"Exercise", "practice questions"), 
    "index.txt": (r"index", "Index"), 
}

changed_name(d_p, rename_rules)

