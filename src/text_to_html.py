from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    # I've decided to break this out into separate tags to better handle individual 
    # concerns for each element type. (semantics, nesting, etc.)
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text_type.value, text_node.text)
        case TextType.NORMAL: 
            return LeafNode(text_node.text_type.value, text_node.text)
        case TextType.BOLD: 
            return LeafNode(text_node.text_type.value, text_node.text)
        case TextType.ITALIC:
            return LeafNode(text_node.text_type.value, text_node.text)
        case TextType.CODE:
            return LeafNode(text_node.text_type.value, text_node.text)
        case TextType.LINK:
            return LeafNode(text_node.text_type.value, text_node.text, {"href": text_node.url, "alt": text_node.text})
        case TextType.IMAGE:
            return LeafNode(text_node.text_type.value, "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Unsupported HTML Type")
            
