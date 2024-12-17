import unittest

from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_print_child(self):
        child = LeafNode("p", "This is a paragraph")
        children = [child]
        node = ParentNode("div", children)
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")

    def test_print_nested_parent(self):
        child = LeafNode("p", "This is a paragraph")
        children = [child]
        parent = ParentNode("div", children)
        parents = [parent]
        grandparent = ParentNode("div", parents)
        self.assertEqual(grandparent.to_html(), "<div><div><p>This is a paragraph</p></div></div>")

    def test_print_nested_parents(self):
        child = LeafNode("p", "This is a paragraph")
        children = [child]
        parent = ParentNode("div", children)
        parent2 = ParentNode("div", children)
        parents = [parent, parent2]
        grandparent = ParentNode("div", parents)
        self.assertEqual(grandparent.to_html(), "<div><div><p>This is a paragraph</p></div><div><p>This is a paragraph</p></div></div>")

    def test_parent_with_inline_items(self):
        bold = LeafNode("b", "Bold text")
        regular = LeafNode(None, "Normal text")
        italic = LeafNode("i", "Italic text")

        children = [bold, regular, italic, regular]

        parent = ParentNode("p", children)

        self.assertEqual(parent.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")
if __name__ == "__main__":
    unittest.main()
