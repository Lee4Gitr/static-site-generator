import re
from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        matches = extract_markdown_links(original_text)
        previous_index = 0  # To track where the last match ended
        for match in matches:
            image_markdown = f"![{match['alt']}]({match['url']})"
            # Use the index of the image markdown for splits
            split_index = original_text.find(image_markdown)
            if split_index != -1:
                # Text before the image
                if original_text[:split_index]:
                    new_nodes.append(TextNode(original_text[:split_index], TextType.TEXT))
                # Image node
                new_nodes.append(TextNode(match['alt'], TextType.IMAGE, match['url']))
                # Update original_text to the remaining part after image markdown
                original_text = original_text[split_index + len(image_markdown):]
        # Append any remaining text
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
