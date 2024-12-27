import unittest

from htmlnode import LeafNode 

class TestLeafNode(unittest.TestCase):
    def test_print(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")
    
    def test_print_with_single_prop(self):
        node = LeafNode("a", "Link Text", props={"href": "www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com">Link Text</a>')
    
    def test_print_with_multiple_props(self):
        node = LeafNode("a", "Link Text", props={"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="www.google.com" target="_blank">Link Text</a>')
    
if __name__ == "__main__":
    unittest.main()
