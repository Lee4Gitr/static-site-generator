import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestTextNodeSplitting(unittest.TestCase):
    def test_basic_functionality(self):
        node = TextNode("This is `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, "")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_missing_delimiter(self):
        node = TextNode("This is incomplete `code", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_text_without_delimiters(self):
        node = TextNode("No special delimiters here.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "No special delimiters here.")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

if __name__ == '__main__':
    unittest.main()
