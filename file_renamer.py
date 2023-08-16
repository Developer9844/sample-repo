import os
import re

def rename_files(directory_path, search_pattern, replace_pattern):

    for filename in os.listdir(directory_path):

        old_filepath = os.path.join(directory_path, filename)

        if os.path.isfile(old_filepath):
            
            new_filename = re.sub(search_pattern, replace_pattern, filename)
            
            new_filepath = os.path.join(directory_path, new_filename)
            
            os.rename(old_filepath, new_filepath)
            
            print(f"Renamed: {filename} to {new_filename}")

if __name__ == "__main__":

    # Update this with your directory path
    dp = "sample-repo"       

    # Update this with the pattern you want to search for
    sp = r"exercise.txt"                         

    # Update this with the pattern you want to replace with
    rp = r"Exercise.txt"                        

    rename_files(dp, sp, rp)