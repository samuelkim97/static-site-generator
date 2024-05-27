import re

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

# TEST
#print(block_to_block_type("# This is heading.\n###### and also new line."))
#print(block_to_block_type("```This is code.\n with many\nline\nhahaha.```"))
#print(block_to_block_type(">This is code.\n> with many\n>line\n>hahaha.```"))
#print(block_to_block_type("* This is code.\n* with many\n- line\n- hahaha.```"))
#print(block_to_block_type("1. This is code.\n2. with many\n3. line\n4. hahaha.```"))
#print(block_to_block_type("This is code.\nwith many\nline\n4. hahaha.```"))
