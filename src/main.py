from os.path import isfile
import os, shutil
from textnode import TextNode
from block_markdown import markdown_to_html_node, extract_title

def main():
    generate_pages_recursive("/home/bumsookim/workspace/github.com/samuelkim97/static-site-generator/content/", "/home/bumsookim/workspace/github.com/samuelkim97/static-site-generator/template.html", "/home/bumsookim/workspace/github.com/samuelkim97/static-site-generator/public/")

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
    return



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from \"{from_path}\" to \"{dest_path}\" using \"{template_path}\"")
    # open file
    markdown_file = open(from_path, "r")
    markdown_text = markdown_file.read()
    template_file = open(template_path, "r")
    template_text = template_file.read()

    # markdown to html
    div_node = markdown_to_html_node(markdown_text)
    html_text = div_node.to_html()


    title = extract_title(markdown_text)
    template_text = template_text.replace("{{ Title }}", title)
    template_text = template_text.replace("{{ Content }}", html_text)

    # close file
    markdown_file.close()
    template_file.close()

    # write file
    if os.path.exists(dest_path) == False:
        os.makedirs(dest_path)
    new_file_path = dest_path + "index.html"
    with open(new_file_path, "w") as new_file:
        new_file.write(template_text)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entry_list = os.listdir(dir_path_content)
    for entry in entry_list:
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(entry_path):
            generate_page(entry_path, template_path, dest_dir_path)
        else:
            new_dest_path = os.path.join(dest_dir_path, entry)
            if os.path.exists(new_dest_path) == False:
                os.makedirs(new_dest_path)
            generate_pages_recursive(entry_path, template_path, new_dest_path + "/")





main()
