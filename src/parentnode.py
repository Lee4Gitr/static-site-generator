from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super()
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided. A tag is necessary");
        elif self.children is None:
            raise ValueError("Children are required.")
        else:
            child_content = ''
            for child in self.children:
                child_content += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{child_content}</{self.tag}>"

    def __repr__(self):
        print(self.tag)
        print(self.value)
        print(self.children)
        print(self.props)
