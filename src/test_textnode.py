import unittest
from textnode import text_node_to_html_node

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_to_html(self):
        text1 = TextNode("This is bold", "bold")
        html1 = text_node_to_html_node(text1)
        print(text1, html1)
        self.assertEqual(html1, "<b>This is bold</b>")
        
if __name__ == "__main__":
    unittest.main()

