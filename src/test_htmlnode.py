import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        html = HTMLNode("h1", "a")
        self.assertTrue(HTMLNode())

    def test_leaf(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.").to_html()
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        print(leaf1)
        print(leaf2)
        self.assertTrue(leaf1)
        self.assertTrue(leaf2)



if __name__ == "__main__":
    unittest.main()
    
