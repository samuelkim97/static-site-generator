import re

# takes raw text and return list of tuples: [(type, link), (type1, link2)...]
def extract_markdown_images(text):
    image_regex = re.compile(r"!\[(.*?)]\((.*?\))")
    return image_regex.findall(text)

def extract_markdown_links(text):
    image_regex = re.compile(r"\[(.*?)]\((.*?\))")
    return image_regex.findall(text)

# FOR TEST

#text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
#print(extract_markdown_images(text))
# [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]:

#text1 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
#print(extract_markdown_links(text1))
# [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
