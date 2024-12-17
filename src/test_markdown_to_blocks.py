import unittest

from markdown_to_blocks import markdown_to_blocks
class TestMarkdownToBlock(unittest.TestCase):
        def test_markdown_to_blocks(self):
            multiline_string = """
                        # This is a heading

                        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                        * This is the first list item in a list block
                        * This is a list item
                        * This is another list item"""


            blocks = markdown_to_blocks(multiline_string)
            self.assertEqual(len(blocks), 3)
if __name__ == "__main__":
    unittest.main()
