import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        html = HTMLNode("h1", "a")
        self.assertTrue(HTMLNode())


if __name__ == "__main__":
    unittest.main()
    
