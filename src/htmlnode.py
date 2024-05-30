# basic structure
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # tag name
        self.value = value # content of tag
        self.children = children # list
        self.props = props # dictionary

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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf node requires a value.")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        str = f"LeafNode({self.tag}, {self.value}, {self.props})"
        return str

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("There is no tag.")
        if self.children == None:
            raise ValueError("There is no children")
        child_html = ""
        for leafnode in self.children:
            if hasattr(leafnode, "__iter__"):
                for child_leafnode in leafnode:
                    child_html += child_leafnode.to_html()
            else:
                child_html += leafnode.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"

    def __repr__(self):
        str = f"ParentNode({self.tag}, {self.children}, {self.props})"
        return str
