import unittest

from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
    def test_converts_b(self):
        test_node = TextNode("Hello", TextType.BOLD)
        result = text_node_to_html_node(test_node)
        html = result.to_html()
        self.assertEqual('<b>Hello</b>', html)

    def test_converts_i(self):
        test_node = TextNode("Hello", TextType.ITALIC)
        result = text_node_to_html_node(test_node)
        html = result.to_html()
        self.assertEqual('<i>Hello</i>', html)

    def test_converts_p(self):
        test_node = TextNode("Hello", TextType.NORMAL)
        result = text_node_to_html_node(test_node)
        html = result.to_html()
        self.assertEqual('<p>Hello</p>', html)

    def test_converts_text(self):
        test_node = TextNode("Hello", TextType.TEXT)
        result = text_node_to_html_node(test_node)
        html = result.to_html()
        self.assertEqual('Hello', html)

    def test_converts_link(self):
        test_node = TextNode("Hello", TextType.LINK, 'www.google.com')
        result = text_node_to_html_node(test_node)
        html = result.to_html()
        self.assertEqual('<a href="www.google.com" alt="Hello">Hello</a>', html)

    def test_converts_img(self):
        test_node = TextNode("Hello", TextType.IMAGE, 'https://gratisography.com/wp-content/uploads/2024/10/gratisography-cool-cat-1035x780.jpg')
        result = text_node_to_html_node(test_node)
        html = result.to_html()
        self.assertEqual('<img src="https://gratisography.com/wp-content/uploads/2024/10/gratisography-cool-cat-1035x780.jpg" alt="Hello"/>', html)




if __name__ == "__main__":
    unittest.main()
