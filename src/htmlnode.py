class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # tag name
        self.value = value # content of tag
        self.children = children # list
        self.props = props # dictionary

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        li = []
        for key, value in self.props.items():
            li.append("".join([key, value]))
        return " ".join(li) 

    def __repr__(self):
        str = f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}"
        return str

