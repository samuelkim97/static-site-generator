import re

from textnode import (
    text_type_text,
    text_type_code,
    text_type_bold,
    text_type_italic,
    text_type_link,
    text_type_image,
    TextNode,
)

image_regex = re.compile(r"!\[(.*?)]\((.*?\))")
link_regex = re.compile(r"\[(.*?)]\((.*?\))")

def find_match_text(string, re_type):
    code_re = re.compile(r"`.+`")
    bold_re = re.compile(r"\*{2}.+\*{2}")
    italic_re = re.compile(r"\*{1}.+\*{1}")

    if re_type == "`":
        clean_str_list = []
        for matched in code_re.findall(string):
            clean_str_list.append(matched.replace(re_type, ""))
        return clean_str_list
    if re_type == "**":
        clean_str_list = []
        for matched in bold_re.findall(string):
            clean_str_list.append(matched.replace(re_type, ""))
        return clean_str_list
    if re_type == "*":
        clean_str_list = []
        for matched in italic_re.findall(string):
            clean_str_list.append(matched.replace(re_type, ""))
        return clean_str_list
    return []

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        after_split_list = old_node.text.split(delimiter)
        if len(after_split_list) % 2 == 0:
            raise ValueError("Invalid Syntax Error.")

        if len(after_split_list) != 1:
            for part in after_split_list:
                if part in find_match_text(old_node.text, delimiter):
                    result.append(TextNode(part, text_type))
                else:
                    result.append(TextNode(part, text_type_text))

    return result

# image and link to list
def extract_markdown_images(text):
    return image_regex.findall(text)

def extract_markdown_links(text):
    return link_regex.findall(text)

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        # TextNode()
        splitted_list = re.split(r"(!\[.*?]\(.*?\))", old_node.text)
        for splitted in splitted_list:
            if image_regex.search(splitted):
                type_of_image, url = image_regex.findall(splitted)[0]
                url = url.replace(")", "")
                result.append(TextNode(type_of_image, text_type_image, url))
            elif splitted == "":
                continue
            else:
                result.append(TextNode(splitted, text_type_text))

    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        # TextNode()
        splitted_list = re.split(r"(\[.*?]\(.*?\))", old_node.text)
        for splitted in splitted_list:
            if link_regex.search(splitted):
                type_of_link, url = image_regex.findall(splitted)[0]
                url = url.replace(")", "")
                result.append(TextNode(type_of_link, text_type_link, url))
            elif splitted == "":
                continue
            else:
                result.append(TextNode(splitted, text_type_text))

    return result





#node = TextNode(
#    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#    text_type_text,
#)
#new_nodes = split_nodes_image([node])
#print(new_nodes)
# print(find_match_text("This is **bold** text.", text_type_bold))
# print(find_match_text("this is *italic text* yes!.", text_type_italic))
#print(split_nodes_delimiter([TextNode("This is text with a `code block` word", text_type_text)], "`", text_type_code))
#print(split_nodes_delimiter([TextNode("This is text with a **bold block** word", text_type_text)], "**", text_type_bold))
#print(split_nodes_delimiter([TextNode("This is text with a *italic block* word", text_type_text)], "*", text_type_italic))

