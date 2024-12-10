import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def url_not_link(self):
        node = TextNode("This is a test", TextType.NORMAL)
        node2 = TextNode("This is a test", TextType.NORMAL, 'https://www.boot.dev')
        self.assertEqual(node.repr, node2.repr)

    def url_displays(self):
        node = TextNode("Test URL", TextType.LINK, 'https://www.boot.dev')
        node2 = TextNode("Test URL", TextType.LINK, 'https://www.boot.dev')
        self.assertTrue('src' in node.repr)
        self.assertEqual(node, node2)
    
    def different_types(self):
        node = TextNode("Test URL", TextType.BOLD) 
        node2 = TextNode("Test URL", TextType.NORMAL)
        self.assertNotEqual(node, node2)
        print('test_eq passed')
    
if __name__ == "__main__":
    unittest.main()
