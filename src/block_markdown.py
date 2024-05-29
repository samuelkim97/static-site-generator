import re
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes

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
# NOTE: DONE!
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



# NOTE: DONE!
# HEADING
def heading_to_html_node(block):
    return_list = []
    for line in block.split("\n"):
        tag = f"h{line.count("#")}"
        value = line.lstrip("#")
        list_of_child = text_to_textnodes(value)
        return_list.append(ParentNode(tag, list_of_child))
    return return_list

# CODE
def code_to_html_node(block):
    replaced_block = block.replace("`", "")
    replaced_string = " ".join(replaced_block.split("\n"))
    child = text_to_textnodes(replaced_string)
    return ParentNode("pre", [ParentNode("code", child)])

# QUOTE
def quote_to_html_node(block):
    pure_text = block.replace(">", "")
    string = " ".join(pure_text.split("\n"))
    child = text_to_textnodes(string)
    return ParentNode("blockquote", child)

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
        child.append(ParentNode("li", text_to_textnodes(line)))
    return ParentNode("ul", child)
# OL
def ol_to_html_node(block):
    after = []
    for line in block.split("\n"):
        after.append(line.replace(r"^\d\.\s", ""))
    after_string= " ".join(after)
    child = text_to_textnodes(after_string)
    return ParentNode("ol", [ParentNode("li", child)])

# PARAGRAPH
def paragraph_to_html_node(block):
    paragraph = " ".join(block.split("\n"))
    child = text_to_textnodes(paragraph)
    return ParentNode("p", child)

# TEST

#print(block_to_html_node("# This is heading.\n###### and also new line."))
#print(block_to_html_node("```This is code.\n with many\nline\nhahaha.```"))
# TODO: 
# split_nodes_delimiter INVALID SYNTAX ERROR INLINE..py
print(block_to_html_node("* This is first item with `code block` inside\n* second item!\n- third item\n- last item.```"))
#print(block_to_html_node("1. This is code.\n2. with many\n3. line\n4. hahaha.```"))
#print(block_to_html_node("This is code.\nwith many\nline\n4. hahaha.```"))
