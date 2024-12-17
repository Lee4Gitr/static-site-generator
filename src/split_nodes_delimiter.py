from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in node.text:
            new_nodes.append(node)
        else:
            split_nodes = node.text.split(delimiter)
            count_of_splits = node.text.count(delimiter)
            if count_of_splits % 2 != 0:
                raise Exception("Text is missing a closing delimiter.")
            text_nodes = []
            for index, split in enumerate(split_nodes):
                if index % 2 == 0:
                    text_nodes.append(TextNode(split, node.text_type))
                else:
                    text_nodes.append(TextNode(split, text_type))

            new_nodes.extend(text_nodes)

    return new_nodes
