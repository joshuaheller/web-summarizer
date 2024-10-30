class WebsiteContent:
    def __init__(self):
        self.url = ""
        self.language = ""
        self.title = ""
        self.headings = ""
        self.texts = []
        self.footer = ""
        self.images = []

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