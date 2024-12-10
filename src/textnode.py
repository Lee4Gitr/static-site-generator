from enum import Enum

class TextType(Enum):
    NORMAL = "p"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"


class TextNode():
    def __init__(self, text, text_type, url=None): 
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, text_node):
        text_is_equal = self.text == text_node.text
        text_type_is_equal = self.text_type == text_node.text_type
        url_is_equal = self.url == text_node.url
        
        if (text_is_equal and text_type_is_equal and url_is_equal):
            return True
        return False

    def __repr__(self):
        if (self.text_type == TextType.LINK):
            return f"<{self.text_type.value} src='{self.url}'>{self.text}</{self.text_type.value}>"
        else:
            return f"<{self.text_type.value}>{self.text}</{self.text_type.value}>"


