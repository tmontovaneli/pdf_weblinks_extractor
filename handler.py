from abc import ABC

class DefaultHandler(ABC):
    def handle(self, hyperlink):
        return 'Hello from default {link}'.format(link=hyperlink)

class HomedepotHandler(DefaultHandler):
    def handle(self, hyperlink):
        return 'Hello from homedepot {link}'.format(link=hyperlink)

class Ikea(DefaultHandler):
    def handle(self, hyperlink):
        return 'Hello from IKEA {link}'.format(link=hyperlink)
