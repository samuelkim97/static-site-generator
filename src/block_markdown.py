import re
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading= "heading"
block_type_code= "code"
block_type_quote= "quote"
block_type_ul= "unordered_list"
block_type_ol= "ordered_list"



def markdown_to_blocks(markdown):
    return markdown.split("\n\n")

# paragraph, heading, code quote unordered_list ordered_list
def block_to_block_type(single_block):
    heading_regex = re.compile(r"^#{1,6}\s")
    code_regex = re.compile(r"^`{3}(?:\n|.)*?`{3}$")
    quote_regex = re.compile(r"^>")
    ul_regex = re.compile(r"^(\*|-)\s")
    ol_regex = re.compile(r"^\d\.\s")

    splitted = single_block.split("\n")
    # heading regex
    if all(heading_regex.search(line) for line in splitted):
        return block_type_heading
    # check for code regex
    if code_regex.search(single_block):
        return block_type_code
    # check for quote_regex
    if all(quote_regex.search(line) for line in splitted):
        return block_type_quote
    # check for ul_regex
    if all(ul_regex.search(line) for line in splitted):
        return block_type_ul
    # check for ol_regex
    if all(ol_regex.search(line) for line in splitted):
        return block_type_ol
    return block_type_paragraph

def block_to_html_node(single_block):
    block_type = block_to_block_type(single_block)
    # HEADING
    if block_type == block_type_heading:
        return heading_to_html_node(single_block)
    # CODE
    if block_type == block_type_code:
        return code_to_html_node(single_block)
    # QUOTE
    if block_type == block_type_quote:
        return quote_to_html_node(single_block)
    # UL
    if block_type == block_type_ul:
        return ul_to_html_node(single_block)
    # OL
    if block_type == block_type_ol:
        return ol_to_html_node(single_block)
    # PARAGRAPH
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(single_block)

# text to list of html node
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

# HEADING
def heading_to_html_node(block):
    return_list = []
    for line in block.split("\n"):
        tag = f"h{line.count("#")}"
        value = line.lstrip("#")
        list_of_child = text_to_children(value)
        return_list.append(ParentNode(tag, list_of_child))
    return return_list

# CODE
def code_to_html_node(block):
    replaced_block = block.replace("`", "")
    replaced_string = " ".join(replaced_block.split("\n"))
    child = text_to_children(replaced_string)
    return [ParentNode("pre", [ParentNode("code", child)])]

# QUOTE
def quote_to_html_node(block):
    pure_text = block.replace(">", "")
    string = " ".join(pure_text.split("\n"))
    child = text_to_children(string)
    return [ParentNode("blockquote", child)]

# UL
def ul_to_html_node(block):
    # split line by line and delete * , - 
    after = []
    for line in block.split("\n"):
        after.append(line.lstrip("* ").lstrip("- "))
    # delelted *, - lines => after

    # change line to HTMLNode
    child = []
    for line in after:
        child.append(ParentNode("li", text_to_children(line)))
    return [ParentNode("ul", child)]
# OL
def ol_to_html_node(block):
    after = []
    child = []
    for line in block.split("\n"):
        after.append(re.sub(r"^\d\.\s", "", line))
    for after_line in after:
        child.append(ParentNode("li", text_to_children(after_line)))
    return [ParentNode("ol", child)]

# PARAGRAPH
def paragraph_to_html_node(block):
    paragraph = " ".join(block.split("\n"))
    child = text_to_children(paragraph)
    return [ParentNode("p", child)]


def markdown_to_html_node(markdown):
    list_of_blocks = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        list_of_blocks.append(block_to_html_node(block))
    return ParentNode("div", list_of_blocks)


def extract_title(markdown):
    for block in markdown_to_html_node(markdown).children:
        for line_node in block:
            if line_node.tag == "h1":
                heading = ""
                list_of_h1 = line_node.children
                for text_node in list_of_h1:
                    heading += text_node.value
                heading = heading.lstrip(" ")
                return heading


    raise Exception("All pages need a single h1 header.")
        #for parent_node in block:
            #print(parent_node)
    #raise Exception("All pages need a h1 header.")

# TEST
#markdown1 = """# This is heading
## and 2

#* this is unordered list.
#- this too

#`print("This is code")
#x = 2 + 2
#print(x)`

#Last, this is with **bold text** and *italic*
#and of course ![image](~/home/picture/pic.jpg)
#[link](https://www.google.com) link too!
#"""
#print(extract_title(markdown1))
#print(markdown_to_html_node(markdown1).children)
#print(block_to_html_node("# This is heading.\n###### and also new line."))
#print(block_to_html_node("```This is code.\n with many\nline\nhahaha.```"))
# split_nodes_delimiter INVALID SYNTAX ERROR INLINE..py
#print(block_to_html_node("* This is first item with `code block` inside\n* second item!\n- third item\n- last item.```"))
#print(block_to_html_node("1. This is code.\n2. with many\n3. line\n4. hahaha.```"))
#print(block_to_html_node("This is code.\nwith many\nline\n4. hahaha.```"))
