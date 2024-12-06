print('Hello World')
from textnode import TextNode, TextType 
def main():
    text_node = TextNode('this is a test', TextType.NORMAL, None)
    second_text_node = TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev')
    link_text_node = TextNode('This is a link', TextType.LINK, 'https://www.boot.dev')
    
    print(text_node)
    print(second_text_node)
    print(link_text_node)

if __name__ == '__main__':
    main()
