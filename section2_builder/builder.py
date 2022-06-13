class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        # indents
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        # text
        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        # child elements
        for e in self.elements:
            lines.append(e.__str(indent + 1))

        # closing tag
        lines.append(f'{i}</{self.name}>')

        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    def create(name):
        return HtmlBuilder(name)

class HtmlBuilder:
    __root = HtmlElement()

    def __initi__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def __str__(self):
        return str(self.__root)
