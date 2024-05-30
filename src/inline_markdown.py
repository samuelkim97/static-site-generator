import re
import pprint

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
    code_re = re.compile(r"`{3}.+`{3}")
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
        if find_match_text(old_node.text, delimiter):
            after_split_list = old_node.text.split(delimiter)
            num_of_delimiter = old_node.text.count(delimiter)
            if old_node.text == "":
                continue
            
            # CASE1: if oldnode doesn't have delimiter or invalid syntax
            elif num_of_delimiter == 0 or (num_of_delimiter % 2 == 1):
                result.append(old_node)
            # CASE2: if oldnode have right syntax
            elif old_node.text.count(delimiter) % 2 == 0:
                for part in after_split_list:
                    if part in find_match_text(old_node.text, delimiter):
                        result.append(TextNode(part, text_type))
                    else:
                        result.append(TextNode(part, text_type_text))

    return old_nodes

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
        if len(splitted_list) == 1:
            result.append(old_node)
        else:
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
        if len(splitted_list) == 1:
            result.append(old_node)
        else:
            for splitted in splitted_list:
                if link_regex.search(splitted):
                    type_of_link, url = link_regex.findall(splitted)[0]
                    url = url.replace(")", "")
                    result.append(TextNode(type_of_link, text_type_link, url))
                elif splitted == "":
                    continue
                else:
                    result.append(TextNode(splitted, text_type_text))

    return result

# LAST PART RETURNS TEXT TO BUNCH OF TEXTNODES
def text_to_textnodes(text):
    text_node = TextNode(text, text_type_text)
    a = split_nodes_image([text_node])
    b = split_nodes_link(a)
    c = split_nodes_delimiter(b, "`", text_type_code)
    d = split_nodes_delimiter(c, "**", text_type_bold)
    e = split_nodes_delimiter(d, "*", text_type_italic)
    return e
    

#final = text_to_textnodes("1. An elaborate pantheon of deities (the `Valar` and `Maiar`)\n2. The tragic saga of the Noldor Elves\n3. The rise and fall of great kingdoms such as Gondolin and Númenor")

#print(final)
#node = TextNode(
#    "This is\n text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#    text_type_text,
#)
#new_nodes = split_nodes_image([node])
#print(new_nodes)
# print(find_match_text("This is **bold** text.", text_type_bold))
# print(find_match_text("this is *italic text* yes!.", text_type_italic))
#print(split_nodes_delimiter([TextNode("This is text with a `code block` word", text_type_text)], "`", text_type_code))
#print(split_nodes_delimiter([TextNode("This is text with a **bold block** word", text_type_text)], "**", text_type_bold))
#print(split_nodes_delimiter([TextNode("This is text with a *italic block* word", text_type_text)], "*", text_type_italic))

