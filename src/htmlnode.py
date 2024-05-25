# basic structure
class HTMLNode:
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag # tag name
        self.value = value # content of tag
        self.props = props # dictionary
        self.children = children # list

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f" {prop}=\"{self.props[prop]}\""
        return props_html

    def __repr__(self):
        str = f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}"
        return str

# html with no children
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf node requires a value.")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
