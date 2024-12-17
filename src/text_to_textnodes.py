from textnode import TextNode, TextType, textnode
from htmlnode import HTMLNode

def text_to_textnodes(text):
    nodes = []
    position = 0
    while position < len(text):
        if text.startswith("**", position):
            end = text.find("**", position + 2)
            if end != -1:
                bold_text = text[position + 2:end]
                nodes.append(TextNode(bold_text, TextType.BOLD))
                position = end + 2
            else:
                break
        elif text.startswith("*", position):
            end = text.find("*", position + 1)
            if end != -1:
                italic_text = text[position + 1:end]
                nodes.append(TextNode(italic_text, TextType.ITALIC))
                position = end + 1
            else:
                break
        elif text.startswith("`", position):
            end = text.find("`", position + 1)
            if end != -1:
                code_text = text[position + 1:end]
                nodes.append(TextNode(code_text, TextType.CODE))
                position = end + 1
            else:
                break
        elif text.startswith("![", position):
            end = text.find("]", position + 1)
            if end != -1:
                image_text = text[position + 1:end]
                nodes.append(TextNode(image_text, TextType.IMAGE))
                position = end + 1
            else:
                break
        elif text.startswith("[", position):
            end = text.find("]", position + 1)
            if end != -1:
                link_text = text[position + 1:end]
                nodes.append(TextNode(link_text, TextType.LINK))
                position = end + 1
            else:
                break
        else:
            next_special = len(text)
            for delimiter in ["**", "*", "`", "[", "!["]:
                delimiter_pos = text.find(delimiter, position)
                if delimiter_pos != -1 and delimiter_pos < next_special:
                    next_special = delimiter_pos
            regular_text = text[position:next_special]
            if regular_text:
                nodes.append(TextNode(regular_text, TextType.TEXT))
            position = next_special
    return nodes
