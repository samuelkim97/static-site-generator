import os, shutil
from textnode import TextNode

def main():
    pass

def copy_dir_to_dir(directory, dst):
    # if given dir exists.
    if os.path.exists(directory):
        # loop through child
        for child in os.listdir(directory):
            # make child path from child name
            child_path = os.path.join(directory, child)
            if os.path.isfile(child_path):
                shutil.copy(child_path, dst)
                print(f"Successfully Copied: \"{child_path}\" to \"{dst}\"")
            if os.path.isdir(child_path):
                new_dst = os.path.join(dst, child)
                print(f"=> Moved to \"{new_dst}\"")
                os.mkdir(new_dst)
                copy_dir_to_dir(child_path, new_dst)
            
main()

# TEST
copy_dir_to_dir("/home/bumsookim/Test/", "/home/bumsookim/workspace/github.com/samuelkim97/static-site-generator/public/")
