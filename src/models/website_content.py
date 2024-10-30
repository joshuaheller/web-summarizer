class WebsiteContent:
    def __init__(self, url="", language="", title="", headings="", texts=None, footer="", images=None):
        self.url = url
        self.language = language
        self.title = title
        self.headings = headings
        self.texts = texts if texts is not None else []
        self.footer = footer
        self.images = images if images is not None else []

    def to_dict(self):
        return {
            "url": self.url,
            "language": self.language,
            "title": self.title,
            "headings": self.headings,
            "texts": self.texts,
            "footer": self.footer,
            "images": self.images
        }