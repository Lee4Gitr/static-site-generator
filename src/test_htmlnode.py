import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode(props={"src": "Test"})
        self.assertEqual(node.props_to_html(), ' src="Test"')
    
    def test_eq(self):
        node = HTMLNode(props={"div": "This is a text node"})
        node2 = HTMLNode(props={"div": "This is a text node"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_other_props_to_html(self):
        node = HTMLNode(props={"target": "_blank"})
        self.assertEqual(node.props_to_html(), ' target="_blank"')
    
if __name__ == "__main__":
    unittest.main()
