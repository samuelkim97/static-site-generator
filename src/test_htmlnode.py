import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parent(self):
        parent = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),]).to_html()
        print(parent)
        parent2 = ParentNode("html", [
            ParentNode("h1", [LeafNode("p", "This is h1"), LeafNode("a", "image", {"href": "www.google.com", "alt": "alt"})]),
            LeafNode("p", "This is paragraph")
        ]).to_html()
        print(parent2)
        self.assertEqual(parent, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(parent2, "<html><h1><p>This is h1</p><a href=\"www.google.com\" alt=\"alt\">image</a></h1><p>This is paragraph</p></html>")


if __name__ == "__main__":
    unittest.main()
    
